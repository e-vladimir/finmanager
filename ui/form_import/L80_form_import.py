# ФОРМА ИМПОРТА ДАННЫХ: ЛОГИКА ДАННЫХ

from L00_formats     import *

from L70_form_import import C70_FormImport
from L90_finstruct   import C90_RecordFinstruct


class C80_FormImport(C70_FormImport):
	""" Форма импорта данных: Логика данных """

	# Импорт
	def StartStopImport(self):
		""" Выполнение импорта """
		self._flag_processing = not self._flag_processing
		self.ShowStateProcessing()

		if not self._flag_processing: return

		index_page : int = self.tbs_input.currentIndex()
		if index_page == 0: self.ExecImportFindata()

	def ExecImportFindata(self):
		""" Импорт финданных """
		if     self._findata_path_file is None : return
		if not self._findata_path_file.exists(): return
		if     self._findata_path_file.is_dir(): return

		if   self._findata_format == FORMAT_TINKOFF : file_encoding = "1251"
		elif self._findata_format == FORMAT_SBERBANK: file_encoding = "utf-8"
		else                                        : return

		dy            : int  = self.workspace.Dy()
		dm            : int  = self.workspace.Dm()

		finstruct_record     = C90_RecordFinstruct()
		finstruct_record.SwitchByName(dy, dm, self._findata_finstruct_name)

		finstruct_oid : str  = finstruct_record.Oid().text
		if not finstruct_oid                   : return

		with open(self._findata_path_file, "r", encoding=file_encoding) as raw_file:
			self.on_ImportStarted()

			raw_data : list[str] = raw_file.readlines()

			self._statistic_count_total = len(raw_data) - 1

			for raw_line in raw_data[1:]:
				if not self._flag_processing: break

				flag_imported : bool = self.findata.ImportFindataFromCsv(raw_line, self._findata_format, finstruct_oid, dy, dm)

				self.application.processEvents()

				self._statistic_count_processed += 1
				self._statistic_count_imported  += 1 if     flag_imported else 0
				self._statistic_count_skipped   += 1 if not flag_imported else 0

		self.on_ImportFinished()
		self.application.form_findata.UpdateData()

# ФОРМА ЭКСПОРТА: ЛОГИКА ДАННЫХ

from pathlib         import Path

from L20_PySide6     import ShowMessage
from L70_form_export import C70_FormExport
from L90_findata     import C90_RecordFindata
from L90_finstruct   import C90_RecordFinstruct


class C80_FormExport(C70_FormExport):
	""" Форма экспорта: Логика данных """

	# Экспорт
	def StartStopExport(self):
		""" Старт/Стоп запуска экспорта """
		if not self._flag_exporting: self.ExecExportFindata()
		else                       : self.SwitchFlagExportingOff()

	def ExecExportFindata(self):
		""" Выполнить экспорт финданных """
		self.on_ExportStarted()

		oids : list[str] = []

		dys  : list[int] = [self._findata_dy]
		dms  : list[int] = [1]

		if not self._findata_dm: dms = list(range(1, 13))

		for dy in dys:
			for dm in dms:
				for dd in range(1, 31):
					oids.extend(self.findata.OidsInDyDmDd(dy, dm, dd))

		self._statistic_count_total = len(oids)

		data : list[str] = []
		data.append("Дата;Сумма;Примечание")

		for oid in oids:
			self._statistic_count_processed += 1

			record_findata   = C90_RecordFindata(oid)
			record_finstruct = C90_RecordFinstruct(record_findata.FinstructOid())

			if not record_finstruct.Name() == self._findata_finstruct: continue

			self._statistic_count_exported  += 1

			data.append(record_findata.ExportToCsv())

			self.on_ExportProcessing()

		self.on_ExportFinished()

		if len(data) == 1              : return
		if self._findata_folder is None: return

		path_filename : Path = self._findata_folder.joinpath(f"{self._findata_filename}.csv")

		with open(path_filename, "w", encoding="utf-8") as csv_file: csv_file.write('\n'.join(data))

		ShowMessage("Экспорт финданных", "Экспорт финданных завершён.", f"{path_filename}")

# ФОРМА ИМПОРТА ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

from L00_formats     import *

from L10_converts    import SecondsToThTmTs

from L60_form_import import C60_FormImport


class C70_FormImport(C60_FormImport):
	""" Форма импорта данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Импорт данных - {self.workspace.DmDyToString()}")

	# Вкладка: Финданные
	def FillFindataFinstruct(self):
		""" Заполнение списка записей финструктуры """
		dy : int = self.workspace.Dy()
		dm : int = self.workspace.Dm()

		self.cbb_findata_finstruct.clear()
		self.cbb_findata_finstruct.addItems(self.finstruct.SubNamesInDyDm(dy, dm))

	def FillFindataFormats(self):
		""" Заполнение списка форматов """
		formats : list[str] = []
		formats.append(FORMAT_TINKOFF)
		formats.append(FORMAT_SBERBANK)

		self.cbb_findata_format.clear()
		self.cbb_findata_format.addItems(sorted(formats))

	def ShowFindata(self):
		""" Отображение параметров финданных """
		self.btn_findata_file.setText("...")
		self.lbl_findata_folder.setText("...")

		if self._findata_path_file is None: return

		self.btn_findata_file.setText(f"{self._findata_path_file.name}")
		self.lbl_findata_folder.setText(f"{self._findata_path_file.parents[0]}")

	# Вкладка: Статистика
	def ShowStatistics(self):
		""" Отображение статистики """
		self.lbl_statistic_count_processed.setText(f"{self._statistic_count_processed}")
		self.lbl_statistic_count_left.setText(f"{self._statistic_count_left}")

		self.lbl_statistic_count_imported.setText(f"{self._statistic_count_imported}")
		self.lbl_statistic_count_skipped.setText(f"{self._statistic_count_skipped}")

		self.lbl_statistic_time_processed.setText(SecondsToThTmTs(self._statistic_time_processed))
		self.lbl_statistic_time_left.setText(SecondsToThTmTs(self._statistic_time_left))

	def ShowStateProcessing(self):
		""" Отображение состояния импорта """
		self.btn_exec_import.setText("Выполнить импорт" if not self._flag_processing else "Остановить импорт")

# ФОРМА ИМПОРТА ДАННЫХ: МЕХАНИКА ДАННЫХ

from pathlib           import Path

from PySide6.QtWidgets import QFileDialog

from G10_datetime      import CurrentUTime

from L50_form_import   import C50_FormImport


class C60_FormImport(C50_FormImport):
	""" Форма импорта данных: Механика данных """

	# Статистика
	def ReadStatisticUtimeStart(self):
		""" Фиксация времени старта импорта """
		self._statistic_utime_start = CurrentUTime()

	def CalcStatistic(self):
		""" Расчёт показателей статистики """
		self._statistic_count_left     = self._statistic_count_total - self._statistic_count_processed
		self._statistic_time_processed = CurrentUTime() - self._statistic_utime_start

		if not self._statistic_count_processed: return
		self._statistic_time_left      = int((self._statistic_time_processed / self._statistic_count_processed) * self._statistic_count_left)

	def ResetStatistic(self):
		""" Сброс статистики """
		self._statistic_count_total     = 0
		self._statistic_count_processed = 0
		self._statistic_count_left      = 0

		self._statistic_count_imported  = 0
		self._statistic_count_skipped   = 0

	# Вкладка: Финданные
	def RequestFindataFilename(self):
		""" Выбрать файл для импорта финданных """
		dialog                = QFileDialog(self)

		filename, file_filter = dialog.getOpenFileName(self)
		if not filename: return

		self._findata_path_file = Path(filename)
		self.on_FindataSelectedFile()

	def ReadFindataFinstructName(self):
		""" Считывание имени финструктуры """
		self._findata_finstruct_name = self.cbb_findata_finstruct.currentText()

	def ReadFindataFormat(self):
		""" Считывание формата импорта финданных """
		self._findata_format = self.cbb_findata_format.currentText()

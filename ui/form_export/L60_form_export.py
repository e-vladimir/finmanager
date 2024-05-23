# ФОРМА ЭКСПОРТА: МЕХАНИКА ДАННЫХ

import os

from   pathlib         import Path

from   G10_datetime    import CurrentUTime

from   L20_PySide6     import RequestDirectory
from   L50_form_export import C50_FormExport


class C60_FormExport(C50_FormExport):
	""" Форма экспорта: Механика данных """

	# Системные параметры
	def SwitchFlagLoadingOn(self):
		""" Включение признака загрузки """
		self._flag_loading = True

	def SwitchFlagLoadingOff(self):
		""" Отключение признака загрузки """
		self._flag_loading = False

	def SwitchFlagExportingOn(self):
		""" Включение признака экспорта """
		self._flag_exporting = True

	def SwitchFlagExportingOff(self):
		""" Отключение признака экспорта """
		self._flag_exporting = False

	# Параметры финданных
	def ReadFindataDyDm(self):
		""" Чтение года """
		if self._flag_loading: return

		try   : self._findata_dy = int(self.cbb_findata_dy.currentText())
		except: pass

		self._findata_dm = self.cbb_findata_dm.currentIndex()

		self.on_FindataDyDmChanged()
		self.on_FindataOptionsChanged()

	def ReadFindataFinstruct(self):
		""" Чтение финструктуры """
		if self._flag_loading: return

		self._findata_finstruct = self.cbb_findata_finstruct.currentText()

		self.on_FindataOptionsChanged()

	def GenerateFindataFilename(self):
		""" Генерация имени файла для экспорта финданных """
		self._findata_filename  = ""

		if not self._findata_finstruct: return
		if not self._findata_dy       : return

		self._findata_filename  = self._findata_finstruct
		self._findata_filename += f"_{self._findata_dy}"

		if not self._findata_dm       : return
		self._findata_filename += f"_{self._findata_dm}"

	def SetFindataFolder(self):
		""" Установка директории экспорта финданных """
		folder : Path | None = RequestDirectory("Экспорт финданных", f"{self._findata_folder}")

		if folder is None: return

		self._findata_folder = folder

		self.on_FindataOptionsChanged()

	def SetFindataFolderToCurrent(self):
		""" Установка директории экспорта на текущую """
		self._findata_folder = Path(os.getcwd())

	# Статистика
	def MemoryTimeStart(self):
		""" Фиксация времени старта """
		self._statistic_time_started = CurrentUTime()

	def CalcStatistic(self):
		""" Расчёт показателей статистики """
		self._statistic_count_left      = self._statistic_count_total - self._statistic_count_processed

		self._statistic_time_processing = CurrentUTime() - self._statistic_time_started

		k_processing : float = 0.00 if not self._statistic_time_processing else (self._statistic_count_processed / self._statistic_time_processing)
		self._statistic_time_left       = int(self._statistic_count_left * k_processing)

	def ResetStatistic(self):
		""" Сброс статистики """
		self._statistic_count_total     : int         = 0
		self._statistic_count_processed : int         = 0
		self._statistic_count_left      : int         = 0
		self._statistic_count_exported  : int         = 0
		self._statistic_time_started    : int         = 0
		self._statistic_time_processing : int         = 0
		self._statistic_time_left       : int         = 0

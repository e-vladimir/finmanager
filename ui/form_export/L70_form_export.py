# ФОРМА ЭКСПОРТА: МЕХАНИКА УПРАВЛЕНИЯ

from G10_cactus_convertors import AnyToStrings

from L00_months            import MONTHS_SHORT

from L10_converts          import SecondsToThTmTs
from L60_form_export       import C60_FormExport


class C70_FormExport(C60_FormExport):
	""" Форма экспорта: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle("Экспорт данных")

	# Панель финданных
	def LoadFindataDy(self):
		""" Загрузка списка годов """
		self.cbb_findata_dy.clear()
		self.cbb_findata_dy.addItems(AnyToStrings(self.workspace.Dys()))

	def LoadFindataDm(self):
		""" Загрузка списка месяцев """
		self.cbb_findata_dm.clear()
		self.cbb_findata_dm.addItems(MONTHS_SHORT)

	def LoadFindataFinstruct(self):
		""" Загрузка финструктуры """
		names  : set[str]  = set()
		months : list[int] = []

		if not self._findata_dm: months = list(range(1, 12))
		else                   : months.append(self._findata_dm)

		for index_month in months: names = names.union(set(self.finstruct.SubNamesInDyDm(self._findata_dy, index_month, "")))

		self.cbb_findata_finstruct.clear()
		self.cbb_findata_finstruct.addItems(sorted(names))

	def LoadDyDmFromWorkspace(self):
		""" Смена года и месяца на данные из рабочего пространства """
		self.cbb_findata_dy.setCurrentText(f"{self.workspace.Dy()}")
		self.cbb_findata_dm.setCurrentIndex(self.workspace.Dm())

	def ShowFindataFilename(self):
		""" Отображение имени файла финданных """
		self.lbl_findata_filename.setText(self._findata_filename)

	def ShowFindataFolder(self):
		""" Отображение директории экспорта финданных """
		self.btn_findata_directory.setText(f"{self._findata_folder}")

	# Панель Статистики
	def ShowExportState(self):
		""" Отображение состояния экспорта """
		self.btn_exec_export.setText("Остановить" if self._flag_exporting else "Выполнить экспорт")

	def ShowExportStatistic(self):
		""" Отображение статистики """
		self.lbl_statistic_count_processed.setText(f"{self._statistic_count_processed}")
		self.lbl_statistic_count_left.setText(f"{self._statistic_count_left}")

		self.lbl_statistic_count_exported.setText(f"{self._statistic_count_exported}")

		self.lbl_statistic_time_processed.setText(SecondsToThTmTs(self._statistic_time_processing))
		self.lbl_statistic_time_left.setText(SecondsToThTmTs(self._statistic_time_left))

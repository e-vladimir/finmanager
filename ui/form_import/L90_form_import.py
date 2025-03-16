# ФОРМА ИМПОРТ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 14 мар 2025

from L80_form_import import C80_FormImport


class C90_FormImport(C80_FormImport):
	""" Форма Импорт данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица данных импорта операций
		self.TableDataOperations.customContextMenuRequested.connect(self.on_RequestShowMenuOperations)

		# Меню Импорт операций
		self.ActionLoadOperationsFromFile.triggered.connect(self.on_RequestLoadOperationsFromFile)

	# Форма
	def on_Opened(self):
		""" Форма открыта """
		self.ShowTitle()

		self.InitModelDataOperations()
		self.AdjustLabelOperations()

	# Меню Импорт операций
	def on_RequestShowMenuOperations(self):
		""" Запрос меню импорта операций """
		self.AdjustMenuOperations()
		self.AdjustMenuOperations_Text()
		self.AdjustMenuOperations_Enable()

		self.ShowMenuOperations()

	# Импорт операций
	def on_RequestLoadOperationsFromFile(self):
		""" Запрос загрузки данных импорта операций из файла """
		self.LoadOperationsDataFromFile()

	def on_OperationsDataLoaded(self):
		""" Данные импорта операций загружены """
		self.InitModelDataOperations()
		self.LoadModelDataOperations()

		self.AdjustTableOperations_Size()

		self.AdjustLabelOperations()

# ФОРМА ИМПОРТ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 14 мар 2025

from L80_form_import import C80_FormImport


class C90_FormImport(C80_FormImport):
	""" Форма Импорт данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица данных импорта операций
		self.TableDataOperations.customContextMenuRequested.connect(self.on_RequestShowMenuOperations)
		self.TableDataOperations.doubleClicked.connect(self.on_RequestEditOperationsField)

		# Меню Импорт операций
		self.ActionLoadOperationsFromFile.triggered.connect(self.on_RequestLoadOperationsFromFile)
		self.ActionEditOperationsStructField.triggered.connect(self.on_RequestEditOperationsField)
		self.ActionImportOperations.triggered.connect(self.on_RequestImportOperations)

	# Форма
	def on_Opened(self):
		""" Форма открыта """
		self.ShowTitle()

		self.InitModelDataOperations()
		self.AdjustLabelOperations()

	def on_RequestUpdateData(self):
		""" Запрос на обновление данных """
		if not self.isVisible(): return

		self.ShowTitle()


	# Меню Импорт операций
	def on_RequestShowMenuOperations(self):
		""" Запрос меню импорта операций """
		self.ReadProcessingRowFromTableDataOperations()

		self.AdjustMenuOperations()
		self.AdjustMenuOperations_Text()
		self.AdjustMenuOperations_Enable()

		self.ShowMenuOperations()


	# Импорт операций
	def on_RequestLoadOperationsFromFile(self):
		""" Запрос загрузки данных импорта операций из файла """
		self.LoadOperationsDataFromFile()

	def on_RequestEditOperationsField(self):
		""" Запрос установки типа поля для структуры данных импорта операций """
		self.ReadProcessingRowFromTableDataOperations()

		self.EditOperationsStructField()

	def on_RequestImportOperations(self):
		""" Запрос импорта операций """
		self.ImportOperations()

	def on_OperationsDataLoaded(self):
		""" Данные импорта операций загружены """
		self.InitModelDataOperations()

		self.AutodetectOperationsStructFields()
		self.LoadModelDataOperations()

		self.AdjustTableOperations_Size()

		self.AdjustLabelOperations()

	def on_OperationsStructChanged(self):
		""" Структура данных импорта операций изменилась """
		self.LoadModelDataOperations()

		self.AdjustTableOperations_Size()

	def on_Imported(self):
		""" Выполнен импорт данных """
		self.Workspace.CachingData()

		self.Application.FormOperations.PartialUpdateData()

		self.Application.FormAccounts.UpdateData()
		self.Application.FormMain.UpdateData()

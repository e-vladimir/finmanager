# ФОРМА ИМПОРТ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_import import C80_FormImport


class C90_FormImport(C80_FormImport):
	""" Форма Импорт данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица финансовых операций
		self.table_operations_data.customContextMenuRequested.connect(self.on_RequestShowMenuOperations)
		self.table_operations_data.doubleClicked.connect(self.on_RequestProcessingTableOperationsDbClick)

		# Меню импорта Финансовых операций
		self.action_operations_operations_open_file.triggered.connect(self.on_RequestOpenFileInOperations)
		self.action_operations_operations_switch_data.triggered.connect(self.on_RequestSwitchDataInOperation)
		self.action_operations_operations_exec_import.triggered.connect(self.on_RequestImportOperation)

		self.action_operations_header_set_field.triggered.connect(self.on_RequestSetFieldInOperation)

	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.InitOperationsModelData()

		self.LoadOperationsHeader()
		self.LoadOperationsFields()
		self.LoadOperationsData()

		self.AdjustTableOperations_Size()

	# Меню импорта финансовых операций
	def on_RequestShowMenuOperations(self):
		""" Запрос отображения меню импорта финансовых операций """
		self.ReadOperationsProcessingRowFromTableDataOperations()

		self.AdjustMenuOperations_Text()
		self.AdjustMenuOperations_Enable()

		self.ShowMenuOperations()

	def on_RequestOpenFileInOperations(self):
		""" Запрос на отрытие файла для импорта финансовых операций """
		self.ReadOperationsFile()
		self.ProcessingFileInOperations()

		self.InitOperationsModelData()

		self.LoadOperationsHeader()
		self.LoadOperationsFields()
		self.LoadOperationsData()

	def on_RequestSwitchDataInOperation(self):
		""" Запрос на смену набора данных импорта финансовых операций """
		self.LoadOperationsData()

	def on_RequestImportOperation(self):
		""" Запрос на выполнение импорта финансовых операций """
		self.ImportOperations()

		self.application.form_operations.UpdateData()

	def on_RequestSetFieldInOperation(self):
		""" Запрос на установку типа данных для элемента заголовка в импорте финансовых операций """
		self.SetFieldInOperations()

		self.LoadOperationsFields()

	# Таблица данных импорта финансовых данных
	def on_RequestProcessingTableOperationsDbClick(self):
		""" Запрос обработки двойного клика по таблице данных импорта финансовых данных """
		self.ReadOperationsProcessingRowFromTableDataOperations()

		self.SetFieldInOperations()

		self.LoadOperationsFields()

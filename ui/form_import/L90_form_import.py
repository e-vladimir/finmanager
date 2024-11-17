# ФОРМА ИМПОРТ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_import import C80_FormImport


class C90_FormImport(C80_FormImport):
	""" Форма Импорт данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица финансовых операций
		self.table_operations_data.customContextMenuRequested.connect(self.on_RequestShowMenuOperations)

		# Меню импорта Финансовых операций
		self.action_operations_open_file.triggered.connect(self.on_RequestOpenFileOperations)
		self.action_operations_switch_data.triggered.connect(self.on_RequestSwitchDataOperation)

	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.InitModelOperations()

		self.LoadOperationsHeader()
		self.LoadOperationsOptions()
		self.LoadOperationsData()

		self.AdjustTableOperations_Size()

	# Меню импорта финансовых операций
	def on_RequestShowMenuOperations(self):
		""" Запрос отображения меню импорта финансовых операций """
		self.AdjustMenuOperations_Text()
		self.AdjustMenuOperations_Enable()

		self.ShowMenuOperations()

	def on_RequestOpenFileOperations(self):
		""" Запрос на отрытие файла для импорта финансовых операций """
		self.ReadOperationsFile()
		self.ProcessingFileForOperations()

		self.InitModelOperations()

		self.LoadOperationsHeader()
		self.LoadOperationsOptions()
		self.LoadOperationsData()

	def on_RequestSwitchDataOperation(self):
		""" Запрос на смену набора данных импорта финансовых операций """
		self.LoadOperationsData()

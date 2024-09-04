# ФОРМА ИМПОРТ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_import import C80_FormImport


class C90_FormImport(C80_FormImport):
	""" Форма Импорт данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица данных импорта финдействий
		self.table_import_finactions_data.customContextMenuRequested.connect(self.on_RequestShowMenuImportFinactions)
		self.table_import_finactions_data.doubleClicked.connect(self.on_RequestSetFieldImportFinactions)

		# Меню импорта финдействий
		self.menu_import_finactions_source_open_file.triggered.connect(self.on_RequestOpenImportFinactionsFile)

		self.menu_import_finactions_column_set_field.triggered.connect(self.on_RequestSetFieldImportFinactions)
		self.menu_import_finactions_column_reset_field.triggered.connect(self.on_RequestResetFieldImportFinactions)

		self.menu_import_finactions_exec_import.triggered.connect(self.on_RequestExecImportFinactions)

	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

	# Меню импорта финдействий
	def on_RequestShowMenuImportFinactions(self):
		""" Запрос отображения меню импорта финдействий """
		self.ReadProcessingColumnFromTableImportFinactionsData()
		self.ReadProcessingNameFromTableImportFinactionsData()

		self.AdjustMenuImportFinactions_Enable()
		self.AdjustMenuImportFinactions_Text()

		self.ShowMenuImportFinactions()

	# Импорт финдействий
	def on_RequestOpenImportFinactionsFile(self):
		""" Запрос файла импорта финдействий """
		self.OpenLocalFileImportFinactions()

		self.AdjustPageFinactions_Text()

		self.LoadModelImportFinactionsData()

		self.AdjustTableImportFinactionsData_Size()
		self.AdjustTableImportFinactionsData_Color()

	# Таблица данных импорта финдействий
	def on_RequestSetFieldImportFinactions(self):
		""" Запрос установки типа поля колонки данных импорта финдействий """
		self.ReadProcessingColumnFromTableImportFinactionsData()
		self.ReadProcessingNameFromTableImportFinactionsData()

		self.SetFieldImportFinactionsHeader()

		self.LoadModelImportFinactionsData()

		self.AdjustTableImportFinactionsData_Size()
		self.AdjustTableImportFinactionsData_Color()

	def on_RequestResetFieldImportFinactions(self):
		""" Запрос сброса типа поля колонки данных импорта финдействий """
		self.ResetFieldImportFinactionsHeader()

		self.LoadModelImportFinactionsData()

		self.AdjustTableImportFinactionsData_Size()
		self.AdjustTableImportFinactionsData_Color()

	def on_RequestExecImportFinactions(self):
		""" Запрос на выполнение импорта финдействий """
		self.ExecImportFinactions()

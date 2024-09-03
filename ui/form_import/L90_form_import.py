# ФОРМА ИМПОРТ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_import import C80_FormImport


class C90_FormImport(C80_FormImport):
	""" Форма Импорт данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица данных импорта финдействий
		self.table_import_finactions_data.customContextMenuRequested.connect(self.on_RequestShowMenuImportFinactions)

		# Меню импорта финдействий
		self.menu_import_finactions_open_file.triggered.connect(self.on_RequestOpenImportFinactionsFile)

	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

	# Меню импорта финдействий
	def on_RequestShowMenuImportFinactions(self):
		""" Запрос отображения меню импорта финдействий """
		self.AdjustMenuImportFinactions_Enable()
		self.AdjustMenuImportFinactions_Text()

		self.ShowMenuImportFinactions()

	# Импорт финдействий
	def on_RequestOpenImportFinactionsFile(self):
		""" Запрос файла импорта финдействий """
		self.OpenLocalFileImportFinactions()

		self.AdjustPageFinactions_Text()

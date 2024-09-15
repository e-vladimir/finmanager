# ФОРМА ЭКСПОРТ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_export import C80_FormExport


class C90_FormExport(C80_FormExport):
	""" Форма Экспорт данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица данных экспорта финдействий
		self.table_finactions_data.doubleClicked.connect(self.on_RequestProcessingDbClickTableFinactionsData)
		self.table_finactions_data.customContextMenuRequested.connect(self.on_RequestShowMenuExportFinactions)

		# Меню экспорта финдействий
		self.menu_export_finactions_period_mode.triggered.connect(self.on_RequestSetOptionsFinactionsPeriodMode)
		self.menu_export_finactions_period_dy.triggered.connect(self.on_RequestSetOptionsFinactionsPeriodDy)
		self.menu_export_finactions_period_dm.triggered.connect(self.on_RequestSetOptionsFinactionsPeriodDm)

		self.menu_export_finactions_finstruct_mode.triggered.connect(self.on_RequestSetOptionsFinactionsFinstructMode)
		self.menu_export_finactions_finstruct_name.triggered.connect(self.on_RequestSetOptionsFinactionsFinstructName)

		self.menu_export_finactions_folder.triggered.connect(self.on_RequestSetOptionsFinactionsFolder)

		self.menu_export_finactions_exec_export.triggered.connect(self.on_RequestProcessingExportFinactions)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.InitModelFinactions()
		self.CalcOptionsFinactionsFilenames()
		self.LoadModelFinactions()
		self.AdjustTableFinactionsData_Span()
		self.AdjustTableFinactionsData_Size()
		self.AdjustTableFinactionsData_Colors()
		self.AdjustTableFinactionsData_Align()

	# Таблица данных экспорта финдействий
	def on_RequestProcessingDbClickTableFinactionsData(self):
		""" Запрос обработки двойного клика по таблице данных экспорта финдействий """
		self.ReadProcessingRowFromTableFinactionsData()
		self.ProcessingDbClickTableFinactionsData()

	def on_RequestSetOptionsFinactionsPeriodMode(self):
		""" Запрос на установку режима выборки периода в параметрах экспорта финдействий """
		self.SetOptionsFinactionsPeriodMode()
		self.CalcOptionsFinactionsFilenames()

		self.LoadModelFinactions()

		self.AdjustTableFinactionsData_Size()
		self.AdjustTableFinactionsData_Colors()

	def on_RequestSetOptionsFinactionsPeriodDm(self):
		""" Запрос на установку месяца периода в параметрах экспорта финдействий """
		self.SetOptionsFinactionsPeriodDm()
		self.CalcOptionsFinactionsFilenames()

		self.LoadModelFinactions()

		self.AdjustTableFinactionsData_Size()
		self.AdjustTableFinactionsData_Colors()

	def on_RequestSetOptionsFinactionsPeriodDy(self):
		""" Запрос на установку года периода в параметрах экспорта финдействий """
		self.SetOptionsFinactionsPeriodDy()
		self.CalcOptionsFinactionsFilenames()

		self.LoadModelFinactions()

		self.AdjustTableFinactionsData_Size()
		self.AdjustTableFinactionsData_Colors()

	def on_RequestSetOptionsFinactionsFinstructMode(self):
		""" Запрос на установку режима выборки счёта в параметрах экспорта финдействий """
		self.SetOptionsFinactionsFinstructMode()
		self.CalcOptionsFinactionsFilenames()

		self.LoadModelFinactions()

		self.AdjustTableFinactionsData_Size()
		self.AdjustTableFinactionsData_Colors()

	def on_RequestSetOptionsFinactionsFinstructName(self):
		""" Запрос на установку наименования счёта в параметрах экспорта финдействий """
		self.SetOptionsFinactionsFinstructNames()
		self.CalcOptionsFinactionsFilenames()

		self.LoadModelFinactions()

		self.AdjustTableFinactionsData_Size()
		self.AdjustTableFinactionsData_Colors()

	def on_RequestSetOptionsFinactionsFolder(self):
		""" Запрос на установку директории в параметрах экспорта финдействий """
		self.SetOptionsFinactionsFolder()
		self.LoadModelFinactions()

		self.AdjustTableFinactionsData_Size()
		self.AdjustTableFinactionsData_Colors()

	# Меню экспорта финдействий
	def on_RequestShowMenuExportFinactions(self):
		""" Запрос на вызов меню экспорта финдействий """
		self.AdjustMenuExportFinactions_Enable()
		self.ShowMenuExportFinactions()

	# Экспорт финдействий
	def on_RequestProcessingExportFinactions(self):
		""" Запрос экспорта финдействий """
		self.ProcessingExportFinactions()

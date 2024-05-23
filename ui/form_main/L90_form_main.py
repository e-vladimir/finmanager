# ФОРМА ОСНОВНАЯ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_main import C80_FormMain


class C90_FormMain(C80_FormMain):
	""" Форма основная: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Панель управления финпериодом
		self.cbbox_dy.currentIndexChanged.connect(self.on_SwitchDyDm)
		self.cbbox_dm.currentIndexChanged.connect(self.on_SwitchDyDm)

		self.btn_dm_prev.clicked.connect(self.on_RequestPrevDm)
		self.btn_dm_next.clicked.connect(self.on_RequestNextDm)

		# Каталоги
		self.btn_findescription.clicked.connect(self.on_RequestOpenFindescription)

		# Оперативные данные
		self.btn_finstruct.clicked.connect(self.on_RequestOpenFinstruct)
		self.btn_findata.clicked.connect(self.on_RequestOpenFindata)

		# Инструментарий
		self.btn_rules.clicked.connect(self.on_RequestOpenRules)

		# Аналитика
		self.btn_finstatistic.clicked.connect(self.on_RequestOpenFinstatistic)
		self.btn_finanalytics.clicked.connect(self.on_RequestOpenFinanalytics)

		# Отчётность
		self.btn_report_summary.clicked.connect(self.on_RequestSummaryReport)
		self.btn_report_finstate.clicked.connect(self.on_RequestFinstateReport)

		# Утилиты
		self.btn_cleaner.clicked.connect(self.on_RequestOpenCleaner)
		self.btn_backups.clicked.connect(self.on_RequestOpenBackups)

	def on_Open(self):
		super().on_Open()

		self.workspace.SwitchToMain()

		self.SetupButtons()

		self.FillCbbDy()
		self.FillCbbDm()

		self.ShowDmFromWorkspace()
		self.ShowDyFromWorkspace()

		self.ShowTitle()

	# Финпериод
	def on_RequestNextDm(self):
		""" Смена финпериода на следующий месяц """
		self.workspace.ShiftByDm(1)

		self.ShowDmFromWorkspace()
		self.ShowDyFromWorkspace()
		self.ShowTitle()

	def on_RequestPrevDm(self):
		""" Смена финпериода на предыдущий месяц """
		self.workspace.ShiftByDm(-1)

		self.ShowDmFromWorkspace()
		self.ShowDyFromWorkspace()
		self.ShowTitle()

	def on_SwitchDyDm(self):
		""" Смена финпериода """
		self.ReadDyToWorkspace()
		self.ReadDmToWorkspace()

		self.ShowTitle()

	# Каталоги
	def on_RequestOpenFindescription(self):
		""" Открытие формы Финсостава """
		self.application.form_findescription.Open()

	def on_RequestOpenRules(self):
		""" Открытие формы Правил обработки """
		self.application.form_rules.Open()

	# Оперативные данные
	def on_RequestOpenFinstruct(self):
		""" Открытие формы Финструктуры """
		self.application.form_finstruct.Open()

	def on_RequestOpenFindata(self):
		""" Открытие формы Финданных """
		self.application.form_findata.Open()

	# Аналитика
	def on_RequestOpenFinstatistic(self):
		""" Запрос на открытие финстатистики """
		self.application.form_finstatistic.Open()

	def on_RequestOpenFinanalytics(self):
		""" Запрос на открытие Финаналитики """
		self.application.form_finanalytics.Open()

	# Отчётность
	def on_RequestSummaryReport(self):
		""" Запрос на генерацию сводного отчёта """
		self.GenerateSummaryReport()

	def on_RequestFinstateReport(self):
		""" Запрос на генерацию хронологии финсостояния """
		self.GenerateHistoryFinstateReport()

	# Утилиты
	def on_RequestOpenCleaner(self):
		""" Запрос на открытие Удаления данных """
		self.application.form_cleaner.Open()

	def on_RequestOpenBackups(self):
		""" Запрос на открытие Копии данных """
		self.application.form_backups.Open()

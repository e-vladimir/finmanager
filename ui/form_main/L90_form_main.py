# ФОРМА ОСНОВНАЯ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_main import C80_FormMain


class C90_FormMain(C80_FormMain):
	""" Форма основная: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Панель финпериода
		self.btn_dm_prev.clicked.connect(self.on_RequestPrevDm)
		self.btn_dm_next.clicked.connect(self.on_RequestNextDm)

		self.cbbox_dy.activated.connect(self.on_RequestSetDyDm)
		self.cbbox_dm.activated.connect(self.on_RequestSetDyDm)

		# Панель форм
		self.btn_fincomposition.clicked.connect(self.on_RequestOpenFincomposition)
		self.btn_finstruct.clicked.connect(self.on_RequestOpenFinstruct)
		self.btn_finactions.clicked.connect(self.on_RequestOpenFinactions)
		self.btn_finstatistics.clicked.connect(self.on_RequestOpenFinstatistics)
		self.btn_finanalitics.clicked.connect(self.on_RequestOpenFinanalitics)
		self.btn_rules.clicked.connect(self.on_RequestOpenRules)
		self.btn_backup.clicked.connect(self.on_RequestOpenBackups)

		# Панель отчётности
		self.cbbox_reports.activated.connect(self.on_RequestReport)

	# Форма
	def on_Show(self):
		""" Отображение формы """
		self.ShowTitle()

		self.FillCbboxDm()
		self.FillCbboxDy()

		self.FillCbbReports()

		self.ShowDm()
		self.ShowDy()

	def on_Close(self):
		self.application.Close()

	# Финпериод
	def on_RequestPrevDm(self):
		""" Смена финпериода на прошлый месяц """
		self.workspace.ShiftDmToPrevDm()

		self.ShowDm()
		self.ShowDy()

		self.ShowTitle()

	def on_RequestNextDm(self):
		""" Смена финпериода в следующий месяц """
		self.workspace.ShiftDmToNextDm()

		self.ShowDm()
		self.ShowDy()

		self.ShowTitle()

	def on_RequestSetDyDm(self):
		""" Ручной выбор финпериода """
		self.ReadProcessingDmFromCbboxDm()
		self.ReadProcessingDyFromCbboxDy()

		self.SetDyDm()

		self.ShowTitle()

	# Переход в другие формы
	def on_RequestOpenFincomposition(self):
		""" Открытие формы финсостава """
		self.application.form_fincomposition.Open()

	def on_RequestOpenFinstruct(self):
		""" Открытие формы финструктуры """
		self.application.form_finstruct.Open()

	def on_RequestOpenFinactions(self):
		""" Открытие формы финдейсвтий """
		self.application.form_finactions.Open()

	def on_RequestOpenRules(self):
		""" Открытие формы Правила """
		self.application.form_rules.Open()

	def on_RequestOpenBackups(self):
		""" Открытие формы Архивирования """
		self.application.form_backup.Open()

	def on_RequestOpenFinstatistics(self):
		""" Открытие формы Финстатистика """
		self.application.form_finstatistics.Open()

	def on_RequestOpenFinanalitics(self):
		""" Открытие формы Финаналитика """
		self.application.form_finanalitics.Open()

	def on_RequestReport(self):
		""" Запрос формирования отчёта """
		self.ReadProcessingReport()
		self.ProcessingRequestReport()
		self.ResetCbbReport()

	def on_RequestReportHistoryFinstate(self):
		""" Запрос формирования отчёта: Хронология финсостояния """
		self.GenerateReportHistoryFinstate()

	def on_RequestReportSummaryMonth(self):
		""" Запрос формирования отчёта: Сводный отчёт за месяц """
		self.GenerateReportSummaryMonth()

# ФОРМА ОСНОВНАЯ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_main import C80_FormMain


class C90_FormMain(C80_FormMain):
	""" Форма Основная: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Панель рабочего периода
		self.btn_dm_next.clicked.connect(self.on_RequestShiftDmToNext)
		self.btn_dm_prev.clicked.connect(self.on_RequestShiftDmToPrev)

		self.btn_dmdy.clicked.connect(self.on_RequestSetDyDm)

		# Панель Данные
		self.btn_accounts.clicked.connect(self.on_RequestOpenFormAccounts)
		self.btn_operations.clicked.connect(self.on_RequestOpenFormOperations)

		# Панель Отчётность
		self.btn_report_dm.clicked.connect(self.on_RequestGenerateReportDm)
		self.btn_report_summary.clicked.connect(self.on_RequestSummaryReport)

		# Панель Аналитика
		self.btn_analytics.clicked.connect(self.on_RequestOpenFormAnalytics)

		# Панель Утилиты
		self.btn_archives.clicked.connect(self.on_RequestOpenFormArchives)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		super().on_Open()

		self.AdjustBtnDyDm_Text()

		self.ShowTitle()

	def on_Close(self):
		self.application.Close()

	# Переход в другие формы
	def on_RequestOpenFormArchives(self):
		""" Запрос на открытие формы Архив данных """
		self.application.form_archives.Open()

	def on_RequestOpenFormAccounts(self):
		""" Запрос на открытие формы Счета """
		self.application.form_accounts.Open()

	def on_RequestOpenFormOperations(self):
		""" Запрос на открытие формы Финансовые операции """
		self.application.form_operations.Open()

	def on_RequestOpenFormAnalytics(self):
		""" Запрос на открытие формы Аналитика """
		self.application.form_analytics.Open()

	# Панель рабочего периода
	def on_RequestShiftDmToNext(self):
		""" Запрос на смещение рабочего периода в следующий месяц """
		self.workspace.ShiftDmToNext()

		self.AdjustBtnDyDm_Text()

		self.ShowTitle()

	def on_RequestShiftDmToPrev(self):
		""" Запрос на смещение рабочего периода в предыдущий месяц """
		self.workspace.ShiftDmToPrev()

		self.AdjustBtnDyDm_Text()

		self.ShowTitle()

	def on_RequestSetDyDm(self):
		""" Запрос на установку рабочего периода """
		self.SetDyDm()

		self.AdjustBtnDyDm_Text()

		self.ShowTitle()

	# Панель отчётности
	def on_RequestGenerateReportDm(self):
		""" Запрос генерации отчёта за месяц """
		self.GenerateReportDm()

	def on_RequestSummaryReport(self):
		""" Запрос генерации сводного отчёта """
		self.GenerateReportSummary()

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

		# Панель Утилиты
		self.btn_archives.clicked.connect(self.on_RequestOpenFormArchives)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		super().on_Open()

		self.AdjustBtnDyDm_Text()

	# Переход в другие формы
	def on_RequestOpenFormArchives(self):
		""" Запрос на открытие формы Архив данных """
		self.application.form_archives.Open()

	# Панель рабочего периода
	def on_RequestShiftDmToNext(self):
		""" Запрос на смещение рабочего периода в следующий месяц """
		self.workspace.ShiftDmToNext()

		self.AdjustBtnDyDm_Text()

	def on_RequestShiftDmToPrev(self):
		""" Запрос на смещение рабочего периода в предыдущий месяц """
		self.workspace.ShiftDmToPrev()

		self.AdjustBtnDyDm_Text()

	def on_RequestSetDyDm(self):
		""" Запрос на установку рабочего периода """
		self.SetDyDm()

		self.AdjustBtnDyDm_Text()

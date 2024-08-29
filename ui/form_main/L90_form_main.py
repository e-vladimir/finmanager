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

	# Форма
	def on_Show(self):
		""" Отображение формы """
		self.ShowTitle()

		self.FillCbboxDm()
		self.FillCbboxDy()

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
		self.ReadDmProcessingFromCbboxDm()
		self.ReadDyProcessingFromCbboxDy()

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

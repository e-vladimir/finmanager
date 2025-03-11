# ФОРМА ОСНОВНАЯ: ЛОГИКА УПРАВЛЕНИЯ
# 12 фев 2025

from L80_form_main import C80_FormMain


class C90_FormMain(C80_FormMain):
	""" Форма Основная: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Блок Рабочий период
		self.LabelPrevDmDy.clicked.connect(self.on_RequestSwitchDyDmToPrevDm)
		self.LabelNextDmDy.clicked.connect(self.on_RequestSwitchDyDmToNextDm)

		self.LabelDmDy.clicked.connect(self.on_RequestEditDyDm)
		self.LabelDmDy.wheelMovedUp.connect(self.on_RequestSwitchDyDmToNextDm)
		self.LabelDmDy.wheelMovedDown.connect(self.on_RequestSwitchDyDmToPrevDm)

		# Блок Счета
		self.LabelInitialBalance.clicked.connect(self.on_RequestOpenAccounts)

		# Блок Операции
		self.LabelDelta.clicked.connect(self.on_RequestOpenOperations)

	# Форма
	def on_RequestOpen(self):
		""" Открытие формы """
		self.ShowTitle()
		self.ShowWorkspace()
		self.ShowAccounts()
		self.ShowOperations()
		self.ShowBackup()

	# Рабочий период
	def on_DyDmChanged(self):
		""" Изменился год и месяц """
		self.ShowTitle()
		self.ShowWorkspace()
		self.ShowAccounts()
		self.ShowOperations()
		self.ShowBackup()

	def on_RequestSwitchDyDmToNextDm(self):
		""" Запрос на переключение рабочего периода на следующий месяц """
		self.Workspace.SwitchDyDmToNextDm()

		self.on_DyDmChanged()

	def on_RequestSwitchDyDmToPrevDm(self):
		""" Запрос на переключение рабочего периода на предыдущий месяц """
		self.Workspace.SwitchDyDmToPrevDm()

		self.on_DyDmChanged()

	def on_RequestEditDyDm(self):
		""" Запрос на редактирование рабочего периода """
		self.EditDyDm()

	# Счета
	def on_RequestOpenAccounts(self):
		""" Запрос на открытие формы Счета """
		self.Application.FormAccounts.Open()

	# Операции
	def on_RequestOpenOperations(self):
		""" Запрос на открытие формы Операции """
		self.Application.FormOperations.Open()

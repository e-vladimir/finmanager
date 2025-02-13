# ФОРМА ОСНОВНАЯ: ЛОГИКА УПРАВЛЕНИЯ
# 12 фев 2025

from L80_form_main import C80_FormMain


class C90_FormMain(C80_FormMain):
	""" Форма Основная: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Панель Рабочий период
		self.label_dm_dy_prev.clicked.connect(self.on_RequestSwitchDyDmToPrevDm)
		self.label_dm_dy_next.clicked.connect(self.on_RequestSwitchDyDmToNextDm)

		self.label_dm_dy.clicked.connect(self.on_RequestSetDyDm)
		self.label_dm_dy.wheelMovedUp.connect(self.on_RequestSwitchDyDmToNextDm)
		self.label_dm_dy.wheelMovedDown.connect(self.on_RequestSwitchDyDmToPrevDm)

	# Форма
	def on_RequestOpen(self):
		""" Открытие формы """
		self.ShowTitle()
		self.ShowWorkspace()
		self.ShowAccounts()
		self.ShowOperations()
		self.ShowBackup()

	# Рабочий период
	def on_RequestSwitchDyDmToNextDm(self):
		""" Запрос на переключение рабочего периода на следующий месяц """
		self.Workspace.SwitchDyDmToNextDm()

		self.ShowWorkspace()

	def on_RequestSwitchDyDmToPrevDm(self):
		""" Запрос на переключение рабочего периода на предыдущий месяц """
		self.Workspace.SwitchDyDmToPrevDm()

		self.ShowWorkspace()

	def on_RequestSetDyDm(self):
		""" Запрос на редактирование рабочего периода """
		self.SetDyDm()

		self.ShowWorkspace()

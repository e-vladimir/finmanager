# ФОРМА СЧЕТА: ЛОГИКА УПРАВЛЕНИЯ
# 14 фев 2025

from L80_form_accounts import C80_FormAccounts


class C90_FormAccounts(C80_FormAccounts):
	""" Форма Счета: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных: Счета
		self.TreeData.customContextMenuRequested.connect(self.on_RequestShowMenuAccounts)
		self.TreeData.doubleClicked.connect(self.on_TreeData_DbClicked)

		# Меню Счета
		self.ActionCreateAccount.triggered.connect(self.on_RequestCreateAccount)

		# Меню Счёт
		self.ActionSetNameAccount.triggered.connect(self.on_RequestSetNameAccount)
		self.ActionDeleteAccount.triggered.connect(self.on_RequestDeleteAccount)

		self.ActionSetInitialBalance.triggered.connect(self.on_RequestSetInitialBalance)

	# Форма
	def on_Opened(self):
		""" Форма открыта """
		self.ShowTitle()

		self.InitModelData()

		self.LoadGroups()
		self.LoadAccounts()

		self.AdjustTreeData_Color()
		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Sort()

	# Меню Счета
	def on_RequestShowMenuAccounts(self):
		""" Запрос отображения меню Счета """
		self.ReadProcessingIdoFromTreeData()
		self.ReadProcessingGroupFromTreeData()

		self.AdjustMenuAccounts()
		self.AdjustMenuAccounts_Enable()
		self.AdjustMenuAccounts_Text()

		self.ShowMenuAccounts()

	# Счёта
	def on_RequestCreateAccount(self):
		""" Запрос на создание счёта """
		self.CreateAccount()

	def on_RequestSetNameAccount(self):
		""" Запрос редактирования названия счёта """
		self.SetNameAccount()

	def on_RequestDeleteAccount(self):
		""" Запрос на удаление счёта """
		self.DeleteAccount()

	def on_RequestSetInitialBalance(self):
		""" Запрос на установку баланса начального """
		self.SetInitialBalance()

	def on_AccountCreated(self):
		""" Счёт создан """
		self.LoadGroups()
		self.LoadAccountInModelData()

		self.AdjustTreeData_Color()
		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Sort()

	def on_AccountChanged(self):
		""" Счёт изменился """
		self.LoadAccountInModelData()
		self.AdjustTreeData_Sort()

	def on_AccountDeleted(self):
		""" Удалён счёт """
		self.InitModelData()

		self.LoadGroups()
		self.LoadAccounts()

		self.AdjustTreeData_Color()
		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Sort()

	# Дерево данных
	def on_TreeData_DbClicked(self):
		""" По дереву данных выполнен двойной клик """
		self.ReadProcessingIdoFromTreeData()
		self.ReadProcessingIdpFromTreeData()
		self.ReadProcessingGroupFromTreeData()

		self.ControlProcessingIdp()

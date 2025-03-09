# ФОРМА СЧЕТА: ЛОГИКА УПРАВЛЕНИЯ
# 14 фев 2025

from L80_form_accounts import C80_FormAccounts


class C90_FormAccounts(C80_FormAccounts):
	""" Форма Счета: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных: Счета
		self.TreeData.customContextMenuRequested.connect(self.on_RequestShowMenuAccounts)
		self.TreeData.doubleClicked.connect(self.on_TreeDataDbClicked)

		# Меню Счета
		self.ActionCreateAccount.triggered.connect(self.on_RequestCreateAccount)

		# Меню Счёт
		self.ActionDeleteAccount.triggered.connect(self.on_RequestDeleteAccount)

		self.ActionEditAccountName.triggered.connect(self.on_RequestEditAccountName)
		self.ActionEditAccountInitialBalance.triggered.connect(self.on_RequestEditAccountInitialBalance)
		self.ActionEditAccountGroup.triggered.connect(self.on_RequestEditAccountGroup)

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

	# Структура счетов
	def on_AccountsChanged(self):
		""" Структура счетов изменилась """
		self.InitModelData()

		self.LoadGroups()
		self.LoadAccounts()

		self.AdjustTreeData_Color()
		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Sort()

	# Счёта
	def on_RequestCreateAccount(self):
		""" Запрос на создание счёта """
		self.CreateAccount()

	def on_RequestDeleteAccount(self):
		""" Запрос на удаление счёта """
		self.DeleteAccount()

	def on_RequestEditAccountName(self):
		""" Запрос редактирования названия счёта """
		self.EditAccountName()

	def on_RequestEditAccountInitialBalance(self):
		""" Запрос на установку баланса начального """
		self.EditAccountInitialBalance()

	def on_RequestEditAccountGroup(self):
		""" Запрос на редактирование группы счетов для счёта """
		self.EditAccountGroup()

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
	def on_TreeDataDbClicked(self):
		""" По дереву данных выполнен двойной клик """
		self.ReadProcessingIdoFromTreeData()
		self.ReadProcessingIdpFromTreeData()
		self.ReadProcessingGroupFromTreeData()

		self.ControlProcessingIdp()

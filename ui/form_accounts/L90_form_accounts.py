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
		self.ActionTransferAccountsToPrevDm.triggered.connect(self.on_RequestTransferAccountsToPrevDm)
		self.ActionTransferAccountsToNextDm.triggered.connect(self.on_RequestTransferAccountsToNextDm)
		self.ActionResetAccounts.triggered.connect(self.on_RequestResetAccounts)
		self.ActionGenerateReportBalances.triggered.connect(self.on_RequestGenerateReportBalances)

		# Меню Группа счетов
		self.ActionEditGroupName.triggered.connect(self.on_RequestEditGroupName)
		self.ActionTransferGroupToPrevDm.triggered.connect(self.on_RequestTransferGroupToPrevDm)
		self.ActionTransferGroupToNextDm.triggered.connect(self.on_RequestTransferGroupToNextDm)

		# Меню Счёт
		self.ActionDeleteAccount.triggered.connect(self.on_RequestDeleteAccount)
		self.ActionEditAccountName.triggered.connect(self.on_RequestEditAccountName)
		self.ActionEditAccountInitialBalance.triggered.connect(self.on_RequestEditAccountInitialBalance)
		self.ActionEditAccountGroup.triggered.connect(self.on_RequestEditAccountGroup)
		self.ActionTransferAccountToPrevDm.triggered.connect(self.on_RequestTransferAccountToPrevDm)
		self.ActionTransferAccountToNextDm.triggered.connect(self.on_RequestTransferAccountToNextDm)
		self.ActionSwitchAccountPriority.triggered.connect(self.on_RequestSwitchAccountPriority)

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

	def on_RequestUpdateData(self):
		""" Запрос на обновление данных """
		if not self.isVisible(): return

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

	# Счета
	def on_RequestResetAccounts(self):
		""" Запрос на сброс данных """
		self.ResetAccounts()

	def on_RequestTransferAccountsToPrevDm(self):
		""" Запрос переноса всех счетов в предыдущий месяц """
		self.TransferAccountsToPrevDm()

	def on_RequestTransferAccountsToNextDm(self):
		""" Запрос переноса всех счетов в следующий месяц """
		self.TransferAccountsToNextDm()

	def on_RequestGenerateReportBalances(self):
		""" Запрос генерации отчёта по остаткам """
		self.GenerateReportBalances()

	def on_AccountsChanged(self):
		""" Структура счетов изменилась """
		self.InitModelData()

		self.LoadGroups()
		self.LoadAccounts()

		self.AdjustTreeData_Color()
		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Sort()

	# Группа счетов
	def on_RequestEditGroupName(self):
		""" Запрос на редактиование названия группы счетов """
		self.EditGroupName()

	def on_RequestTransferGroupToPrevDm(self):
		""" Запрос на перенос группы счетов в предыдущий месяц """
		self.TransferGroupToPrevDm()

	def on_RequestTransferGroupToNextDm(self):
		""" Запрос на перенос группы счетов в следующий месяц """
		self.TransferGroupToNextDm()

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

	def on_RequestTransferAccountToNextDm(self):
		""" Запрос на перенос счёта в следующий месяц """
		self.TransferAccountToNextDm()

	def on_RequestTransferAccountToPrevDm(self):
		""" Запрос на перенос счёта в предыдущий месяц """
		self.TransferAccountToPrevDm()

	def on_RequestSwitchAccountPriority(self):
		""" Запрос на смену приоритетности счёта """
		self.SwitchAccountPriority()

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

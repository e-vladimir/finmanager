# ФОРМА СЧЕТА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_accounts import C80_FormAccounts


class C90_FormAccounts(C80_FormAccounts):
	""" Форма Счета: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных
		self.tree_data.customContextMenuRequested.connect(self.on_RequestShowMenuAccounts)

		# Структура счетов
		self.menu_accounts_struct_create_account.triggered.connect(self.on_RequestCreateAccount)
		self.menu_accounts_struct_reset.triggered.connect(self.on_RequestResetData)

		# Группа счетов
		self.menu_account_group_rename.triggered.connect(self.on_RequestRenameAccountsGroup)

		# Счёт
		self.menu_account_rename.triggered.connect(self.on_RequestRenameAccount)
		self.menu_account_delete.triggered.connect(self.on_RequestDeleteAccount)
		self.menu_account_change_group.triggered.connect(self.on_RequestChangeGroupForAccount)
		self.menu_account_transfer_next_dm.triggered.connect(self.on_RequestTransferAccountToNextDm)

	# Форма
	def on_Open(self):
		super().on_Open()

		self.ShowTitle()

		self.InitModelData()
		self.ShowAccounts()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Sort()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

	# Меню Счета
	def on_RequestShowMenuAccounts(self):
		""" Запрос меню Счета """
		self.ReadProcessingIdoFromTreeData()
		self.ReadProcessingGroupFromTreeData()
		self.ReadProcessingNameFromTreeData()

		self.AdjustMenuAccounts_Enable()
		self.AdjustMenuAccounts_Text()

		self.ShowMenuAccounts()

	# Меню Счета: Структура счетов
	def on_RequestCreateAccount(self):
		""" Запрос создания счёта в структуре счетов """
		self.CreateAccount()

		self.ReadProcessingGroupFromAccount()

		self.LoadAccountsGroup()
		self.LoadAccount()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Sort()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

	def on_RequestResetData(self):
		""" Запрос сброса данных """
		self.ResetData()

		self.InitModelData()
		self.ShowAccounts()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Sort()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

	# Меню Счета: Группа счетов
	def on_RequestRenameAccountsGroup(self):
		""" Запрос на переименование группы счетов """
		self.RenameAccountsGroup()

		self.InitModelData()
		self.ShowAccounts()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Sort()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

	# Меню Счета: Счёт
	def on_RequestRenameAccount(self):
		""" Запрос на переименование счёта """
		self.RenameAccount()

		self.ReadProcessingGroupFromAccount()

		self.LoadAccountsGroup()
		self.LoadAccount()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Sort()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

	def on_RequestDeleteAccount(self):
		""" Запрос удаления счёта """
		self.DeleteAccount()

		self.InitModelData()
		self.ShowAccounts()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Sort()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

	def on_RequestChangeGroupForAccount(self):
		""" Запрос на перемещение счёта в другую группу """
		self.ChangeGroupForAccount()

		self.InitModelData()
		self.ShowAccounts()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Sort()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

	def on_RequestTransferAccountToNextDm(self):
		""" Запрос на перенос счёта в следующий месяц """
		self.TransferAccountToNextDm()

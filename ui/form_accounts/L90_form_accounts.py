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

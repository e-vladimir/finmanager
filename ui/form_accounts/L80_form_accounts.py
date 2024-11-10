# ФОРМА СЧЕТА: ЛОГИКА ДАННЫХ

from L00_containers    import CONTAINERS
from L20_PySide6       import RequestText, RequestConfirm, RequestValue
from L70_form_accounts import C70_FormAccounts
from L90_accounts      import C90_Account


class C80_FormAccounts(C70_FormAccounts):
	""" Форма Счета: Логика данных """

	# Счета
	def ShowAccounts(self):
		""" Отображение счетов """
		dy, dm = self.workspace.DyDm()

		for self._processing_group in self.accounts_struct.GroupsNamesInDyDm(dy, dm) : self.LoadAccountsGroup()
		for self._processing_ido   in self.accounts_struct.AccountsIdosInDyDm(dy, dm): self.LoadAccount()

	# Структура счётов
	def CreateAccount(self):
		""" Создание счёта в структуре счетов """
		dy, dm                    = self.workspace.DyDm()
		groups_names : list[str]  = self.accounts_struct.GroupsNamesInDyDm(dy, dm)
		group_name   : str | None = self._processing_group
		group_name                = RequestText("Создание счёта", "Группа счетов", group_name, groups_names)
		if group_name   is None: return

		account_name : str | None = RequestText("Создание счёта", f"Наименование счёта в группе {group_name}", "")
		if account_name is None: return

		self._processing_ido = self.accounts_struct.CreateAccountInDyDm(dy, dm, group_name, account_name)

	def TransferAccountsStructToNextDm(self):
		""" Перенос структуры счётов в следующий месяц """
		dy, dm = self.workspace.DyDm()

		self.accounts_struct.TransferToNextDm(dy, dm)

	def TransferAccountsStructToPrevDm(self):
		""" Перенос структуры счётов в прошлый месяц """
		dy, dm = self.workspace.DyDm()

		self.accounts_struct.TransferToPrevDm(dy, dm)

	def ResetData(self):
		""" Сброс данных """
		if not RequestConfirm("Сброс данных", f"Сброс данных за {self.workspace.DmDyToString()}"): return

		account = C90_Account()
		dy, dm  = self.workspace.DyDm()

		for ido in self.accounts_struct.AccountsIdosInDyDm(dy, dm):
			account.Ido(ido)
			account.DeleteObject(CONTAINERS.DISK)

	# Группа счетов
	def RenameAccountsGroup(self):
		""" Смена наименования группы счетов """
		self.accounts_group.ProcessingGroup(self._processing_group)

		dy, dm                    = self.workspace.DyDm()

		groups_names : list[str]  = self.accounts_struct.GroupsNamesInDyDm(dy, dm)
		group_name   : str | None = self._processing_group
		group_name   : str | None = RequestText("Переименовывание группы счетов", group_name, group_name, groups_names)
		if group_name is None: return

		self.accounts_group.Rename(dy, dm, group_name)

	def TransferAccountsGroupToNextDm(self):
		""" Перенос группы счётов в следующий месяц """
		dy, dm = self.workspace.DyDm()

		self.accounts_group.ProcessingGroup(self._processing_group)
		self.accounts_group.TransferToNextDm(dy, dm)

	def TransferAccountsGroupToPrevDm(self):
		""" Перенос группы счётов в прошлый месяц """
		dy, dm = self.workspace.DyDm()

		self.accounts_group.ProcessingGroup(self._processing_group)
		self.accounts_group.TransferToPrevDm(dy, dm)

	# Счёт
	def SetBalanceInitial(self):
		""" Установка остатка начального """
		account = C90_Account(self._processing_ido)

		balance : int | None = RequestValue(account.Name(), f"Остаток начальный на {self.workspace.DmDyToString()}", account.BalanceInitial(), -9999999, 9999999)
		if balance is None: return

		account.BalanceInitial(balance)

	def RenameAccount(self):
		""" Переименование счёта """
		account_name : str | None = RequestText("Переименование счёта", f"{self._processing_group}\n{self._processing_name}", self._processing_name)
		if account_name is None: return

		dy, dm                    = self.workspace.DyDm()

		self.accounts_struct.RenameAccountInDyDm(dy, dm, self._processing_name, account_name)

	def DeleteAccount(self):
		""" Удаление счёта """
		if not RequestConfirm("Удаление счёта", f"{self._processing_group}\n{self._processing_name}"): return

		account = C90_Account(self._processing_ido)
		account.DeleteObject(CONTAINERS.DISK)

	def ChangeGroupForAccount(self):
		""" Перемещение счёта в другую группу """
		dy, dm                    = self.workspace.DyDm()
		groups_names : list[str]  = self.accounts_struct.GroupsNamesInDyDm(dy, dm)
		group_name   : str | None = self._processing_group
		group_name                = RequestText("Перемещение счёта", f"{self._processing_name}", group_name, groups_names)
		if group_name   is None: return

		account                   = C90_Account(self._processing_ido)
		account.ChangeGroup(group_name)

	def TransferAccountToNextDm(self):
		""" Перенос счёта в следующий месяц """
		account = C90_Account(self._processing_ido)
		account.TransferToNextDm()

	def TransferAccountToPrevDm(self):
		""" Перенос счёта в прошлый месяц """
		account = C90_Account(self._processing_ido)
		account.TransferToPrevDm()

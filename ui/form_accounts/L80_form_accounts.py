# ФОРМА СЧЕТА: ЛОГИКА ДАННЫХ

from L00_containers    import CONTAINERS
from L20_PySide6       import RequestText, RequestConfirm
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

	# Счёт
	def CreateAccount(self):
		""" Создание счёта в структуре счетов """
		dy, dm                    = self.workspace.DyDm()
		groups_names : list[str]  = self.accounts_struct.GroupsNamesInDyDm(dy, dm)
		group_name   : str | None = self._processing_group
		group_name                = RequestText("Создание счёта", "Группа счетов", group_name, groups_names)
		if group_name   is None: return

		account_name : str | None = RequestText("Создание счёта", f"Наименование счёта в группе {group_name}", "")
		if account_name is None: return

		self._processing_ido = self.accounts_struct.CreateAccount(dy, dm, group_name, account_name)

	def RenameAccount(self):
		""" Переименование счёта """
		account_name : str | None = RequestText("Переименование счёта", f"{self._processing_group}\n{self._processing_name}", self._processing_name)
		if account_name is None: return

		dy, dm                    = self.workspace.DyDm()

		self.accounts_struct.RenameAccount(dy, dm, self._processing_name, account_name)

	def DeleteAccount(self):
		""" Удаление счёта """
		if not RequestConfirm("Удаление счёта", f"{self._processing_group}\n{self._processing_name}"): return

		account = C90_Account(self._processing_ido)
		account.DeleteObject(CONTAINERS.DISK)

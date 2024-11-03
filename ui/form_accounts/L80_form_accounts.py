# ФОРМА СЧЕТА: ЛОГИКА ДАННЫХ

from L20_PySide6       import RequestText
from L70_form_accounts import C70_FormAccounts


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
		self._processing_name     = ""
		self._processing_ido      = ""
		self._processing_group    = ""

		dy, dm                    = self.workspace.DyDm()
		groups_names : list[str]  = self.accounts_struct.GroupsNamesInDyDm(dy, dm)
		group_name   : str | None = self._processing_group
		group_name                = RequestText("Создание счёта", "Группа счетов", group_name, groups_names)
		if group_name   is None: return

		account_name : str | None = RequestText("Создание счёта", "Наименование счёта", "")
		if account_name is None: return

		self._processing_ido = self.accounts_struct.CreateAccount(dy, dm, group_name, account_name)

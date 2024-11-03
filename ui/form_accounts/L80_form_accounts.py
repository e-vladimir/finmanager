# ФОРМА СЧЕТА: ЛОГИКА ДАННЫХ

from L70_form_accounts import C70_FormAccounts


class C80_FormAccounts(C70_FormAccounts):
	""" Форма Счета: Логика данных """

	# Счета
	def ShowAccounts(self):
		""" Отображение счетов """
		dy, dm = self.workspace.DyDm()

		for self._processing_name in self.accounts_struct.GroupsNamesInDyDm(dy, dm): self.LoadAccountsGroup()
		for self._processing_ido  in self.accounts_struct.AccountsIdosInDyDm(dy, dm): self.LoadAccount()

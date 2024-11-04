# ФОРМА СЧЕТА: МОДЕЛЬ СОБЫТИЙ

from L42_form_accounts import C42_FormAccounts


class C50_FormAccounts(C42_FormAccounts):
	""" Форма Счета: Модель событий """

	# Меню Счета
	def on_RequestShowMenuAccounts(self): pass

	# Структура счетов
	def on_RequestCreateAccount(self): pass
	def on_RequestTransferAccountsStructToNextDm(self): pass
	def on_RequestTransferAccountsStructToPrevDm(self): pass
	def on_RequestResetData(self): pass

	# Группа счетов
	def on_RequestRenameAccountsGroup(self): pass
	def on_RequestTransferAccountsGroupToNextDm(self): pass
	def on_RequestTransferAccountsGroupToPrevDm(self): pass

	# Счёт
	def on_RequestRenameAccount(self): pass
	def on_RequestDeleteAccount(self): pass
	def on_RequestChangeGroupForAccount(self): pass
	def on_RequestTransferAccountToNextDm(self): pass
	def on_RequestTransferAccountToPrevDm(self): pass

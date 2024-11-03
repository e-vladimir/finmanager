# ФОРМА СЧЕТА: МОДЕЛЬ СОБЫТИЙ

from L42_form_accounts import C42_FormAccounts


class C50_FormAccounts(C42_FormAccounts):
	""" Форма Счета: Модель событий """

	# Меню Счета
	def on_RequestShowMenuAccounts(self): pass

	# Структура счетов
	def on_RequestCreateAccount(self): pass

	# Счёт
	def on_RequestRenameAccount(self): pass

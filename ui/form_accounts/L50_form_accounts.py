# ФОРМА СЧЕТА: МОДЕЛЬ СОБЫТИЙ
# 14 фев 2025

from L42_form_accounts import C42_FormAccounts


class C50_FormAccounts(C42_FormAccounts):
	""" Форма Счета: Модель событий """

	# Меню Счета
	def on_RequestShowMenuAccounts(self): pass

	# Дерево счетов
	def on_TreeDataDbClicked(self): pass

	# Структура счетов
	def on_AccountsChanged(self): pass

	# Счёт
	def on_RequestCreateAccount(self): pass
	def on_RequestDeleteAccount(self): pass
	def on_RequestEditAccountName(self): pass
	def on_RequestEditAccountGroup(self): pass
	def on_RequestEditAccountInitialBalance(self): pass

	def on_AccountCreated(self): pass
	def on_AccountChanged(self): pass
	def on_AccountDeleted(self): pass

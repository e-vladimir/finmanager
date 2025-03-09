# СЧЁТ: ЛОГИКА УПРАВЛЕНИЯ
# 14 фев 2025

from L80_account import C80_Account, C80_Accounts


class C90_Account(C80_Account):
	""" Счёт: Логика управления """

	def on_ObjectRegistered(self, container_name: str):
		self.dm              = 0
		self.dy              = 0
		self.group           = ""
		self.initial_balance = ""
		self.name            = ""


class C90_Accounts(C80_Accounts):
	""" Контроллер счетов: Логика управления """
	pass

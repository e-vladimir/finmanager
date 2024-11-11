# СЧЕТА: ЛОГИКА УПРАВЛЕНИЯ

from L80_accounts import C80_Accounts, C80_AccountGroup, C80_Account


class C90_Account(C80_Account):
	""" Счёт: Логика управления """

	def on_ObjectRegistered(self, container_name: str):
		""" Объект зарегистрирован в контейнере """
		self.Dy(0)
		self.Dm(0)
		self.Name("")
		self.Group("")
		self.BalanceInitial(0)


class C90_AccountGroup(C80_AccountGroup):
	""" Группа счетов: Логика управления """
	pass


class C90_Accounts(C80_Accounts):
	""" Счета: Логика управления """
	pass

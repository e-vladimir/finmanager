# ФОРМА СЧЕТА: ЛОГИКА ДАННЫХ
# 14 фев 2025

from L00_containers    import CONTAINERS
from L20_PySide6 import RequestConfirm, RequestText, RequestValue
from L70_form_accounts import C70_FormAccounts
from L90_account       import C90_Account


class C80_FormAccounts(C70_FormAccounts):
	""" Форма Счета: Логика данных """

	# Счета
	def LoadGroups(self):
		""" Загрузка счетов """
		dy, dm = self.Workspace.DyDm()

		for self.processing_group in self.Accounts.Groups(dy, dm): self.LoadGroupInModelData()

	def LoadAccounts(self):
		""" Загрузка счетов """
		dy, dm = self.Workspace.DyDm()

		for self.processing_ido   in self.Accounts.Idos(dy, dm)  : self.LoadAccountInModelData()

	# Счёт
	def CreateAccount(self):
		""" Создание счёта """
		dy, dm             = self.Workspace.DyDm()
		group : str | None = RequestText("Создание счёта", "Группа счетов:", self.processing_group, self.Accounts.Groups(dy, dm))
		if not group              : return

		name  : str | None = RequestText("Создание счёта", f"Группа счетов: {group}\n\nНазвание счёта:", "", self.Accounts.Names(group=group))
		if not name               : return

		self.processing_ido = self.Accounts.CreateAccount(dy, dm, group, name)
		if not self.processing_ido: return

		self.on_AccountCreated()

	def SetNameAccount(self):
		""" Редактирование названия счёта """
		account           = C90_Account(self.processing_ido)

		name : str | None = RequestText("Редактирование счёта", "Наименование счёта:", account.name)
		if not name: return

		account.name = name

		self.on_AccountChanged()

	def DeleteAccount(self):
		""" Удаление счёта """
		account = C90_Account(self.processing_ido)

		if not RequestConfirm("Удаление счёта", f"{account.group}\n{account.name}"): return

		account.DeleteObject(CONTAINERS.DISK)

		self.on_AccountDeleted()

	def SetInitialBalance(self):
		""" Установка баланса начального """
		account              = C90_Account(self.processing_ido)

		balance : int | None = RequestValue("Остаток на начало месяца", f"{account.group}\n{account.name}", account.initial_balance, -99999999, 99999999)
		if not balance: return

		account.initial_balance = balance

		self.on_AccountChanged()

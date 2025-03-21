# ФОРМА СЧЕТА: ЛОГИКА ДАННЫХ
# 14 фев 2025

from pathlib           import Path

from L00_containers    import CONTAINERS
from L20_PySide6       import RequestConfirm, RequestText, RequestValue, ShowMessage
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

	def ResetAccounts(self):
		""" Сброс данных """
		if not RequestConfirm("Сброс данных", f"Сброс счетов на {self.Workspace.DmDyToString()}"): return

		dy, dm = self.Workspace.DyDm()
		for ido in self.Accounts.Idos(dy, dm): C90_Account(ido).DeleteObject(CONTAINERS.DISK)

		self.on_AccountsChanged()

	def TransferAccountsToNextDm(self):
		""" Перенос счётов в следующий месяц """
		dy, dm = self.Workspace.DyDm()

		for ido in self.Accounts.Idos(dy, dm):
			account = C90_Account(ido)
			account.TransferToDm(1)

	def TransferAccountsToPrevDm(self):
		""" Перенос счётов в предыдущий месяц """
		dy, dm = self.Workspace.DyDm()

		for ido in self.Accounts.Idos(dy, dm):
			account = C90_Account(ido)
			account.TransferToDm(-1)

	def GenerateReportBalances(self):
		""" Генерация отчёта по остаткам """
		pdf_file : Path | None = self.Report.GenerateReportBalances()
		if not pdf_file:
			ShowMessage("Отчёт по остаткам",
			            "Генерация отчёта прервана")
			return

		ShowMessage( "Отчёт по остаткам",
		            f"Отчёт сохранён в файл {pdf_file.name}",
		            f"{pdf_file.absolute()}")

	# Группа счетов
	def EditGroupName(self):
		""" Редактирование названия группы счетов """
		dy, dm                = self.Workspace.DyDm()
		name_old : str        = self.processing_group
		name_new : str | None = RequestText("Редактирование группы счетов", "Группа счетов:", name_old, self.Accounts.Groups(dy, dm))
		if not name_new: return

		self.Accounts.EditGroupName(dy, dm, name_old, name_new)

		self.on_AccountsChanged()

	def TransferGroupToNextDm(self):
		""" Перенос счёта в следующий месяц """
		dy, dm = self.Workspace.DyDm()

		for ido in self.Accounts.Idos(dy, dm, self.processing_group):
			account = C90_Account(ido)
			account.TransferToDm(1)

	def TransferGroupToPrevDm(self):
		""" Перенос счёта в предыдущий месяц """
		dy, dm = self.Workspace.DyDm()

		for ido in self.Accounts.Idos(dy, dm, self.processing_group):
			account = C90_Account(ido)
			account.TransferToDm(-1)

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

	def DeleteAccount(self):
		""" Удаление счёта """
		account = C90_Account(self.processing_ido)

		if not RequestConfirm("Удаление счёта", f"{account.group}\n{account.name}"): return

		account.DeleteObject(CONTAINERS.DISK)

		self.on_AccountDeleted()

	def EditAccountName(self):
		""" Редактирование названия счёта """
		account           = C90_Account(self.processing_ido)

		name : str | None = RequestText("Редактирование счёта", "Наименование счёта:", account.name)
		if not name: return

		account.name = name

		self.on_AccountChanged()

	def EditAccountInitialBalance(self):
		""" Установка баланса начального """
		account              = C90_Account(self.processing_ido)

		balance : int | None = RequestValue("Остаток на начало месяца", f"{account.group}\n{account.name}\n\nОстаток на начало месяца:", account.initial_balance, -99999999, 99999999)
		if balance is None: return

		account.initial_balance = balance

		self.on_AccountChanged()

	def EditAccountGroup(self):
		""" Редактирование группы счетов для счёта """
		account            = C90_Account(self.processing_ido)

		dy, dm             = self.Workspace.DyDm()
		group : str | None = RequestText("Редактирование счёта", "Группа счетов:", account.group, self.Accounts.Groups(dy, dm))
		if not group              : return

		account.group = group

		self.on_AccountsChanged()

	def TransferAccountToNextDm(self):
		""" Перенос счёта в следующий месяц """
		account = C90_Account(self.processing_ido)
		account.TransferToDm(1)

	def TransferAccountToPrevDm(self):
		""" Перенос счёта в предыдущий месяц """
		account = C90_Account(self.processing_ido)
		account.TransferToDm(-1)

	def SwitchAccountPriority(self):
		""" Переключение приоритетности счёта """
		account = C90_Account(self.processing_ido)
		account.priority = abs(account.priority - 1)

		self.on_AccountChanged()

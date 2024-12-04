# ФОРМА ФИНАНСОВАЯ ОПЕРАЦИЯ: ЛОГИКА ДАННЫХ

from G11_convertor_data import AmountToString

from L00_months         import MONTHS
from L20_PySide6        import RequestValue, RequestText, RequestMultipleText, RequestItems
from L70_form_operation import C70_FormOperation


class C80_FormOperation(C70_FormOperation):
	""" Форма Финансовая операция: Логика данных """

	# Финансовая операция
	def SetDate(self):
		""" Установка даты """
		caption : str        = f"{AmountToString(self.operation.Amount())} от {self.operation.DdDmDyToString()}"
		text    : str        = f"Дата операции\n\n{caption}\n{self.operation.Description()}"
		date    : str | None = RequestText(caption, text, self.operation.DdDmDyToString())
		if     date is None          : return

		dd_dm_dy = date.split(' ')
		if not len(dd_dm_dy) == 3    : return

		try   :
			dd = int(dd_dm_dy[0])
			dm = MONTHS.FindByNameS(dd_dm_dy[1])
			dy = int(dd_dm_dy[2])
		except: return

		if     dd not in range(1, 31): return

		self.operation.Dd(dd)
		self.operation.Dm(dm.code)
		self.operation.Dy(dy)

	def SetAmount(self):
		""" Установка суммы """
		caption : str        = f"{AmountToString(self.operation.Amount())} от {self.operation.DdDmDyToString()}"
		text    : str        = f"Описание операции:\n{self.operation.Description()}\n\nНазначение операции:\n{self.operation.Destination()}"
		amount  : int | None = RequestValue(caption, text, int(self.operation.Amount()), -99999999, 99999999)
		if amount is None: return

		self.operation.Amount(amount)

	def SetDescription(self):
		""" Установка описания """
		caption     : str        = f"{AmountToString(self.operation.Amount())} от {self.operation.DdDmDyToString()}"
		text        : str        = f"Описание операции:\n{self.operation.Description()}\n\nНазначение операции:\n{self.operation.Destination()}"
		description : str | None = RequestText(caption, text, self.operation.Description())
		if description is None: return

		self.operation.Description(description)

	def SetDestination(self):
		""" Установка назначения """
		caption     : str        = f"{AmountToString(self.operation.Amount())} от {self.operation.DdDmDyToString()}"
		text        : str        = f"Описание операции:\n{self.operation.Description()}\n\nНазначение операции:\n{self.operation.Destination()}"
		destination : str | None = RequestText(caption, text, self.operation.Destination())
		if destination is None: return

		self.operation.Destination(destination)

	def SetAccounts(self):
		""" Установка счетов """
		dy, dm                         = self.workspace.DyDm()
		caption            : str       = f"{AmountToString(self.operation.Amount())} от {self.operation.DdDmDyToString()}"
		text               : str       = f"Описание операции:\n{self.operation.Description()}\n\nНазначение операции:\n{self.operation.Destination()}"
		accounts_checked   : list[str] = self.accounts.IdosToNames(self.operation.AccountsIdos())
		accounts_available : list[str] = self.accounts.AccountsNamesInDyDm(dy, dm)
		accounts           : list[str] | None = RequestItems(caption, text, accounts_available, accounts_checked)
		if accounts is None: return

		self.operation.AccountsIdos(self.accounts.NamesToIdos(dy, dm, accounts))

	def SetLabels(self):
		""" Установка меток """
		caption     : str              = f"{AmountToString(self.operation.Amount())} от {self.operation.DdDmDyToString()}"
		text        : str              = f"Описание операции:\n{self.operation.Description()}\n\nНазначение операции:\n{self.operation.Destination()}"
		labels      : list[str] | None = RequestMultipleText(caption, text, self.operation.Labels())
		if labels is None: return

		self.operation.Labels(labels)

# ФОРМА ФИНАНСОВАЯ ОПЕРАЦИЯ: ЛОГИКА ДАННЫХ

from G11_convertor_data import AmountToString

from L00_months         import MONTHS
from L20_PySide6        import RequestValue, RequestText
from L70_form_operation import C70_FormOperation


class C80_FormOperation(C70_FormOperation):
	""" Форма Финансовая операция: Логика данных """

	# Финансовая операция
	def SetDate(self):
		""" Установка даты """
		caption : str        = f"{AmountToString(self.operation.Amount())} от {self.operation.DdDmDyToString()}"
		date    : str | None = RequestText(caption, "Дата операции", self.operation.DdDmDyToString())
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
		amount  : int | None = RequestValue(caption, "Сумма операции", self.operation.Amount(), -99999999, 99999999)
		if amount is None: return

		self.operation.Amount(amount)

	def SetDescription(self):
		""" Установка описания """
		caption     : str        = f"{AmountToString(self.operation.Amount())} от {self.operation.DdDmDyToString()}"
		description : str | None = RequestText(caption, "Описание операции", self.operation.Description())
		if description is None: return

		self.operation.Description(description)

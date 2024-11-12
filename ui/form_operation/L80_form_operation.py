# ФОРМА ФИНАНСОВАЯ ОПЕРАЦИЯ: ЛОГИКА ДАННЫХ

from G11_convertor_data import AmountToString

from L20_PySide6        import RequestValue, RequestText
from L70_form_operation import C70_FormOperation


class C80_FormOperation(C70_FormOperation):
	""" Форма Финансовая операция: Логика данных """

	# Финансовая операция
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

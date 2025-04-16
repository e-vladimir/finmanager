# ФОРМА ОСНОВНАЯ: МЕХАНИКА ДАННЫХ
# 12 фев 2025

from L20_finmanager_struct import T20_Day
from L50_form_main         import C50_FormMain
from L90_operations        import C90_Operation


class C60_FormMain(C50_FormMain):
	""" Форма Основная: Механика данных """

	@property
	def amounts(self) -> dict[int, T20_Day]:
		return self._amounts

	def LoadAmounts(self):
		""" Сбор сумм """
		self._amounts.clear()

		dy, dm                   = self.Workspace.DyDm()
		operation                = C90_Operation()

		for operation_ido in self.Operations.Idos(dy, dm, include_skip=False):
			operation.Ido(operation_ido)

			amount = operation.amount

			if amount > 0: self._amounts[operation.dd].amount_income  += amount
			else         : self._amounts[operation.dd].amount_outcome += amount

	def SendAmountsToDiaDmView(self):
		""" Отправка данных в виджет обзор месяца """
		self.DiaDmViewer._days = self._amounts

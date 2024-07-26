# ФИНСТАТИСТИКА: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL

from L70_finstatistic       import C70_Finstatistic


class C80_Finstatistic(C70_Finstatistic):
	""" Финстатистика: Логика данных """

	# Расчёты
	def CalcIncomeByFindescription(self, ido: str, dy: int, dm: int) -> int:
		""" Расчёт дохода за финпериод """
		filter_findata = C30_FilterLinear1D(self._idc)
		filter_findata.FilterIdpVlpByEqual(self._idp_dy, dy)
		filter_findata.FilterIdpVlpByEqual(self._idp_dm, dm)
		filter_findata.FilterIdpVlpByInclude(self._idp_findescription, ido)
		filter_findata.FilterIdpVlpByMore(self._idp_amount, 0)

		filter_findata.Capture(CONTAINER_LOCAL)

		return sum(filter_findata.ToIntegers(self._idp_amount, False, False).data)

	def CalcOutcomeByFindescription(self, ido: str, dy: int, dm: int) -> int:
		""" Расчёт расхода за финпериод """
		filter_findata = C30_FilterLinear1D(self._idc)
		filter_findata.FilterIdpVlpByEqual(self._idp_dy, dy)
		filter_findata.FilterIdpVlpByEqual(self._idp_dm, dm)
		filter_findata.FilterIdpVlpByInclude(self._idp_findescription, ido)
		filter_findata.FilterIdpVlpByLess(self._idp_amount, 0)

		filter_findata.Capture(CONTAINER_LOCAL)

		return sum(filter_findata.ToIntegers(self._idp_amount, False, False).data)

	def CalcIncomeByFindescriptions(self, idos: list[str], dy: int, dm: int) -> int:
		""" Расчёт дохода за финпериод """
		filter_findata = C30_FilterLinear1D(self._idc)
		filter_findata.FilterIdpVlpByEqual(self._idp_dy, dy)
		filter_findata.FilterIdpVlpByEqual(self._idp_dm, dm)
		for ido in idos: filter_findata.FilterIdpVlpByInclude(self._idp_findescription, ido)
		filter_findata.FilterIdpVlpByMore(self._idp_amount, 0)

		filter_findata.Capture(CONTAINER_LOCAL)

		return sum(filter_findata.ToIntegers(self._idp_amount, False, False).data)

	def CalcOutcomeByFindescriptions(self, idos: list[str], dy: int, dm: int) -> int:
		""" Расчёт расхода за финпериод """
		filter_findata = C30_FilterLinear1D(self._idc)
		filter_findata.FilterIdpVlpByEqual(self._idp_dy, dy)
		filter_findata.FilterIdpVlpByEqual(self._idp_dm, dm)
		for ido in idos: filter_findata.FilterIdpVlpByInclude(self._idp_findescription, ido)
		filter_findata.FilterIdpVlpByLess(self._idp_amount, 0)

		filter_findata.Capture(CONTAINER_LOCAL)

		return sum(filter_findata.ToIntegers(self._idp_amount, False, False).data)

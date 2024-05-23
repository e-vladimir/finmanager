# ФИНСТАТИСТИКА: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL

from L70_finstatistic       import C70_Finstatistic


class C80_Finstatistic(C70_Finstatistic):
	""" Финстатистика: Логика данных """

	# Расчёты
	def CalcIncomeByFindescription(self, oid: str, dy: int, dm: int) -> int:
		""" Расчёт дохода за финпериод """
		filter_findata = C30_FilterLinear1D(self._oci)
		filter_findata.FilterPidCvlByEqual(self._pid_dy, dy)
		filter_findata.FilterPidCvlByEqual(self._pid_dm, dm)
		filter_findata.FilterPidCvlByInclude(self._pid_findescription, oid)
		filter_findata.FilterPidCvlByMore(self._pid_amount, 0)

		filter_findata.Capture(CONTAINER_LOCAL)

		return sum(filter_findata.ToIntegers(self._pid_amount, False, False).items)

	def CalcOutcomeByFindescription(self, oid: str, dy: int, dm: int) -> int:
		""" Расчёт расхода за финпериод """
		filter_findata = C30_FilterLinear1D(self._oci)
		filter_findata.FilterPidCvlByEqual(self._pid_dy, dy)
		filter_findata.FilterPidCvlByEqual(self._pid_dm, dm)
		filter_findata.FilterPidCvlByInclude(self._pid_findescription, oid)
		filter_findata.FilterPidCvlByLess(self._pid_amount, 0)

		filter_findata.Capture(CONTAINER_LOCAL)

		return sum(filter_findata.ToIntegers(self._pid_amount, False, False).items)

	def CalcIncomeByFindescriptions(self, oids: list[str], dy: int, dm: int) -> int:
		""" Расчёт дохода за финпериод """
		filter_findata = C30_FilterLinear1D(self._oci)
		filter_findata.FilterPidCvlByEqual(self._pid_dy, dy)
		filter_findata.FilterPidCvlByEqual(self._pid_dm, dm)
		for oid in oids: filter_findata.FilterPidCvlByInclude(self._pid_findescription, oid)
		filter_findata.FilterPidCvlByMore(self._pid_amount, 0)

		filter_findata.Capture(CONTAINER_LOCAL)

		return sum(filter_findata.ToIntegers(self._pid_amount, False, False).items)

	def CalcOutcomeByFindescriptions(self, oids: list[str], dy: int, dm: int) -> int:
		""" Расчёт расхода за финпериод """
		filter_findata = C30_FilterLinear1D(self._oci)
		filter_findata.FilterPidCvlByEqual(self._pid_dy, dy)
		filter_findata.FilterPidCvlByEqual(self._pid_dm, dm)
		for oid in oids: filter_findata.FilterPidCvlByInclude(self._pid_findescription, oid)
		filter_findata.FilterPidCvlByLess(self._pid_amount, 0)

		filter_findata.Capture(CONTAINER_LOCAL)

		return sum(filter_findata.ToIntegers(self._pid_amount, False, False).items)

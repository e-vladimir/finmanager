# ФИНАНСОВЫЕ ОПЕРАЦИИ: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L70_operations         import C70_Operation, C70_Operations


class C80_Operation(C70_Operation):
	""" Финансовая операция: Логика данных """
	pass


class C80_Operations(C70_Operations):
	""" Финансовые операции: Логика данных """

	# Дни
	def DdsInDyDm(self, dy: int, dm: int) -> list[int]:
		""" Список дней """
		account_operation = C80_Operation()
		idc    : str      = account_operation.Idc().data
		idp_dy : str      = account_operation.f_dy.Idp().data
		idp_dm : str      = account_operation.f_dm.Idp().data
		idp_dd : str      = account_operation.f_dd.Idp().data

		filter_data = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.ToIntegers(idp_dd, True, True).data

	# Финансовые операции
	def OperationsIdosInDyDmDd(self, dy: int, dm: int, dd: int = None) -> list[str]:
		""" Список IDO операций по счетам в указанном периоде """
		account_operation = C80_Operation()
		idc        : str  = account_operation.Idc().data
		idp_dy     : str  = account_operation.f_dy.Idp().data
		idp_dm     : str  = account_operation.f_dm.Idp().data
		idp_dd     : str  = account_operation.f_dd.Idp().data
		idp_amount : str  = account_operation.f_amount.Idp().data

		filter_data       = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		if dd is not None: filter_data.FilterIdpVlpByEqual(idp_dd, dd)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.Idos(idp_amount).data

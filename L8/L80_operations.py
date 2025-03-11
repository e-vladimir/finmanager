# ФИНАНСОВЫЕ ОПЕРАЦИИ: ЛОГИКА ДАННЫХ
# 11 мар 2025

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L70_operations         import C70_Operation, C70_Operations


class C80_Operation(C70_Operation):
	""" Финансовая операция: Логика данных """
	pass


class C80_Operations(C70_Operations):
	""" Финансовые операции: Логика данных """

	# Выборки данных
	def Idos(self, dy: int, dm: int, dd: int = None, account_ido: str = None) -> list[str]:
		""" Список IDO финансовых операций """
		operation         = C80_Operation()
		idc         : str = operation.Idc().data
		idp_dy      : str = operation.FDy.Idp().data
		idp_dm      : str = operation.FDm.Idp().data
		idp_dd      : str = operation.FDd.Idp().data
		idp_amount  : str = operation.FAmount.Idp().data
		idp_account : str = operation.FAccountIdos.Idp().data

		filter_data       = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.FilterIdpVlpByEqual(idp_dd, dd)
		filter_data.FilterIdpVlpByInclude(idp_account, account_ido)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.Idos(idp_amount).data

	def Amounts(self, dy: int, dm: int, dd: int = None, account_ido: str = None) -> list[float]:
		""" Список сумм финансовых операций """
		operation         = C80_Operation()
		idc         : str = operation.Idc().data
		idp_dy      : str = operation.FDy.Idp().data
		idp_dm      : str = operation.FDm.Idp().data
		idp_dd      : str = operation.FDd.Idp().data
		idp_amount  : str = operation.FAmount.Idp().data
		idp_account : str = operation.FAccountIdos.Idp().data

		filter_data       = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.FilterIdpVlpByEqual(idp_dd, dd)
		filter_data.FilterIdpVlpByInclude(idp_account, account_ido)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.ToFloats(idp_amount).data

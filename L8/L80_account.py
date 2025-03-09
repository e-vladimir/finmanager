# СЧЁТ: ЛОГИКА ДАННЫХ
# 14 фев 2025

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L70_account            import C70_Account, C70_Accounts


class C80_Account(C70_Account):
	""" Счёт: Логика данных """
	pass


class C80_Accounts(C70_Accounts):
	""" Контроллер счетов: Логика данных """

	# Выборка данных
	def Idos(self, dy: int = None, dm: int = None) -> list[str]:
		""" Список IDO счетов в указанном месяце """
		account        = C80_Account()
		idc      : str = account.Idc().data
		idp_dy   : str = account.FDy.Idp().data
		idp_dm   : str = account.FDm.Idp().data
		idp_name : str = account.FName.Idp().data

		filter_data    = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.Idos(idp_name).data

	def Names(self, dy: int = None, dm: int = None, group: str = None) -> list[str]:
		""" Названия счетов в указанном месяце """
		account         = C80_Account()
		idc       : str = account.Idc().data
		idp_dy    : str = account.FDy.Idp().data
		idp_dm    : str = account.FDm.Idp().data
		idp_name  : str = account.FName.Idp().data
		idp_group : str = account.FGroup.Idp().data

		filter_data     = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy,    dy)
		filter_data.FilterIdpVlpByEqual(idp_dm,    dm)
		filter_data.FilterIdpVlpByEqual(idp_group, group)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.ToStrings(idp_name, True, True).data

	def Groups(self, dy: int = None, dm: int = None) -> list[str]:
		""" Названия групп счетов в указанном месяце """
		account         = C80_Account()
		idc       : str = account.Idc().data
		idp_dy    : str = account.FDy.Idp().data
		idp_dm    : str = account.FDm.Idp().data
		idp_group : str = account.FGroup.Idp().data

		filter_data     = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.ToStrings(idp_group, True, True).data

	# Управление счетами
	def CreateAccount(self, dy: int, dm: int, group: str, name: str) -> str:
		""" Создание счёта """
		if not name                      : return ""
		if     name in self.Names(dy, dm): return ""

		account       = C80_Account()
		account.GenerateIdo()
		account.RegisterObject(CONTAINERS.DISK)

		account.dm    = dm
		account.dy    = dy
		account.name  = name
		account.group = group

		return account.Ido().data

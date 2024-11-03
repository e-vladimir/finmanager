# СЧЕТА: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L70_accounts           import C70_AccountsStruct, C70_AccountsGroup, C70_Account


class C80_Account(C70_Account):
	""" Счёт: Логика данных """
	pass


class C80_AccountsGroup(C70_AccountsGroup):
	""" Группа счетов: Логика данных """
	pass


class C80_AccountsStruct(C70_AccountsStruct):
	""" Структура счетов: Логика данных """

	# Структура счетов
	def AccountsIdosInDyDm(self, dy: int, dm: int) -> list[str]:
		""" Список IDO счетов в указанном периоде """
		account         = C80_Account()

		idc       : str = account.Idc().data
		idp_dy    : str = account.f_dy.Idp().data
		idp_dm    : str = account.f_dm.Idp().data
		idp_name  : str = account.f_name.Idp().data

		filter_accounts = C30_FilterLinear1D(idc)
		filter_accounts.FilterIdpVlpByEqual(idp_dy, dy)
		filter_accounts.FilterIdpVlpByEqual(idp_dm, dm)
		filter_accounts.Capture(CONTAINERS.DISK)

		return filter_accounts.Idos(idp_name).data

	# Группа счетов
	def GroupsNamesInDyDm(self, dy: int, dm: int) -> list[str]:
		""" Список названий групп счетов в указанном периоде """
		account         = C80_Account()

		idc       : str = account.Idc().data
		idp_dy    : str = account.f_dy.Idp().data
		idp_dm    : str = account.f_dm.Idp().data
		idp_group : str = account.f_group.Idp().data

		filter_accounts = C30_FilterLinear1D(idc)
		filter_accounts.FilterIdpVlpByEqual(idp_dy, dy)
		filter_accounts.FilterIdpVlpByEqual(idp_dm, dm)
		filter_accounts.Capture(CONTAINERS.DISK)

		return filter_accounts.ToStrings(idp_group, True, True).data

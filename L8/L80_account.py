# СЧЁТ: ЛОГИКА ДАННЫХ
# 14 фев 2025

from G10_datetime           import CalcDyDmByShiftDm
from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L70_account            import C70_Account, C70_Accounts


class C80_Account(C70_Account):
	""" Счёт: Логика данных """

	# Перенос
	def TransferToDm(self, count_dm: int = 1):
		""" Перенос счёта в следующий месяц """
		if not count_dm: return

		dy, dm                = CalcDyDmByShiftDm(self.dy, self.dm, count_dm)
		name            : str = self.name
		group           : str = self.group
		summary_balance : int = self.summary_balance
		priority        : int = self.priority

		if not self.SwitchByName(dy, dm, name):
			self.GenerateIdo()
			self.RegisterObject(CONTAINERS.DISK)
			self.dy   = dy
			self.dm   = dm
			self.name = name

		self.group    = group
		self.priority = priority

		if count_dm > 0: self.initial_balance = summary_balance


class C80_Accounts(C70_Accounts):
	""" Контроллер счетов: Логика данных """

	# Выборка данных
	@classmethod
	def Idos(self, dy: int = None, dm: int = None, group: str = None) -> list[str]:
		""" Список IDO счетов в указанном месяце """
		account         = C80_Account()
		idc       : str = account.Idc().data
		idp_dy    : str = account.FDy.Idp().data
		idp_dm    : str = account.FDm.Idp().data
		idp_group : str = account.FGroup.Idp().data
		idp_name  : str = account.FName.Idp().data

		filter_data    = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.FilterIdpVlpByEqual(idp_group, group)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.Idos(idp_name).data

	@classmethod
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

	@classmethod
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

	@classmethod
	def AvailableDys(self) -> list[int]:
		""" Список годов с доступными счетами """
		account         = C80_Account()
		idc       : str = account.Idc().data
		idp_dy    : str = account.FDy.Idp().data

		filter_data     = C30_FilterLinear1D(idc)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.ToIntegers(idp_dy, True, True).data

	# Управление счетами
	@classmethod
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

	# Управление группами счетов
	@classmethod
	def EditGroupName(self, dy: int, dm: int, name_old: str, name_new: str):
		""" Редактирование имени группы счетов """
		account         = C80_Account()
		idc       : str = account.Idc().data
		idp_dy    : str = account.FDy.Idp().data
		idp_dm    : str = account.FDm.Idp().data
		idp_group : str = account.FGroup.Idp().data

		filter_data     = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.FilterIdpVlpByEqual(idp_group, name_old)
		filter_data.Capture(CONTAINERS.DISK)

		for ido in filter_data.Idos().data:
			account = C80_Account(ido)
			account.group = name_new

	# Преобразования
	@classmethod
	def IdosToNames(self, idos: list[str]) -> list[str]:
		""" Преобразование IDO в названия счетов """
		return sorted([C80_Account(ido).name for ido in idos])

	@classmethod
	def NamesToIdos(self, dy: int, dm: int, names: list[str]) -> list[str]:
		""" Преобразование названий счетов в список IDO """
		result : list[str] = []

		for name in names:
			account = C80_Account()
			if not account.SwitchByName(dy, dm, name): continue

			result.append(account.Ido().data)

		return result

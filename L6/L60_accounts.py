# СЧЕТА: МЕХАНИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L50_accounts           import C50_AccountsStruct, C50_AccountsGroup, C50_Account


class C60_Account(C50_Account):
	""" Счёт: Механика данных """

	# Параметры
	def Dy(self, year: int = None) -> int:
		""" Год """
		if year is None : return self.f_dy.ToInteger(CONTAINERS.DISK).data
		else            :        self.f_dy.FromInteger(CONTAINERS.DISK, year)

	def Dm(self, month: int = None) -> int:
		""" Месяц """
		if month is None: return self.f_dm.ToInteger(CONTAINERS.DISK).data
		else            :        self.f_dm.FromInteger(CONTAINERS.DISK, month)

	def Name(self, text: str = None) -> str:
		""" Название """
		if text is None : return self.f_name.ToString(CONTAINERS.DISK).data
		else            :        self.f_name.FromString(CONTAINERS.DISK, text)

	def Group(self, text: str = None) -> str:
		""" Группа счетов """
		if text is None : return self.f_group.ToString(CONTAINERS.DISK).data
		else            :        self.f_group.FromString(CONTAINERS.DISK, text)

	# Упаковка данных
	def DyDm(self) -> (int, int):
		""" Год - Месяц """
		return self.Dy(), self.Dm()

	# Переключение
	def SwitchByNameInDyDm(self, dy: int, dm: int, name: str) -> bool:
		""" Переключение по наименованию в указанном периоде """
		idc       : str       = self.Idc().data
		idp_dy    : str       = self.f_dy.Idp().data
		idp_dm    : str       = self.f_dm.Idp().data
		idp_name  : str       = self.f_name.Idp().data

		filter_accounts       = C30_FilterLinear1D(idc)
		filter_accounts.FilterIdpVlpByEqual(idp_dy,   dy)
		filter_accounts.FilterIdpVlpByEqual(idp_dm,   dm)
		filter_accounts.FilterIdpVlpByEqual(idp_name, name)
		filter_accounts.Capture(CONTAINERS.DISK)

		idos      : list[str] = filter_accounts.Idos().data
		if not idos: return False

		self.Ido(idos[0])

		return True


class C60_AccountsGroup(C50_AccountsGroup):
	""" Группа счетов: Механика данных """

	# Параметры
	def ProcessingGroup(self, name: str = None) -> str:
		""" Имя группы """
		if name is None: return self._processing_group
		else           :        self._processing_group = name


class C60_AccountsStruct(C50_AccountsStruct):
	""" Структура счетов: Механика данных """
	pass

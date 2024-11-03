# СЧЕТА: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINERS
from L50_accounts   import C50_AccountStruct, C50_AccountGroup, C50_Account


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


class C60_AccountGroup(C50_AccountGroup):
	""" Группа счетов: Механика данных """
	pass


class C60_AccountStruct(C50_AccountStruct):
	""" Структура счетов: Механика данных """
	pass

# РАБОЧЕЕ ПРОСТРАНСТВО: МЕХАНИКА ДАННЫХ

from G10_datetime   import CalcDyDmByShiftDm

from L00_containers import CONTAINERS
from L50_workspace  import C50_Workspace


class C60_Workspace(C50_Workspace):
	""" Рабочее пространство: Механика данных """

	# Переключение
	def SwitchToMain(self):
		""" Переключение на основное рабочее пространство """
		self.Ido("main_workspace")

	# Параметры
	def Dy(self, year: int = None) -> int:
		""" Год """
		if year is None: return self.f_dy.ToInteger(CONTAINERS.DISK).data
		else           :        self.f_dy.FromInteger(CONTAINERS.DISK, year)

	def Dm(self, month: int = None) -> int:
		""" Месяц """
		if month is None: return self.f_dm.ToInteger(CONTAINERS.DISK).data
		else            :        self.f_dm.FromInteger(CONTAINERS.DISK, month)

	# Смещение рабочего периода
	def ShiftDmToNext(self):
		""" Смещение рабочего периода в следующий месяц """
		dy, dm = CalcDyDmByShiftDm(self.Dy(), self.Dm(), 1)

		self.Dy(dy)
		self.Dm(dm)

	def ShiftDmToPrev(self):
		""" Смещение рабочего периода в предыдущий месяц """
		dy, dm = CalcDyDmByShiftDm(self.Dy(), self.Dm(), -1)

		self.Dy(dy)
		self.Dm(dm)

	def DyDm(self, year: int = None, month: int = None) -> [int, int]:
		""" Смещение рабочего периода на произвольный месяц """
		if   year  is     None or month is None: return self.Dy(), self.Dm()
		else                                   :
			if year  is not None: self.Dy(year)
			if month is not None: self.Dm(month)

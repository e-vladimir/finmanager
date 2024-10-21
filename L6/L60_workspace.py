# РАБОЧЕЕ ПРОСТРАНСТВО: МЕХАНИКА ДАННЫХ

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

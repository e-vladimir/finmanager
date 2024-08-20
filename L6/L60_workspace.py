# РАБОЧЕЕ ПРОСТРАНСТВО: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINER_RAM
from L50_workspace  import C50_Workspace


class C60_Workspace(C50_Workspace):
	""" Рабочее пространство: Механика данных """

	# Параметры
	def Dy(self, year: int = None) -> int:
		""" Год """
		if year is None: return self.f_dy.ToInteger(CONTAINER_RAM).data
		else           :        self.f_dy.FromInteger(CONTAINER_RAM, year)

	def Dm(self, month: int = None) -> int:
		""" Месяц """
		if month is None: return self.f_dm.ToInteger(CONTAINER_RAM).data
		else            :        self.f_dm.FromInteger(CONTAINER_RAM, month)

	# IDO
	def SwitchToMain(self):
		""" Переключение на основное рабочее пространство """
		self.Ido("main")

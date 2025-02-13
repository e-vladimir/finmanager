# РАБОЧЕЕ ПРОСТРАНСТВО: МЕХАНИКА ДАННЫХ
# 12 фев 2025

from G10_datetime   import CalcDyDmByShiftDm

from L00_containers import CONTAINERS
from L50_workspace  import C50_Workspace


class C60_Workspace(C50_Workspace):
	""" Рабочее пространство: Механика данных """

	# Параметры
	@property
	def dy(self) -> int:
		return self.FDy.ToInteger(CONTAINERS.MEMORY).data
	@dy.setter
	def dy(self, year: int):
		self.FDy.FromInteger(CONTAINERS.MEMORY, year)

	@property
	def dm(self) -> int:
		return self.FDm.ToInteger(CONTAINERS.MEMORY).data
	@dm.setter
	def dm(self, month: int):
		self.FDm.FromInteger(CONTAINERS.MEMORY, month)

	# Управление IDO
	def SwitchToMain(self):
		""" Переключение на рабочее пространство: Основное """
		self.Ido("WORKSPACE_MAIN")

	# Управление Рабочим периодом
	def SwitchDyDmToNextDm(self):
		""" Смещение рабочего периода в следующий месяц """
		self.dy, self.dm = CalcDyDmByShiftDm(self.dy, self.dm,  1)

	def SwitchDyDmToPrevDm(self):
		""" Смещение рабочего периода в предыдущий месяц """
		self.dy, self.dm = CalcDyDmByShiftDm(self.dy, self.dm, -1)

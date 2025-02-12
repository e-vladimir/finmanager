# РАБОЧЕЕ ПРОСТРАНСТВО: МЕХАНИКА ДАННЫХ
# 12 фев 2025

from L00_containers import CONTAINERS
from L50_workspace import C50_Workspace


class C60_Workspace(C50_Workspace):
	""" Рабочее пространство: Механика данных """

	# Параметры
	@property
	def dy(self) -> int:
		return self.F_Dy.ToInteger(CONTAINERS.DISK).data
	@dy.setter
	def dy(self, year: int):
		self.F_Dy.FromInteger(CONTAINERS.DISK, year)

	@property
	def dm(self) -> int:
		return self.F_Dm.ToInteger(CONTAINERS.DISK).data
	@dm.setter
	def dm(self, month: int):
		self.F_Dm.FromInteger(CONTAINERS.DISK, month)

	# Управление IDO
	def SwitchToMain(self):
		""" Переключение на рабочее пространство: Основное """
		self.Ido("WORKSPACE_MAIN")

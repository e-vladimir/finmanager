# РАБОЧЕЕ ПРОСТРАНСТВО: ЛОГИКА ДАННЫХ
# 12 фев 2025

from L00_months    import MONTHS_SHORT
from L70_workspace import C70_Workspace


class C80_Workspace(C70_Workspace):
	""" Рабочее пространство: Логика данных """

	def DyDm(self) -> (int, int):
		""" Упаковка Год-Месяц в кортеж """
		return self.dy, self.dm

	def DmDyToString(self) -> str:
		""" Месяц-Год в текстовом формате """
		return f"{MONTHS_SHORT[self.dm]} {self.dy}"

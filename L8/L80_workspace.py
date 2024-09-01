# РАБОЧЕЕ ПРОСТРАНСТВО: ЛОГИКА ДАННЫХ

from G10_datetime  import CalcDyDmByShiftDm, CurrentDy

from L00_months    import MONTHS_SHORT
from L70_workspace import C70_Workspace


class C80_Workspace(C70_Workspace):
	""" Рабочее пространство: Логика данных """

	# Конвертация данных
	def DyDm(self) -> [int, int]:
		""" Вывод год-месяц в виде набора """
		return self.Dy(), self.Dm()

	def DmDyToString(self) -> str:
		""" Вывод Месяц-Год в текстовом формате """
		return f"{MONTHS_SHORT[self.Dm()]} {self.Dy():04d}"

	# Управление финпериодом
	def ShiftDmToNextDm(self):
		""" Смещение финпериода на следующий месяц """
		dy, dm = CalcDyDmByShiftDm(self.Dy(), self.Dm(), 1)

		self.Dy(dy)
		self.Dm(dm)

	def ShiftDmToPrevDm(self):
		""" Смещение финпериода на прошлый месяц """
		dy, dm = CalcDyDmByShiftDm(self.Dy(), self.Dm(), -1)

		self.Dy(dy)
		self.Dm(dm)

	# Генерация данных
	def AvailableDys(self) -> list[int]:
		""" Список доступных годов """
		return list(range(CurrentDy() - 5, CurrentDy() + 1))

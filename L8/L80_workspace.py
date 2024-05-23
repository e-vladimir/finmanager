# РАБОЧЕЕ ПРОСТРАНСТВО: ЛОГИКА ДАННЫХ

from L00_months    import MONTHS_SHORT

from L11_datetime  import CalcDyDmByShiftDm, CurrentDy
from L70_workspace import C70_Workspace


class C80_Workspace(C70_Workspace):
	""" Рабочее пространство: Логика данных """

	# Финпериод
	def ShiftByDm(self, count_dm: int):
		""" Смещение финпериода на указанное количество месяцев """
		dy, dm = CalcDyDmByShiftDm(self.Dy(), self.Dm(), count_dm)

		self.Dy(dy)
		self.Dm(dm)

	# Вывод информации
	def DmDyToString(self) -> str:
		""" Преобразование месяца, года в строку """
		return f"{MONTHS_SHORT[self.Dm()]} {self.Dy()}"

	# Генерация информации
	def Dys(self) -> list[int]:
		return list(range(CurrentDy() - 5, CurrentDy() + 1))

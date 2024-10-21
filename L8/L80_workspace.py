# РАБОЧЕЕ ПРОСТРАНСТВО: ЛОГИКА ДАННЫХ

from L00_months    import MONTHS
from L70_workspace import C70_Workspace


class C80_Workspace(C70_Workspace):
	""" Рабочее пространство: Логика данных """

	# Рабочий период
	def DmDyToString(self) -> str:
		""" МЕС ГОД """
		dm : str = MONTHS(self.Dm()).name_s
		dy : str = f"{self.Dy():04d}"

		return f"{dm} {dy}"

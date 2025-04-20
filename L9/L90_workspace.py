# РАБОЧЕЕ ПРОСТРАНСТВО: ЛОГИКА УПРАВЛЕНИЯ
# 12 фев 2025

from L80_workspace import C80_Workspace


class C90_Workspace(C80_Workspace):
	""" Рабочее пространство: Логика управления """

	def on_DyDmChange(self):
		""" Изменился год-месяц """
		self.CachingData()

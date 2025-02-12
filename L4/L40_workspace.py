# РАБОЧЕЕ ПРОСТРАНСТВО: МОДЕЛЬ ДАННЫХ
# 12 фев 2025

from G10_datetime     import CurrentDm, CurrentDy
from G30_cactus_frame import C30_StructField
from G31_cactus_frame import C31_StructFrameWithEvents


class C40_Workspace(C31_StructFrameWithEvents):
	""" Рабочее пространство: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.F_Dy = C30_StructField(self, "Год",   CurrentDy())
		self.F_Dm = C30_StructField(self, "Месяц", CurrentDm())

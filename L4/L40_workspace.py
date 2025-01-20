# РАБОЧЕЕ ПРОСТРАНСТВО: МОДЕЛЬ ДАННЫХ

from G10_datetime     import CurrentDy, CurrentDm
from G30_cactus_frame import C30_StructField
from G31_cactus_frame import C31_StructFrameWithEvents


class C40_Workspace(C31_StructFrameWithEvents):
	_idc = "Рабочее пространство"

	def Init_10(self):
		super().Init_10()

		self.f_dy            = C30_StructField(self, "Год",   CurrentDy())
		self.f_dm            = C30_StructField(self, "Месяц", CurrentDm())

		self.f_ido_operation = C30_StructField(self, "IDO Финансовой операции",      "")

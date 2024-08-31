# РАБОЧЕЕ ПРОСТРАНСТВО: МОДЕЛЬ ДАННЫХ

from G10_datetime     import CurrentDy, CurrentDm
from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_Workspace(C30_StructFrame):
	""" Рабочее пространство: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.f_dy                    = C30_StructField(self, "Год",   CurrentDy())
		self.f_dm                    = C30_StructField(self, "Месяц", CurrentDm())

		self.f_ido_finactions_record = C30_StructField(self, "IDO Записи финдействий", "")

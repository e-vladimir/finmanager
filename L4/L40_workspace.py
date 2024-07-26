# РАБОЧЕЕ ПРОСТРАНСТВО: МОДЕЛЬ ДАННЫХ

from G30_cactus_frame import C30_StructFrame, C30_StructField
from L11_datetime     import CurrentDy, CurrentDm


class C40_Workspace(C30_StructFrame):
	""" Рабочее пространство: Модель данных """

	_idc = "workspace"

	def Init_10(self):
		""" Инициализация параметров """
		self.f_dy                    = C30_StructField(self, "Год",   CurrentDy())
		self.f_dm                    = C30_StructField(self, "Месяц", CurrentDm())

		self.f_record_findata_ido    = C30_StructField(self, "Запись финданных")
		self.f_record_finactions_ido = C30_StructField(self, "Запись финдействий")
		self.f_record_rules_ido      = C30_StructField(self, "Запись правил")
		self.f_processing_type       = C30_StructField(self, "Тип обработки")

# ФИНАНСОВАЯ ОПЕРАЦИЯ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructField
from G31_cactus_frame import C31_StructFrameWithEvents


class C40_Operation(C31_StructFrameWithEvents):
	""" Финансовая операция: Модель данных """

	_idc = "Финансовая операция"

	def Init_10(self):
		super().Init_10()

		self.f_dy            = C30_StructField(self, "Год")
		self.f_dm            = C30_StructField(self, "Месяц")
		self.f_dd            = C30_StructField(self, "День")

		self.f_amount        = C30_StructField(self, "Сумма")
		self.f_destination   = C30_StructField(self, "Назначение")
		self.f_detail        = C30_StructField(self, "Уточнение")

		self.f_accounts_idos = C30_StructField(self, "Счета")
		self.f_object_int    = C30_StructField(self, "Объект внутренний")
		self.f_object_ext    = C30_StructField(self, "Объект внешний")

		self.f_color         = C30_StructField(self, "Цветовая метка")

class C40_Operations(C20_MetaFrame):
	""" Финансовые операции: Модель данных """
	pass

# ФИНСТРУКТУРА: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_FinstructRecord(C30_StructFrame):
	""" Запись финструктуры: Модель данных """

	_idc = "Финструктура"

	def Init_10(self):
		super().Init_10()

		self.f_dy         = C30_StructField(self, "Год")
		self.f_dm         = C30_StructField(self, "Месяц")

		self.f_name       = C30_StructField(self, "Наименование")


class C40_Finstruct(C20_MetaFrame):
	""" Финструктура: Модель данных """
	pass

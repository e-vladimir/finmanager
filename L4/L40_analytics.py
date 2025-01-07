# АНАЛИТИКА: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructField
from G31_cactus_frame import C31_StructFrameWithEvents


class C40_AnalyticsItem(C31_StructFrameWithEvents):
	""" Элемент аналитики: Модель данных """

	_idc = "Аналитика"

	def Init_10(self):
		super().Init_10()

		self.f_name    = C30_StructField(self, "Наименование")
		self.f_include = C30_StructField(self, "Признак включения")
		self.f_exclude = C30_StructField(self, "Признак исключения")


class C40_Analytics(C20_MetaFrame):
	""" Аналитика: Модель данных """
	pass

# АНАЛИТИКА ДАННЫХ: МОДЕЛЬ ДАННЫХ
# 27 апр 2025

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructField
from G31_cactus_frame import C31_StructFrameWithEvents


class C40_AnalyticsItem(C31_StructFrameWithEvents):
	""" Элемент аналитики данных: Модель данных """

	_idc = "Аналитика данных"

	def Init_10(self):
		super().Init_10()

		self.FName      = C30_StructField(self, "Название")
		self.FParentIdo = C30_StructField(self, "Корневой элемент")


class C40_Analytics(C20_MetaFrame):
	""" Аналитика: Модель данных """
	pass

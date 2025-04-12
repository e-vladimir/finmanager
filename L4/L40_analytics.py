# АНАЛИТИКА ДАННЫХ: МОДЕЛЬ ДАННЫХ
# 12 апр 2025

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructField
from G31_cactus_frame import C31_StructFrameWithEvents


class C40_AnalyticsItem(C31_StructFrameWithEvents):
	""" Элемент аналитики данных: Модель данных """

	_idc = "Элемент аналитики"

	def Init_10(self):
		super().Init_10()

		self.FName    = C30_StructField(self, "Название")
		self.FInclude = C30_StructField(self, "Признаки+")
		self.FExclude = C30_StructField(self, "Признаки-")


class C40_Analytics(C20_MetaFrame):
	""" Аналитика данных: Модель данных """
	pass

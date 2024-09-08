# ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_ProcessingRulesRecord(C30_StructFrame):
	""" Правила обработки данных: Модель данных """

	_idc = "Правило_обработки_данных"

	def Init_10(self):
		super().Init_10()

		self.f_type   = C30_StructField(self, "Тип правила")

		self.f_options_input  = C30_StructField(self, "Параметры входящие")
		self.f_options_output = C30_StructField(self, "Параметры исходящие")


class C40_ProcessingRules(C20_MetaFrame):
	""" Правила обработки данных: Модель данных """
	pass

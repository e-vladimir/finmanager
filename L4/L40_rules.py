# ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructField
from G31_cactus_frame import C31_StructFrameWithEvents


class C40_ProcessingRule(C31_StructFrameWithEvents):
	""" Правило обработки данных: Модель данных """

	_idc = "Правила обработки данных"

	def Init_10(self):
		super().Init_10()

		self.f_type   = C30_StructField(self, "Тип правила")
		self.f_input  = C30_StructField(self, "Вход данных")
		self.f_output = C30_StructField(self, "Выход данных")


class C40_ProcessingRules(C20_MetaFrame):
	""" Правила обработки данных: Модель данных """
	pass

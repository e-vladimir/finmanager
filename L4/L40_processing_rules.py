# ПРАВИЛА ОБРАБОТКИ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_RecordProcessingRules(C30_StructFrame):
	""" Правило обработки: Модель данных """

	_oci = "Правила обработки данных"

	def InitFields(self):
		""" Инициализация параметров """
		self.f_type           = C30_StructField(self, "Тип")

		self.f_options_input  = C30_StructField(self, "Параметры входящие")
		self.f_options_output = C30_StructField(self, "Параметры исходящие")


class C40_ProcessingRules(C20_MetaFrame):
	""" Правила обработки: Модель данных """

	def Init_00(self):
		self._oci                : str = ""

		self._pid_type           : str = ""
		self._pid_options_input  : str = ""
		self._pid_options_output : str = ""

	def Init_01(self):
		record_rule = C40_RecordProcessingRules()

		self._oci                      = record_rule.Oci().text

		self._pid_type                 = record_rule.f_type.Pid().text
		self._pid_options_input        = record_rule.f_options_input.Pid().text
		self._pid_options_output       = record_rule.f_options_output.Pid().text

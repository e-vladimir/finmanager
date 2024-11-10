# ОПЕРАЦИИ ПО СЧЕТАМ: СТРУКТУРА ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructField
from G31_cactus_frame import C31_StructFrameWithEvents


class C40_Operation(C31_StructFrameWithEvents):
	""" Операция по счету: Структура данных """

	_idc = "Операция по счету"

	def Init_10(self):
		super().Init_10()

		self.f_dy              = C30_StructField(self, "Год")
		self.f_dm              = C30_StructField(self, "Месяц")
		self.f_dd              = C30_StructField(self, "День")

		self.f_crc             = C30_StructField(self, "CRC")
		self.f_color           = C30_StructField(self, "Цветовая метка")

		self.f_src_amount      = C30_StructField(self, "Исходная сумма")
		self.f_src_description = C30_StructField(self, "Исходное описание")

		self.f_amount          = C30_StructField(self, "Сумма")
		self.f_description     = C30_StructField(self, "Описание")

		self.f_labels          = C30_StructField(self, "Метки")


class C40_Operations(C20_MetaFrame):
	""" Операции по счетам: Структура данных """
	pass

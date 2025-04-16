# ФИНАНСОВЫЕ ОПЕРАЦИИ: МОДЕЛЬ ДАННЫХ
# 11 мар 2025

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructField
from G31_cactus_frame import C31_StructFrameWithEvents


class C40_Operation(C31_StructFrameWithEvents):
	""" Финансовая операция: Модель данных """

	_idc = "Финансовая операция"

	def Init_10(self):
		self.FDy          = C30_StructField(self, "Год")
		self.FDm          = C30_StructField(self, "Месяц")
		self.FDd          = C30_StructField(self, "День")

		self.FAccountIdos = C30_StructField(self, "Счета")
		self.FAmount      = C30_StructField(self, "Сумма")
		self.FDescription = C30_StructField(self, "Описание")
		self.FDestination = C30_StructField(self, "Назначение")
		self.FColor       = C30_StructField(self, "Цветовая метка")
		self.FLabels      = C30_StructField(self, "Метки")
		self.FSkip        = C30_StructField(self, "Не учитывать")


class C40_Operations(C20_MetaFrame):
	""" Финансовые операции: Модель данных """
	pass

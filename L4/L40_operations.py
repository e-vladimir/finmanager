# ФИНАНСОВЫЕ ОПЕРАЦИИ: МОДЕЛЬ ДАННЫХ
# 11 мар 2025

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructField
from G31_cactus_frame import C31_StructFrameWithEvents


class C40_Operation(C31_StructFrameWithEvents):
	""" Финансовая операция: Модель данных """

	_idc = "Финансовая операция"

	def Init_00(self):
		super().Init_00()

		self._use_cache : bool = False

	def Init_10(self):
		super().Init_10()

		self.FAccountIdos    = C30_StructField(self, "Счета")
		self.FAmount         = C30_StructField(self, "Сумма")
		self.FColor          = C30_StructField(self, "Цветовая метка")
		self.FDd             = C30_StructField(self, "День")
		self.FDescription    = C30_StructField(self, "Описание")
		self.FDestination    = C30_StructField(self, "Назначение")
		self.FDm             = C30_StructField(self, "Месяц")
		self.FDy             = C30_StructField(self, "Год")
		self.FParentIdo      = C30_StructField(self, "Корневая операция")
		self.FSkip           = C30_StructField(self, "Не учитывать")
		self.FSrcDescription = C30_StructField(self, "Исходное описание")
		self.FVirtualIdos    = C30_StructField(self, "Виртуальные операции")


class C40_Operations(C20_MetaFrame):
	""" Финансовые операции: Модель данных """
	pass

# ФИНСОСТАВ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_FincompositionRecord(C30_StructFrame):
	""" Запись финсостава: Модель данных """

	_idc = "Финсостав"

	def Init_10(self):
		super().Init_10()

		self.f_name       = C30_StructField(self, "Наименование")
		self.f_parent_ido = C30_StructField(self, "IDO верхнего уровня")


class C40_Fincomposition(C20_MetaFrame):
	""" Финсостав: Модель данных """
	pass

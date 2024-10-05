# ФИНСОСТАВ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_FincompositionRecord(C30_StructFrame):
	""" Запись финсостава: Модель данных """

	_idc = "Финсостав"

	def Init_10(self):
		super().Init_10()

		self.f_category   = C30_StructField(self, "Категория финсостава")

		self.f_name       = C30_StructField(self, "Наименование")
		self.f_parent_ido = C30_StructField(self, "IDO верхнего уровня")

		self.f_marks_inc  = C30_StructField(self, "Признак усиления")
		self.f_marks_dec  = C30_StructField(self, "Признак ослабления")
		self.f_marks_100  = C30_StructField(self, "Признак подтверждения")
		self.f_marks_000  = C30_StructField(self, "Признак отрицания")


class C40_Fincomposition(C20_MetaFrame):
	""" Финсостав: Модель данных """
	pass

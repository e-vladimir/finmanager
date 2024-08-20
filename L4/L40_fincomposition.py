# ФИНСОСТАВ: МОДЕЛЬ ДАННЫХ

from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_Fincomposition(C30_StructFrame):
	""" Финсостав: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.f_name       = C30_StructField(self, "Название")
		self.f_parent_ido = C30_StructField(self, "IDO верхнего уровня")

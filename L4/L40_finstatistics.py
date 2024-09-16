# ФИНСТАТИСТИКА: МОДЕЛЬ ДАННЫХ

from G20_meta_frame import C20_MetaFrame

from L90_finactions import C90_Finactions


class C40_Finstatistics(C20_MetaFrame):
	""" Финстатистика: Модель данных """

	def Init_10(self):
		self.finactions = C90_Finactions()

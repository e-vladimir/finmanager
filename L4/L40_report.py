# ГЕНЕРАТОР ОТЧЁТОВ: МОДЕЛЬ ДАННЫХ
# 10 мар 2025

from G20_meta_frame import C20_MetaFrame

from L90_account    import C90_Accounts


class C40_Report(C20_MetaFrame):
	""" Генератор отчётов: Модель данных """

	def Init_10(self):
		self.Accounts  = C90_Accounts()

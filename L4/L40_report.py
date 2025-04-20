# ГЕНЕРАТОР ОТЧЁТОВ: МОДЕЛЬ ДАННЫХ
# 10 мар 2025

from G20_meta_frame import C20_MetaFrame

from L90_account    import C90_Accounts
from L90_operations import C90_Operations


class C40_Report(C20_MetaFrame):
	""" Генератор отчётов: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.Accounts   = C90_Accounts()
		self.Operations = C90_Operations()

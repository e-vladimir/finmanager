# ОТЧЁТНОСТЬ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame import C20_MetaFrame

from L90_accounts   import C90_Accounts
from L90_operations import C90_Operations


class C40_Report(C20_MetaFrame):
	""" Отчётность: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.accounts   = C90_Accounts()
		self.operations = C90_Operations()

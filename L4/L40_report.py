# ОТЧЁТНОСТЬ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame import C20_MetaFrame

from L90_accounts   import C90_Accounts
from L90_operations import C90_Operations
from L90_statistic  import C90_Statistic


class C40_Report(C20_MetaFrame):
	""" Отчётность: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.accounts   = C90_Accounts()
		self.statistics = C90_Statistic()
		self.operations = C90_Operations()

# ФОРМА ОБРАБОТКА ДАННЫХ: МОДЕЛЬ ДАННЫХ
# 22 мар 2025

from L41_form_processing import C41_FormProcessing
from L90_operations      import C90_Operations
from L90_workspace       import C90_Workspace


class C42_FormProcessing(C41_FormProcessing):
	""" Форма Обработка данных: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.Operations          = C90_Operations()
		self.Workspace           = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.Workspace.SwitchToMain()

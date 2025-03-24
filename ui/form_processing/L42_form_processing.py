# ФОРМА ОБРАБОТКА ДАННЫХ: МОДЕЛЬ ДАННЫХ
# 22 мар 2025

from L20_PySide6         import C20_StandardItemModel
from L41_form_processing import C41_FormProcessing
from L90_operations      import C90_Operations
from L90_workspace       import C90_Workspace


class C42_FormProcessing(C41_FormProcessing):
	""" Форма Обработка данных: Модель данных """

	def Init_00(self):
		super().Init_00()

	def Init_10(self):
		super().Init_10()

		self.ModelDataManual = C20_StandardItemModel()

		self.Operations      = C90_Operations()
		self.Workspace       = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.Workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.TreeDataManual.setModel(self.ModelDataManual)

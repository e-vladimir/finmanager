# ФОРМА ОБРАБОТКА ДАННЫХ: МОДЕЛЬ ДАННЫХ
# 22 мар 2025

from L00_colors          import COLORS
from L00_form_processing import PROCESSING_FIELDS
from L20_PySide6         import C20_StandardItemModel
from L41_form_processing import C41_FormProcessing
from L90_operations      import C90_Operations
from L90_workspace       import C90_Workspace


class C42_FormProcessing(C41_FormProcessing):
	""" Форма Обработка данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._operations_filter_description             : str    = ""
		self._operations_processing_replace_description : str    = ""
		self._operations_processing_set_description     : str    = ""
		self._operations_processing_set_color           : COLORS = COLORS.BLACK

		self._processing_field                          : PROCESSING_FIELDS = PROCESSING_FIELDS.NONE

	def Init_10(self):
		super().Init_10()

		self.ModelDataOperations = C20_StandardItemModel()

		self.Operations          = C90_Operations()
		self.Workspace           = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.Workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.TreeDataOperations.setModel(self.ModelDataOperations)

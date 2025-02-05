# ФОРМА ОБРАБОТКА ДАННЫХ: МОДЕЛЬ ДАННЫХ

from L00_colors          import COLORS
from L00_form_processing import INTERVALS
from L20_PySide6         import C20_StandardItemModel
from L41_form_processing import C41_FormProcessing
from L90_operations      import C90_Operations
from L90_workspace       import C90_Workspace


class C42_FormProcessing(C41_FormProcessing):
	""" Форма Обработка данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._operations_include     : str       = ""
		self._operations_exclude     : str       = ""
		self._operations_destination : str       = ""
		self._operations_detail      : str       = ""
		self._operations_object_int  : str       = ""
		self._operations_object_ext  : str       = ""
		self._operations_color       : COLORS    = COLORS.NONE
		self._operations_interval    : INTERVALS = INTERVALS.DM

		self._processing_ido         : str       = ""

	def Init_10(self):
		super().Init_10()

		self.model_operations = C20_StandardItemModel()

		self.operations       = C90_Operations()
		self.workspace        = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.tree_data_operations.setModel(self.model_operations)

# ФОРМА ПРАВИЛ ОБРАБОТКИ: МОДЕЛЬ ДАННЫХ

from L20_PySide6          import C20_StandardItemModel
from L41_form_rules       import C41_FormRules
from L90_findescription   import C90_Findescription
from L90_processing_rules import C90_ProcessingRules


class C42_FormRules(C41_FormRules):
	""" Форма правил обработки: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._ido_processing    : str = ""
		self._type_processing   : str = ""
		self._column_processing : int = -1
		self._name_processing   : str = ""

	def Init_10(self):
		super().Init_10()

		self.findescription = C90_Findescription()
		self.rules          = C90_ProcessingRules()

		self.model_data     = C20_StandardItemModel(None)

	def Init_20(self):
		super().Init_20()

		self.tree_data.setModel(self.model_data)

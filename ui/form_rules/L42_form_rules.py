# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МОДЕЛЬ ДАННЫХ

from L00_rules      import RULES
from L20_PySide6    import C20_StandardItemModel
from L41_form_rules import C41_FormRules
from L90_rules      import C90_ProcessingRules


class C42_FormRules(C41_FormRules):
	""" Форма Правила обработки данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_type   : RULES | None = None
		self._processing_ido    : str          = ""
		self._processing_name   : str          = ""
		self._processing_column : int          = -1

	def Init_10(self):
		super().Init_10()

		self.rules      = C90_ProcessingRules()

		self.model_data = C20_StandardItemModel()

	def Init_20(self):
		super().Init_20()

		self.table_data.setModel(self.model_data)

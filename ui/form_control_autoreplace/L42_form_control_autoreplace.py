# ФОРМА УПРАВЛЕНИЕ АВТОЗАМЕНОЙ: МОДЕЛЬ ДАННЫХ

from L20_PySide6                  import C20_StandardItemModel
from L41_form_control_autoreplace import C41_FormControlAutoreplace
from L90_rules                    import C90_ProcessingRules


class C42_FormControlAutoreplace(C41_FormControlAutoreplace):
	""" Форма Управление автозаменой: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_ido    : str = ""
		self._processing_output : str = ""

	def Init_10(self):
		super().Init_10()

		self.model_data = C20_StandardItemModel()

		self.rules      = C90_ProcessingRules()

	def Init_20(self):
		super().Init_20()

		self.table_data.setModel(self.model_data)

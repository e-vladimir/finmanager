# ФОРМА УПРАВЛЕНИЕ АВТОЗАМЕНОЙ: МЕХАНИКА ДАННЫХ

from L20_PySide6                  import C20_StandardItem, ROLES
from L50_form_control_autoreplace import C50_FormControlAutoreplace
from L90_rules                    import C90_ProcessingRule


class C60_FormControlAutoreplace(C50_FormControlAutoreplace):
	""" Форма Управление автозаменой: Механика данных """

	# Модель данных
	def InitModelData(self):
		""" Инициализация модели данных """
		self.model_data.removeAll()

		self.model_data.setHorizontalHeaderLabels(["Фрагмент поиска", "Фрагмент замены"])

	def LoadRuleAutoreplace(self):
		""" Загрузка правила автозамены """
		if not self._processing_ido: return

		rule         = C90_ProcessingRule(self._processing_ido)

		if not self.model_data.checkIdo(self._processing_ido):
			item_input  = C20_StandardItem('\n'.join(rule.InputAsStrings()))
			item_input.setData(self._processing_ido, ROLES.IDO)

			item_output = C20_StandardItem(rule.OutputAsString())
			item_output.setData(self._processing_ido, ROLES.IDO)

			root_item   = self.model_data.invisibleRootItem()
			root_item.appendRow([item_input, item_output])

		indexes_data = self.model_data.indexesInRowByIdo(self._processing_ido)

		item_input   = self.model_data.itemFromIndex(indexes_data[0])
		item_input.setText('\n'.join(rule.InputAsStrings()))

		item_output  = self.model_data.itemFromIndex(indexes_data[1])
		item_output.setText(rule.OutputAsString())

# ФОРМА УПРАВЛЕНИЕ ОПИСАНИЕМ: МЕХАНИКА ДАННЫХ

from L20_PySide6                  import C20_StandardItem, ROLES
from L50_form_control_description import C50_FormControlDescription
from L90_rules                    import C90_ProcessingRule


class C60_FormControlDescription(C50_FormControlDescription):
	""" Форма Управление описанием: Механика данных """

	# Модель правил
	def InitModelRules(self):
		""" Инициализация модели правил """
		self.model_rules.removeAll()

		self.model_rules.setHorizontalHeaderLabels(["Фрагмент поиска", "Фрагмент замены"])

	def LoadRuleInModel(self):
		""" Загрузка правила в модель данных """
		if not self._processing_ido: return

		rule = C90_ProcessingRule(self._processing_ido)

		if not self.model_rules.checkIdo(self._processing_ido):
			item_input  = C20_StandardItem("")
			item_input.setData(self._processing_ido, ROLES.IDO)

			item_output = C20_StandardItem("")
			item_output.setData(self._processing_ido, ROLES.IDO)

			root_item   = self.model_rules.invisibleRootItem()
			root_item.appendRow([item_input, item_output])

		indexes     = self.model_rules.indexesInRowByIdo(self._processing_ido)

		item_input  = self.model_rules.itemFromIndex(indexes[0])
		item_input.setText('\n'.join(rule.InputAsStrings()))

		item_output = self.model_rules.itemFromIndex(indexes[1])
		item_output.setText(rule.OutputAsString())

	# Модель управления
	def InitModelControl(self):
		""" Инициализация модели управления """
		self.model_control.removeAll()

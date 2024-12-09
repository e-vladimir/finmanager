# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: МЕХАНИКА ДАННЫХ

from L00_rules                      import RULES

from L20_PySide6                    import C20_StandardItem, ROLES
from L50_form_processing_operations import C50_FormProcessingOperations
from L90_rules                      import C90_ProcessingRule


class C60_FormProcessingOperations(C50_FormProcessingOperations):
	""" Форма Обработка операций: Механика данных """

	# Модель правил
	def InitModelRules(self):
		""" Инициализация модели правил """
		self.model_rules.removeAll()

		match self._processing_rule_types:
			case RULES.REPLACE_DESCRIPTION: self.model_rules.setHorizontalHeaderLabels(["Фрагменты поиска", "Фрагмент замены"])
			case RULES.MATCH_DESTINATION  : self.model_rules.setHorizontalHeaderLabels(["Фрагменты поиска", "Фрагмент сопоставления"])
			case RULES.DETECT_LABEL       : self.model_rules.setHorizontalHeaderLabels(["Фрагменты поиска", "Применяемые метки"])

	def LoadRuleToModel(self):
		""" Загрузка правила в модель """
		if not self.model_rules.checkIdo(self._processing_ido):
			item_input  = C20_StandardItem("")
			item_input.setData(self._processing_ido, ROLES.IDO)

			item_output = C20_StandardItem("")
			item_output.setData(self._processing_ido, ROLES.IDO)

			self.model_rules.invisibleRootItem().appendRow([item_input, item_output])

		rule        = C90_ProcessingRule(self._processing_ido)

		indexes     = self.model_rules.indexesInRowByIdo(self._processing_ido)
		item_input  = self.model_rules.itemFromIndex(indexes[0])
		item_input.setText('\n'.join(rule.InputAsStrings()))

		item_output = self.model_rules.itemFromIndex(indexes[1])
		item_output.setText('\n'.join(rule.OutputAsStrings()))

	# Параметры
	def SwitchRuleTypesToDescription(self):
		""" Смена типа правил на Описание """
		self._processing_rule_types = RULES.REPLACE_DESCRIPTION

	def SwitchRuleTypesToDestination(self):
		""" Смена типа правил на Назначение """
		self._processing_rule_types = RULES.MATCH_DESTINATION

	def SwitchRuleTypesToLabels(self):
		""" Смена типа правил на Метки """
		self._processing_rule_types = RULES.DETECT_LABEL

	def ReadProcessingIdoFromTableRules(self):
		""" Чтение текущего IDO из таблицы правил """
		current_index = self.table_rules.currentIndex()
		self._processing_ido = current_index.data(ROLES.IDO)

	def ReadProcessingIdoFromWorkspace(self):
		""" Чтение текущего IDO из рабочего пространства """
		self._processing_ido = self.workspace.IdoRule()

	def WriteProcessingRuleToWorkspace(self):
		""" Запись правила обработки к рабочее пространство """
		self.workspace.IdoRule(self._processing_ido)

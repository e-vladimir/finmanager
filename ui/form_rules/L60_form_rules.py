# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МЕХАНИКА ДАННЫХ

from L00_rules      import RULES
from L20_PySide6    import C20_StandardItem
from L50_form_rules import C50_FormRules
from L90_rules      import C90_ProcessingRule


class C60_FormRules(C50_FormRules):
	""" Форма Правила обработки данных: Механика данных """

	# Параметры
	def ReadProcessingTypeFromCbboxTypes(self):
		""" Чтение типа правил из списка типов правил обработки данных """
		self._processing_type = RULES(self.cbbox_types.currentText())

	# Модель данных
	def InitModelData(self):
		""" Инициализация модели данных """
		self.model_data.removeAll()

		labels : list[str] = ["", ""]

		match self._processing_type:
			case RULES.UNKNOWN             : pass
			case RULES.REPLACE_TEXT        : labels = ["Поиск", "Замена"]
			case RULES.DETECT_LABEL_BY_TEXT: labels = ["Поиск", "Метки"]

		self.model_data.setHorizontalHeaderLabels(labels)

	def LoadRule(self):
		""" Загрузка правила обработки данных """
		if not self._processing_ido: return

		rule         = C90_ProcessingRule(self._processing_ido)

		if not self.model_data.checkIdo(self._processing_ido):
			item_input  = C20_StandardItem("", self._processing_ido)
			item_output = C20_StandardItem("", self._processing_ido)

			item_root   = self.model_data.invisibleRootItem()

			item_root.appendRow([item_input, item_output])

		indexes      = self.model_data.indexesInRowByIdo(self._processing_ido)
		index_input  = indexes[0]
		index_output = indexes[1]

		item_input   = self.model_data.itemFromIndex(index_input)
		item_input.setText('\n'.join(rule.InputAsStrings()))

		item_output  = self.model_data.itemFromIndex(index_output)
		item_output.setText('\n'.join(rule.OutputAsStrings()))

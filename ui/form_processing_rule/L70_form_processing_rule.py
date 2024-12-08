# ФОРМА ПРАВИЛО ОБРАБОТКИ: МЕХАНИКА УПРАВЛЕНИЯ

from L00_rules                import RULES
from L60_form_processing_rule import C60_FormProcessingRule


class C70_FormProcessingRule(C60_FormProcessingRule):
	""" Форма Правило обработки: Механика управления """

	# Панель input
	def ShowInput(self):
		""" Отображение панели input """
		title            : str  = ""
		visible_single   : bool = False
		visible_multiple : bool = False
		visible_items    : bool = False

		match self.processing_rule.RuleType():
			case RULES.REPLACE_DESCRIPTION:
				title            = "Фрагменты поиска"
				visible_multiple = True

			case RULES.MATCH_DESTINATION:
				title            = "Фрагменты поиска"
				visible_multiple = True

			case RULES.MATCH_DESTINATION:
				title            = "Фрагменты поиска"
				visible_multiple = True

		self.label_input.setText(title)
		self.edit_input_single.setVisible(visible_single)
		self.edit_input_multiple.setVisible(visible_multiple)
		self.list_input_items.setVisible(visible_items)

	def FillInput(self):
		""" Заполнение полей Input """
		self.list_input_items.clear()

		self.edit_input_single.setText(self.processing_rule.InputAsString())
		self.edit_input_multiple.setPlainText('\n'.join(self.processing_rule.InputAsStrings()))
		self.list_input_items.addItems(self.processing_rule.InputAsStrings())

	# Панель output
	def ShowOutput(self):
		""" Отображение панели output """
		title            : str  = ""
		visible_single   : bool = False
		visible_multiple : bool = False
		visible_items    : bool = False

		match self.processing_rule.RuleType():
			case RULES.REPLACE_DESCRIPTION:
				title            = "Фрагмент замены"
				visible_single   = True

			case RULES.MATCH_DESTINATION:
				title            = "Фрагмент сопоставления"
				visible_single   = True

			case RULES.MATCH_DESTINATION:
				title            = "Метки"
				visible_multiple = True

		self.label_output.setText(title)
		self.edit_output_single.setVisible(visible_single)
		self.edit_output_multiple.setVisible(visible_multiple)
		self.list_output_items.setVisible(visible_items)

	def FillOutput(self):
		""" Заполнение полей Output """
		self.list_output_items.clear()

		self.edit_output_single.setText(self.processing_rule.OutputAsString())
		self.edit_output_multiple.setPlainText('\n'.join(self.processing_rule.OutputAsStrings()))
		self.list_output_items.addItems(self.processing_rule.OutputAsStrings())

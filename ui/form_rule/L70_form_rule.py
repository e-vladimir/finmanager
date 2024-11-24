# ФОРМА ПРАВИЛО ОБРАБОТКИ ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

from L00_rules     import RULES
from L60_form_rule import C60_FormRule


class C70_FormRule(C60_FormRule):
	""" Форма Правило обработки данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(self.rule.Type().value)

	# Поле ввода Input
	def FillEditInput(self):
		""" Заполнение поля ввода Input """
		self.edit_input.setPlainText(self.rule.InputAsString())

	def AdjustEditInput_Placeholder(self):
		""" Настройка поля ввода Input: Placeholder """
		match self.rule.Type():
			case RULES.REPLACE_TEXT        : self.edit_input.setPlaceholderText("Фрагменты поиска")
			case RULES.DETECT_LABEL_BY_TEXT: self.edit_input.setPlaceholderText("Фрагменты поиска")
			case _                         : self.edit_input.setPlaceholderText("---")

	# Поле ввода Output
	def FillEditOutput(self):
		""" Заполнение поля ввода Output """
		self.edit_output.setPlainText(self.rule.OutputAsString())

	def AdjustEditOutput_Placeholder(self):
		""" Настройка поля ввода Output: Placeholder """
		match self.rule.Type():
			case RULES.REPLACE_TEXT        : self.edit_output.setPlaceholderText("Фрагмент замены")
			case RULES.DETECT_LABEL_BY_TEXT: self.edit_output.setPlaceholderText("Метки")
			case _                         : self.edit_output.setPlaceholderText("---")

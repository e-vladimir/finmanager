# ФОРМА ПРАВИЛО ОБРАБОТКИ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_rule import C80_FormRule


class C90_FormRule(C80_FormRule):
	""" Форма Правило обработки данных: Логика управления """

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ReadIdoRuleFromWorkspace()

		self.FillEditInput()
		self.FillEditOutput()

		self.AdjustEditInput_Placeholder()
		self.AdjustEditOutput_Placeholder()

		self.ShowTitle()

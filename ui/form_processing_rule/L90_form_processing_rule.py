# ФОРМА ПРАВИЛО ОБРАБОТКИ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_processing_rule import C80_FormProcessingRule


class C90_FormProcessingRule(C80_FormProcessingRule):
	""" Форма Правило обработки: Логика управления """

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ReadProcessingRuleFromWorkspace()

		self.ShowInput()
		self.ShowOutput()

		self.FillInput()
		self.FillOutput()

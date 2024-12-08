# ФОРМА ПРАВИЛО ОБРАБОТКИ: МЕХАНИКА ДАННЫХ

from L50_form_processing_rule import C50_FormProcessingRule


class C60_FormProcessingRule(C50_FormProcessingRule):
	""" Форма Правило обработки: Механика данных """

	# Параметры
	def ReadProcessingRuleFromWorkspace(self):
		""" Чтение правила обработки из рабочего пространства """
		self.processing_rule.Ido(self.workspace.IdoRule())

	def WriteProcessingRuleToWorkspace(self):
		""" Запись правила обработки в рабочее пространство """
		self.workspace.IdoRule(self.processing_rule.Ido().data)

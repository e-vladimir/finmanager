# ФОРМА УПРАВЛЕНИЕ ОПИСАНИЕМ: ЛОГИКА ДАННЫХ

from L00_containers               import CONTAINERS
from L00_rules                    import RULES

from L20_PySide6 import RequestConfirm, RequestMultipleText, RequestText
from L70_form_control_description import C70_FormControlDescription
from L90_rules                    import C90_ProcessingRule


class C80_FormControlDescription(C70_FormControlDescription):
	""" Форма Управление описанием: Логика данных """

	# Правила автозамены описания
	def ShowRules(self):
		""" Отображение правил автозамены описания """
		for self._processing_ido in self.rules.IdosByType(RULES.REPLACE_DESCRIPTION): self.LoadRuleInModel()

	# Правило автозамены описания
	def CreateRule(self):
		""" Создание правила автозамены описания """
		text_output : str | None = RequestText("Правило автозамены описания", "Создание правила автозамены описания", "")
		if text_output is None: return

		rule = C90_ProcessingRule()
		rule.GenerateIdo()
		rule.RegisterObject(CONTAINERS.DISK)

		rule.RuleType(RULES.REPLACE_DESCRIPTION)

		rule.OutputAsString(text_output)

		self._processing_ido = rule.Ido().data

	def DeleteRule(self):
		""" Удаление правила """
		rule = C90_ProcessingRule(self._processing_ido)

		if not RequestConfirm("Правило автозамены описания", f"Удаление правила по автозамене описания.\n\nФрагменты поиска:{', '.join(rule.InputAsString())}\n\nФрагмент замены: {rule.OutputAsString()}"): return

		rule.DeleteObject(CONTAINERS.DISK)

	def EditRuleInput(self):
		""" Редактирование входа правила """
		rule                     = C90_ProcessingRule(self._processing_ido)

		texts : list[str] | None = RequestMultipleText("Правило автозамены описания", f"Фрагмент замены: {rule.OutputAsString()}\n\nФрагмент поиска:", rule.InputAsStrings())
		if texts is None: return

		rule.InputAsStrings(texts)

	def EditRuleOutput(self):
		""" Редактирование выхода правила """
		rule              = C90_ProcessingRule(self._processing_ido)

		text : str | None = RequestText("Правило автозамены описания", f"Фрагменты поиска:\n{'\n'.join(rule.InputAsStrings())}\n\nФрагмент замены:", rule.OutputAsString())
		if text is None: return

		rule.OutputAsString(text)

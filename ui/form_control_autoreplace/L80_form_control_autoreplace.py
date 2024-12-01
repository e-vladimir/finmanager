# ФОРМА УПРАВЛЕНИЕ АВТОЗАМЕНОЙ: ЛОГИКА ДАННЫХ

from L00_containers               import CONTAINERS
from L00_rules                    import RULES

from L20_PySide6                  import RequestText, RequestMultipleText
from L70_form_control_autoreplace import C70_FormControlAutoreplace
from L90_rules                    import C90_ProcessingRule


class C80_FormControlAutoreplace(C70_FormControlAutoreplace):
	""" Форма Управление автозаменой: Логика данных """

	# Правила автозамены
	def ShowRules(self):
		""" Отображение правил """
		for self._processing_ido in self.rules.IdosByType(RULES.REPLACE_TEXT, True): self.LoadRuleAutoreplace()

	# Правила автозамены
	def CreateRule(self):
		""" Создание правила автозамены """
		text_output : str | None       = RequestText("Создание правила автозамены", "Фрагмент замены:", "")
		if text_output is None: return

		text_input  : list[str] | None = RequestMultipleText("Создание правила автозамены", f"Фрагмент замены: {text_output}\n\nФрагменты поиска:", [])
		if text_input  is None: return

		rule                           = C90_ProcessingRule()
		rule.GenerateIdo()
		rule.RegisterObject(CONTAINERS.DISK)

		rule.Type(RULES.REPLACE_TEXT)
		rule.InputAsStrings(text_input)
		rule.OutputAsString(text_output)

		self._processing_ido = rule.Ido().data

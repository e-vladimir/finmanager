# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: ЛОГИКА ДАННЫХ

from L00_containers import CONTAINERS
from L00_rules      import RULES
from L20_PySide6    import RequestMultipleText, RequestText
from L70_form_rules import C70_FormRules
from L90_rules      import C90_ProcessingRule


class C80_FormRules(C70_FormRules):
	""" Форма Правила обработки данных: Логика данных """

	# Правила обработки данных
	def ShowRules(self):
		""" Загрузка правил обработки данных """
		for self._processing_ido in self.rules.IdosByType(self._processing_type): self.LoadRule()

	# Правило обработки данных
	def CreateRule(self):
		""" Создание правила обработки данных """
		data_output : list[str] | None = None

		match self._processing_type:
			case RULES.REPLACE_TEXT:
				data : str | None       = RequestText("Создание правила обработки данных",         f"{self._processing_type.value}\n\nНа что заменить", "")
				if data is None: return

				data_output = [data]

			case RULES.DETECT_LABEL_BY_TEXT:
				data : list[str] | None = RequestMultipleText("Создание правила обработки данных", f"{self._processing_type.value}\n\nМетки",           [])
				if data is None: return

				data_output = data.copy()

		if data_output is None: return

		rule                           = C90_ProcessingRule()
		rule.GenerateIdo()
		rule.RegisterObject(CONTAINERS.DISK)

		rule.Type(self._processing_type)
		rule.InputAsString("")
		rule.OutputAsStrings(data_output)

# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: ЛОГИКА ДАННЫХ

from L00_containers import CONTAINER_LOCAL
from L00_rules      import RULES

from L20_PySide6    import RequestText, RequestMultipleText, RequestConfirm
from L70_form_rules import C70_FormRules
from L90_rules      import C90_ProcessingRulesRecord


class C80_FormRules(C70_FormRules):
	""" Форма Правила обработки данных: Логика данных """

	# Правила обработки данных
	def LoadRules(self):
		""" Загрузка правил обработки данных """
		if not self._processing_type: return

		for self._processing_ido in self.rules.IdosByType(self._processing_type): self.LoadRulesRecord()

	# Правило замены текстового фрагмента
	def CreateRuleReplaceText(self):
		""" Создание правила замены текстового фрагмента """
		if self._processing_type is None: return

		text : str | None = RequestText("Создание правила", "На что заменяется")
		if text is None: return

		rule_record = C90_ProcessingRulesRecord()
		rule_record.GenerateIdo()
		rule_record.RegisterObject(CONTAINER_LOCAL)
		rule_record.Type(RULES.REPLACE_TEXT)
		rule_record.OptionsInputAsString("")
		rule_record.OptionsOutputAsString(text)

	def EditInputRuleReplaceText(self):
		""" Редактирование фрагмента поиска правила замены текстового фрагмента """
		if not self._processing_ido: return

		record = C90_ProcessingRulesRecord(self._processing_ido)

		texts : list[str] | None = RequestMultipleText("Правило замены текста", f"Замена на {record.OptionsOutputAsString()}", record.OptionsInputAsStrings())
		if texts is None: return

		record.OptionsInputAsStrings(texts)

	def EditOutputRuleReplaceText(self):
		""" Редактирование фрагмента замены правила замены текстового фрагмента """
		if not self._processing_ido: return

		record = C90_ProcessingRulesRecord(self._processing_ido)

		text : str | None = RequestText("Правило замены текста", f"Замена на {record.OptionsOutputAsString()}", record.OptionsOutputAsString())
		if text is None: return

		record.OptionsOutputAsString(text)

	def DeleteRuleReplaceText(self):
		""" Удаление правила замены текста """
		if not self._processing_ido: return

		record = C90_ProcessingRulesRecord(self._processing_ido)

		if not RequestConfirm("Удаление правила замены текста", f"Замена на {record.OptionsOutputAsString()}"): return

		record.DeleteObject(CONTAINER_LOCAL)

	# Правило определения метки
	def CreateRuleDetectLabel(self):
		""" Создание правила определения метки """
		if self._processing_type is None: return

		text : str | None = RequestText("Создание правила", "Метка")
		if text is None: return

		rule_record = C90_ProcessingRulesRecord()
		rule_record.GenerateIdo()
		rule_record.RegisterObject(CONTAINER_LOCAL)
		rule_record.Type(RULES.DETECT_LABEL)
		rule_record.OptionsInputAsString("")
		rule_record.OptionsOutputAsString(text)

	def EditInputRuleDetectLabel(self):
		""" Редактирование фрагмента поиска определения метки """
		if not self._processing_ido: return

		record = C90_ProcessingRulesRecord(self._processing_ido)

		texts : list[str] | None = RequestMultipleText("Правило определения метки", f"Поиск метки {record.OptionsOutputAsString()}", record.OptionsInputAsStrings())
		if texts is None: return

		record.OptionsInputAsStrings(texts)

	def EditOutputRuleDetectLabel(self):
		""" Редактирование метки правила определения метки """
		if not self._processing_ido: return

		record = C90_ProcessingRulesRecord(self._processing_ido)

		text : str | None = RequestText("Правило определения метки", f"Поиск метки {record.OptionsOutputAsString()}", record.OptionsOutputAsString())
		if text is None: return

		record.OptionsOutputAsString(text)

	def DeleteRuleDetectLabel(self):
		""" Удаление правила определения метки """
		if not self._processing_ido: return

		record = C90_ProcessingRulesRecord(self._processing_ido)

		if not RequestConfirm("Удаление правила определения метки", f"Определение метки {record.OptionsOutputAsString()}"): return

		record.DeleteObject(CONTAINER_LOCAL)

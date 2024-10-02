# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: ЛОГИКА ДАННЫХ

from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QProgressDialog

from L00_containers    import CONTAINER_LOCAL
from L00_rules         import RULES

from L20_PySide6       import RequestText, RequestMultipleText, RequestConfirm
from L70_form_rules    import C70_FormRules
from L90_rules         import C90_ProcessingRulesRecord


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
	def CreateRuleDetectLabels(self):
		""" Создание правила определения меток """
		if self._processing_type is None: return

		labels : list[str] | None = RequestMultipleText("Создание правила", "Метки")
		if labels is None: return

		rule_record               = C90_ProcessingRulesRecord()
		rule_record.GenerateIdo()
		rule_record.RegisterObject(CONTAINER_LOCAL)
		rule_record.Type(RULES.DETECT_LABELS)
		rule_record.OptionsInputAsString("")
		rule_record.OptionsOutputAsStrings(labels)

	def EditInputRuleDetectLabels(self):
		""" Редактирование фрагмента поиска определения меток """
		if not self._processing_ido: return

		record                   = C90_ProcessingRulesRecord(self._processing_ido)
		labels : str             = ', '.join(record.OptionsOutputAsStrings())
		labels                   = labels[:50]

		texts : list[str] | None = RequestMultipleText("Правило определения меток", f"Поиск меток {labels}", record.OptionsInputAsStrings())
		if texts is None: return

		record.OptionsInputAsStrings(texts)

	def EditOutputRuleDetectLabels(self):
		""" Редактирование меток правила определения меток """
		if not self._processing_ido: return

		record                    = C90_ProcessingRulesRecord(self._processing_ido)
		labels : str              = ', '.join(record.OptionsOutputAsStrings())
		labels                    = labels[:50]

		labels : list[str] | None = RequestMultipleText("Правило определения меток", f"Поиск меток {labels}", record.OptionsOutputAsStrings())
		if labels is None: return

		record.OptionsOutputAsStrings(labels)

	def DeleteRuleDetectLabels(self):
		""" Удаление правила определения меток """
		if not self._processing_ido: return

		record       = C90_ProcessingRulesRecord(self._processing_ido)
		labels : str = ', '.join(record.OptionsOutputAsStrings())
		labels       = labels[:50]

		if not RequestConfirm("Удаление правила определения метки", f"Определение меток {labels}"): return

		record.DeleteObject(CONTAINER_LOCAL)

	# Сброс данных
	def ResetRulesByType(self):
		""" Сброс правил обработки данных """
		idos: list[str] = self.rules.IdosByType(self._processing_type)

		if not idos: return
		if not RequestConfirm("Сброс правил обработки данных", f"Правил обработки данных: {len(idos)}"): return

		dialog_progress = QProgressDialog(self)
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setMaximum(len(idos))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.setWindowTitle("Сброс правил обработки данных")

		for index_ido, ido in enumerate(idos):
			dialog_progress.setLabelText(f"Ожидает обработки: {dialog_progress.maximum() - dialog_progress.value()}")
			dialog_progress.setValue(index_ido + 1)

			record = C90_ProcessingRulesRecord(ido)
			record.DeleteObject(CONTAINER_LOCAL)

		dialog_progress.setValue(dialog_progress.maximum())

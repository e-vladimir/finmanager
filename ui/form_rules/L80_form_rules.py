# ФОРМА ПРАВИЛ ОБРАБОТКИ: ЛОГИКА ДАННЫХ

from L00_containers       import CONTAINER_LOCAL
from L00_rules_types      import *

from L20_PySide6          import RequestText, RequestMultipleText, RequestConfirm
from L70_form_rules       import C70_FormRules
from L90_findescription   import C90_RecordFindescription
from L90_processing_rules import C90_RecordProcessingRules


class C80_FormRules(C70_FormRules):
	""" Форма правил обработки: Логика данных """

	# Данные
	def ShowData(self):
		""" Загрузка данных """
		if not self.isVisible(): return

		self.SetupModelData()

		if   self._type_processing == RULE_REPLACE_TEXT                 :
			for self._ido_processing in self.rules.IdosByType(RULE_REPLACE_TEXT): self.LoadRecordReplaceText()

		elif self._type_processing == RULE_DETECT_FINDESCRIPTION_BY_TEXT:
			for self._ido_processing in self.findescription.SubIdos()                            : self.LoadRecordFindescription()
			for self._ido_processing in self.rules.IdosByType(RULE_DETECT_FINDESCRIPTION_BY_TEXT): self.LoadRecordDetectFindescriptionByText()

	# Дерево данных
	def ProcessingTreeDataDbClick(self):
		""" Обработка двойного клика по дереву данных """
		if   self._type_processing == RULE_REPLACE_TEXT:
			if   self._column_processing == 0: self.on_RequestEditInputForReplaceText()
			elif self._column_processing == 1: self.on_RequestEditOutputForReplaceText()

		elif self._type_processing == RULE_DETECT_FINDESCRIPTION_BY_TEXT:
			self.on_RequestEditInputForDetectFindescription()

	# Правила замены текстовых фрагментов
	def CreateRecordReplaceText(self):
		""" Создание записи правил замены текстовых фрагментов """
		options_output : str | None = RequestText("Правила замены текстовых фрагментов", "Создание правила замены текстовых фрагментов.\n\nФрагмент для замены")
		if options_output is None: return

		record_rules = C90_RecordProcessingRules()
		record_rules.GenerateIdo()
		record_rules.RegisterObject(CONTAINER_LOCAL)

		record_rules.OptionsOutputAsString(options_output)
		record_rules.Type(RULE_REPLACE_TEXT)

		self._ido_processing = record_rules.Ido().data

		self.on_RecordReplaceTextCreated()

	def EditInputForRecordReplaceText(self):
		""" Редактирование записи правил замены текстовых фрагментов """
		if not self._ido_processing : return

		record_rule               = C90_RecordProcessingRules(self._ido_processing)

		input_options : list[str] | None = RequestMultipleText("Запись правил замены текстовых фрагментов", f"Фрагмент замены: {record_rule.OptionsOutputAsString()}", record_rule.OptionsInputAsStrings())
		if     input_options is None: return

		record_rule.OptionsInputAsStrings(input_options)

		self.on_RecordReplaceTextChanged()

	def EditOutputForRecordReplaceText(self):
		""" Редактирование записи правил замены текстовых фрагментов """
		if not self._ido_processing : return

		record_rule                 = C90_RecordProcessingRules(self._ido_processing)

		output_options : str | None = RequestText("Запись правил замены текстовых фрагментов", "Фрагменты поиска:\n" + '\n'.join(record_rule.OptionsInputAsStrings()), record_rule.OptionsOutputAsString())
		if     output_options is None: return

		record_rule.OptionsOutputAsString(output_options)

		self.on_RecordReplaceTextChanged()

	def DeleteRecordReplaceText(self):
		""" Удаление записи правил замены текстовых фрагментов """
		if not self._ido_processing: return

		record_rule = C90_RecordProcessingRules(self._ido_processing)

		if not RequestConfirm("Запись правил замены текстовых фрагментов", f"Удаление записи для фрагмента: {record_rule.OptionsOutputAsString()}"): return

		record_rule.DeleteObject(CONTAINER_LOCAL)

		self.on_RecordReplaceTextDeleted()

	# Правила определения финструктуры по текстовым фрагментам
	def EditInputForRecordDetectFindescription(self):
		""" Редактирование параметров записи правил """
		if not self._name_processing: return

		if not self._ido_processing :
			record_findescription           = C90_RecordFindescription()
			if not record_findescription.SwitchByName(self._name_processing): return

			record_rules                     = C90_RecordProcessingRules()
			record_rules.GenerateIdo()
			record_rules.RegisterObject(CONTAINER_LOCAL)

			record_rules.OptionsOutputAsString(record_findescription.Ido().data)
			record_rules.Type(RULE_DETECT_FINDESCRIPTION_BY_TEXT)

			self._ido_processing = record_rules.Ido().data

		if not self._ido_processing : return

		record_rule                      = C90_RecordProcessingRules(self._ido_processing)

		input_options : list[str] | None = RequestMultipleText("Запись правил определения финсостава по текстовым фрагментам", f"Финсостав: {self._name_processing}", record_rule.OptionsInputAsStrings())
		if     input_options is None: return

		record_rule.OptionsInputAsStrings(input_options)

		self.on_RecordDetectFindescriptionChanged()

	def DeleteRecordDetectFindescription(self):
		""" Удаление записи правил определения финсостава по текстовым фрагментам """
		if not self._ido_processing: return

		record_rule = C90_RecordProcessingRules(self._ido_processing)

		if not RequestConfirm("Запись правил определения финсостава по текстовым фрагментам", f"Удаление записи для финсостава: {self._name_processing}"): return

		record_rule.DeleteObject(CONTAINER_LOCAL)

		self.on_RecordDetectFindescriptionDeleted()

	def WrapSubRecordsDetectFindescription(self):
		""" Свёртка фрагментов поиска для записи определения финсостава """
		if not self._name_processing: return

		record_findescription              = C90_RecordFindescription()
		if not record_findescription.SwitchByName(self._name_processing): return

		options_input          : list[str] = []
		findescription_subidos : list      = record_findescription.SubIdos(True)

		for rule_ido in self.rules.IdosByType(RULE_DETECT_FINDESCRIPTION_BY_TEXT):
			record_rule = C90_RecordProcessingRules(rule_ido)

			if record_rule.OptionsOutputAsString() not in findescription_subidos: continue

			options_input.extend(record_rule.OptionsInputAsStrings())

		if not self._ido_processing:
			record_rule = C90_RecordProcessingRules()
			record_rule.GenerateIdo()
			record_rule.RegisterObject(CONTAINER_LOCAL)

			record_rule.Type(RULE_DETECT_FINDESCRIPTION_BY_TEXT)
			record_rule.OptionsOutputAsString(record_findescription.Ido().data)

			self._ido_processing = record_rule.Ido().data

		else                       :
			record_rule = C90_RecordProcessingRules(self._ido_processing)

		record_rule.OptionsInputAsStrings(list(set(options_input)))

		self.on_RecordDetectFindescriptionChanged()

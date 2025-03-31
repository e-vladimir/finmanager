# ФОРМА ОБРАБОТКА ДАННЫХ: ЛОГИКА ДАННЫХ
# 22 мар 2025

from PySide6.QtCore      import Qt
from PySide6.QtWidgets   import QProgressDialog

from G10_list import ClearList
from L00_containers      import CONTAINERS
from L00_form_processing import OBJECTS_TYPE, PROCESSING_FIELDS
from L00_rules           import RULES
from L20_PySide6         import RequestConfirm, RequestMultipleText, RequestText
from L70_form_processing import C70_FormProcessing
from L90_operations      import C90_Operation
from L90_rules           import C90_ProcessingRule


class C80_FormProcessing(C70_FormProcessing):
	""" Форма Обработка данных: Логика данных """

	# Параметры ручной обработки
	def EditOptionsManual(self):
		match self.processing_field:
			case PROCESSING_FIELDS.DESCRIPTION_ADD    : self.SetManualDescriptionAdd()
			case PROCESSING_FIELDS.DESCRIPTION_INCLUDE: self.SetManualDescriptionInclude()
			case PROCESSING_FIELDS.DESCRIPTION_EXCLUDE: self.SetManualDescriptionExclude()
			case PROCESSING_FIELDS.DESCRIPTION_REPLACE: self.SetManualDescriptionReplace()
			case PROCESSING_FIELDS.DESCRIPTION_SET    : self.SetManualDescriptionSet()
			case PROCESSING_FIELDS.LABELS_ADD         : self.SetManualLabelsAdd()
			case PROCESSING_FIELDS.LABELS_EXCLUDE     : self.SetManualLabelsExclude()
			case PROCESSING_FIELDS.LABELS_INCLUDE     : self.SetManualLabelsInclude()
			case PROCESSING_FIELDS.LABELS_REMOVE      : self.SetManualLabelsRemove()
			case PROCESSING_FIELDS.LABELS_REPLACE     : self.SetManualLabelsReplace()

	# Ручная обработка
	def ManualProcessingOperations(self):
		""" Выполнение ручной обработки данных операций """
		dy, dm           = self.Workspace.DyDm()
		idos : list[str] = self.Operations.Idos(dy, dm)

		dialog_import    = QProgressDialog(self)
		dialog_import.setWindowTitle("Обработка операций")
		dialog_import.setMaximum(len(idos))
		dialog_import.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_import.setLabelText(f"Осталось обработать операций: {dialog_import.maximum()}")
		dialog_import.setMinimumWidth(480)
		dialog_import.forceShow()

		for index_data, ido in enumerate(idos):
			dialog_import.setValue(index_data + 1)
			dialog_import.setLabelText(f"Осталось обработать операций: {dialog_import.maximum() - dialog_import.value()}")

			operation               = C90_Operation(ido)
			description : str       = operation.description.lower()
			labels      : set[str]  = set(label.lower() for label in operation.labels)

			flag_skip   : bool      = True

			if self._manual_description_include.enable:
				flag_skip &= not any([item.lower()  in description for item  in self._manual_description_include.data])

			if self._manual_description_exclude.enable:
				flag_skip |=     any([item.lower()  in description for item  in self._manual_description_exclude.data])

			if self._manual_labels_include.enable:
				flag_skip &= not any([label.lower() in labels      for label in self._manual_labels_include.data])

			if self._manual_labels_exclude.enable:
				flag_skip |=     any([label.lower() in labels      for label in self._manual_labels_exclude.data])

			if flag_skip: continue

			description             = operation.description
			labels      : set[str]  = set(operation.labels)

			if self._manual_description_replace.enable and self._manual_description_include.enable:
				for src in self._manual_description_include.data:
					description = description.replace(src, self._manual_description_replace.data)

			if self._manual_description_set.enable:
				description = self._manual_description_set.data

			if self._manual_description_add.enable:
				description += self._manual_description_add.data

			if self._manual_labels_add.enable:
				labels.update(self._manual_labels_add.data)

			if self._manual_labels_replace.enable and self._manual_labels_include.enable:
				for src in self._manual_labels_include.data:
					if src not in labels: continue

					labels.remove(src)
					labels.add(self._manual_labels_replace.data)

			if self._manual_labels_remove.enable:
				labels.difference_update(self._manual_labels_remove.data)

			operation.description = description
			operation.labels      = list(labels)

	def ManualProcessing(self):
		""" Выполнение ручной обработки данных """
		match self.processing_objects_type:
			case OBJECTS_TYPE.OPERATIONS: self.ManualProcessingOperations()

	# Автоматическая обработка
	def LoadRules(self):
		""" Загрузка данных в модель автоматической обработки """
		for self.processing_ido in self.ProcessingRules.Idos(self.processing_rules_type):
			match self.processing_rules_type:
				case RULES.REPLACE_DESCRIPTION:	self.LoadRuleReplaceDescriptionInModel()

	def CreateRule(self):
		""" Создание правила автоматической обработки """
		rule = C90_ProcessingRule()
		rule.GenerateIdo()
		rule.RegisterObject(CONTAINERS.DISK)

		rule.rules_type = self.processing_rules_type

		self.processing_ido = rule.Ido().data

		self.on_RuleCreated()

	def DeleteRule(self):
		""" Удаление правила автоматической обработки """
		rule              = C90_ProcessingRule(self.processing_ido)

		text_input  : str = ""
		text_output : str = ""

		match self.processing_rules_type:
			case RULES.REPLACE_DESCRIPTION:
				text_input  = "Поиск\n"  + ', '.join(rule.inputs)[:30]
				text_output = "Замена\n" + ', '.join(rule.outputs)[:30]

		if not RequestConfirm("Удаление правила автоматической обработки", f"Тип правила: {self.processing_rules_type}\n\n{text_input}\n\n{text_output}"): return

		rule.DeleteObject(CONTAINERS.DISK)

		self.on_RuleDeleted()

	def EditRule(self):
		""" Редактирование правила автоматической обработки """
		rule       = C90_ProcessingRule()
		idp_input  = rule.FInput.Idp().data
		idp_output = rule.FOutput.Idp().data
		idp_block  = rule.FBlock.Idp().data

		if   self.processing_idp == idp_input : self.EditRuleInput()
		elif self.processing_idp == idp_output: self.EditRuleOutput()
		elif self.processing_idp == idp_block : self.EditRuleBlock()

	def EditRuleInput(self):
		""" Редактирование параметра input для правила автоматической обработки """
		rule       = C90_ProcessingRule(self.processing_ido)

		match rule.rules_type:
			case RULES.REPLACE_DESCRIPTION:
				inputs : list[str] | None = RequestMultipleText( "Редактирование правила автоматической обработки",
				                                                f"{', '.join(rule.inputs)}\n"
				                                                f"замена на\n"
				                                                f"{rule.output}",
				                                                rule.inputs,
				                                                self.Operations.Descriptions())
				if inputs is None: return

				rule.inputs = ClearList(inputs, clear_simbols=False)

				self.on_RuleChanged()

	def EditRuleOutput(self):
		""" Редактирование параметра output для правила автоматической обработки """
		rule       = C90_ProcessingRule(self.processing_ido)

		match rule.rules_type:
			case RULES.REPLACE_DESCRIPTION:
				output : str | None = RequestText( "Редактирование правила автоматической обработки",
                                                  f"{', '.join(rule.inputs)}\n"
                                                  f"замена на\n"
                                                  f"{rule.output}",
                                                  rule.output,
                                                  self.Operations.Descriptions())
				if output is None: return

				rule.output = output

				self.on_RuleChanged()

	def EditRuleBlock(self):
		""" Редактирование параметра block для правила автоматической обработки """
		rule       = C90_ProcessingRule(self.processing_ido)

		match rule.rules_type:
			case RULES.REPLACE_DESCRIPTION:
				blocks : list[str] | None = RequestMultipleText( "Редактирование правила автоматической обработки",
				                                                f"{', '.join(rule.inputs)}\n"
				                                                f"замена на\n"
				                                                f"{rule.output}\n\nПризнаки пропуска:",
				                                                rule.blocks,
				                                                self.Operations.Descriptions())
				if blocks is None: return

				rule.blocks = ClearList(blocks, clear_simbols=False)

				self.on_RuleChanged()

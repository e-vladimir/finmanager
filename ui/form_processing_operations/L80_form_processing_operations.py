# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: ЛОГИКА ДАННЫХ

from PySide6.QtCore                 import Qt
from PySide6.QtWidgets              import QProgressDialog

from L00_containers                 import CONTAINERS
from L00_rules                      import RULES

from L20_PySide6                    import RequestConfirm, RequestText
from L70_form_processing_operations import C70_FormProcessingOperations
from L90_operations                 import C90_Operation, C90_Operations
from L90_rules                      import C90_ProcessingRule


class C80_FormProcessingOperations(C70_FormProcessingOperations):
	""" Форма Обработка операций: Логика данных """

	# Форма
	def UpdateDataPartial(self):
		""" Частичное обновление данных """
		self.ReadProcessingIdoFromWorkspace()
		self.LoadRuleToModel()

		self.AdjustTableRules_Size()

	# Правила обработки
	def ShowRules(self):
		""" Отображение правил обработки """
		for self._processing_ido in self.rules.IdosByType(self._processing_rule_types, True): self.LoadRuleToModel()

	def ApplyRules(self):
		""" Применение правил обработки """
		dy, dm           = self.workspace.DyDm()
		operations       = C90_Operations()

		idos : list[str] = operations.OperationsIdosInDyDmDd(dy, dm)

		dialog_progress  = QProgressDialog(self)
		dialog_progress.setWindowTitle("Обработка операций")
		dialog_progress.setMaximum(len(idos))
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum()} записей")
		dialog_progress.setMinimumWidth(480)
		dialog_progress.forceShow()

		for ido in idos:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum() - dialog_progress.value()} записей")

			operation = C90_Operation(ido)

			match self._processing_rule_types:
				case RULES.REPLACE_DESCRIPTION: operation.ApplyAutoreplaceDescription()
				case RULES.MATCH_DESTINATION  : operation.ApplyMatchDestination()
				case RULES.DETECT_LABEL       : operation.ApplyDetectLabels()

		dialog_progress.close()

	# Правило обработки
	def CreateRule(self):
		""" Создание правила обработки """
		rule = C90_ProcessingRule()
		rule.GenerateIdo()
		rule.RegisterObject(CONTAINERS.DISK)

		rule.RuleType(self._processing_rule_types)

		self.workspace.IdoRule(rule.Ido().data)

	def DeleteRule(self):
		""" Удаление правила обработки """
		rule = C90_ProcessingRule(self._processing_ido)

		if not RequestConfirm("Правило обработки", f"Удаление правила обработки.\n\n{'\n'.join(rule.OutputAsStrings())}"): return

		rule.DeleteObject(CONTAINERS.DISK)

	# Инструменты обработки описания
	def EditToolsDescriptionInclude(self):
		""" Редактирование обработки описания: Содержит """
		text : str | None = RequestText("Обработка описания", "Описание содержит:", self._tools_description_include)
		if text is None: return

		self._tools_description_include = text

	def EditToolsDescriptionApplies(self):
		""" Редактирование обработки описания: Применяется """
		text : str | None = RequestText("Обработка описания", "Применяется:", self._tools_description_applies)
		if text is None: return

		self._tools_description_applies = text

	def ProcessingDescription(self):
		""" Обработка описания """
		dy, dm           = self.workspace.DyDm()
		operations       = C90_Operations()

		idos : list[str] = operations.OperationsIdosInDyDmDd(dy, dm)

		dialog_progress  = QProgressDialog(self)
		dialog_progress.setWindowTitle("Обработка описания")
		dialog_progress.setMaximum(len(idos))
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum()} записей")
		dialog_progress.setMinimumWidth(480)
		dialog_progress.forceShow()

		for ido in idos:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum() - dialog_progress.value()} записей")

			operation         = C90_Operation(ido)
			description : str = operation.Description().replace(self._tools_description_include, self._tools_description_applies)
			operation.Description(description)

		dialog_progress.close()

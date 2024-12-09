# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: ЛОГИКА ДАННЫХ

from PySide6.QtCore                 import Qt
from PySide6.QtWidgets              import QProgressDialog

from L00_containers                 import CONTAINERS
from L00_form_processing_operations import SUBJECTS
from L00_rules                      import RULES

from L20_PySide6                    import RequestConfirm
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
		match self._processing_subject:
			case SUBJECTS.DESCRIPTION:
				for self._processing_ido in self.rules.IdosByType(RULES.REPLACE_DESCRIPTION): self.LoadRuleToModel()

			case SUBJECTS.DESTINATION:
				for self._processing_ido in self.rules.IdosByType(RULES.MATCH_DESTINATION)  : self.LoadRuleToModel()

			case SUBJECTS.LABELS     :
				for self._processing_ido in self.rules.IdosByType(RULES.DETECT_LABEL)       : self.LoadRuleToModel()

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

			match self._processing_subject:
				case SUBJECTS.DESCRIPTION: operation.ApplyAutoreplaceDescription()
				case SUBJECTS.DESTINATION: operation.ApplyMatchDestination()
				case SUBJECTS.LABELS     : operation.ApplyDetectLabels()

		dialog_progress.close()

	# Правило обработки
	def CreateRule(self):
		""" Создание правила обработки """
		rule = C90_ProcessingRule()
		rule.GenerateIdo()
		rule.RegisterObject(CONTAINERS.DISK)

		match self._processing_subject:
			case SUBJECTS.DESCRIPTION: rule.RuleType(RULES.REPLACE_DESCRIPTION)
			case SUBJECTS.DESTINATION: rule.RuleType(RULES.MATCH_DESTINATION)
			case SUBJECTS.LABELS     : rule.RuleType(RULES.DETECT_LABEL)

		self.workspace.IdoRule(rule.Ido().data)

	def DeleteRule(self):
		""" Удаление правила обработки """
		rule = C90_ProcessingRule(self._processing_ido)

		if not RequestConfirm("Правило обработки", f"Удаление правила обработки.\n\n{'\n'.join(rule.OutputAsStrings())}"): return

		rule.DeleteObject(CONTAINERS.DISK)

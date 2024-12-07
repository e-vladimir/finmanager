# ФОРМА УПРАВЛЕНИЕ НАЗНАЧЕНИЕМ: ЛОГИКА ДАННЫХ

from PySide6.QtCore               import  Qt
from PySide6.QtWidgets            import  QProgressDialog

from L00_containers               import  CONTAINERS
from L00_rules                    import  RULES

from L20_PySide6                  import (RequestConfirm,
                                          RequestMultipleText,
                                          RequestText,
                                          ShowMessage)
from L70_form_control_destination import  C70_FormControlDestination
from L90_operations               import  C90_Operation, C90_Operations
from L90_rules                    import  C90_ProcessingRule


class C80_FormControlDestination(C70_FormControlDestination):
	""" Форма Управление назначением: Логика данных """

	# Правила сопоставления назначения
	def ShowRules(self):
		""" Отображение правил сопоставления назначения """
		for self._processing_ido in self.rules.IdosByType(RULES.MATCH_DESTINATION): self.LoadRuleInModel()

	def ApplyRules(self):
		""" Применение правил сопоставления назначения """
		operations       = C90_Operations()
		dy, dm           = self.workspace.DyDm()
		idos : list[str] = operations.OperationsIdosInDyDmDd(dy, dm)

		dialog_progress  = QProgressDialog(self)
		dialog_progress.setWindowTitle("Финансовые операции: Применение правил сопоставления назначения")
		dialog_progress.setLabelText("Осталось обработать: --")
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setMaximum(len(idos))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.forceShow()

		for ido in idos:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum() - dialog_progress.value()}")

			operation = C90_Operation(ido)
			operation.ApplyMatchDestination()

		dialog_progress.close()

		ShowMessage("Применение правил сопоставления назначения", "Выполнено")

	# Правило сопоставления назначения
	def CreateRule(self):
		""" Создание правила сопоставления назначения """
		text_output : str | None = RequestText("Правило сопоставления назначения", "Создание правила сопоставления назначения", "")
		if text_output is None: return

		rule                     = C90_ProcessingRule()
		rule.GenerateIdo()
		rule.RegisterObject(CONTAINERS.DISK)

		rule.RuleType(RULES.REPLACE_DESCRIPTION)

		rule.OutputAsString(text_output)

		self._processing_ido = rule.Ido().data

	def DeleteRule(self):
		""" Удаление правила """
		rule = C90_ProcessingRule(self._processing_ido)

		if not RequestConfirm("Правило сопоставления назначения", f"Удаление правила сопоставления назначения.\n\nФрагменты поиска:{', '.join(rule.InputAsString())}\n\nНазначение: {rule.OutputAsString()}"): return

		rule.DeleteObject(CONTAINERS.DISK)

	def EditRuleInput(self):
		""" Редактирование входа правила """
		rule                     = C90_ProcessingRule(self._processing_ido)

		texts : list[str] | None = RequestMultipleText("Правило сопоставления назначения", f"Назначение: {rule.OutputAsString()}\n\nФрагмент поиска:", rule.InputAsStrings())
		if texts is None: return

		rule.InputAsStrings(texts)

	def EditRuleOutput(self):
		""" Редактирование выхода правила """
		rule              = C90_ProcessingRule(self._processing_ido)

		text : str | None = RequestText("Правило сопоставления назначения", f"Фрагменты поиска:\n{'\n'.join(rule.InputAsStrings())}\n\nНазначение:", rule.OutputAsString())
		if text is None: return

		rule.OutputAsString(text)

	# Поиск и замена
	def ExecReplace(self):
		""" Выполнение поиска и замены """
		data_inputs : list[str] = self.edit_control_replace_input.toPlainText().split('\n')
		data_output : str       = self.edit_control_replace_output.text()

		operations              = C90_Operations()
		dy, dm                  = self.workspace.DyDm()
		idos : list[str]        = operations.OperationsIdosInDyDmDd(dy, dm)

		dialog_progress         = QProgressDialog(self)
		dialog_progress.setWindowTitle("Финансовые операции: Поиск и замена")
		dialog_progress.setLabelText("Осталось обработать: --")
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setMaximum(len(idos))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.forceShow()

		for ido in idos:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum() - dialog_progress.value()}")

			operation         = C90_Operation(ido)

			destination : str = operation.Destination()

			for data_input in sorted(data_inputs, key=len):
				destination = destination.replace(data_input, data_output)

			operation.Destination(destination)

		dialog_progress.close()

		ShowMessage("Поиск и замена", "Выполнено")

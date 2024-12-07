# ФОРМА УПРАВЛЕНИЕ ОПИСАНИЕМ: ЛОГИКА ДАННЫХ

from PySide6.QtCore               import  Qt
from PySide6.QtWidgets            import  QProgressDialog

from L00_containers               import  CONTAINERS
from L00_rules                    import  RULES

from L20_PySide6 import (RequestConfirm,
                         RequestMultipleText,
                         RequestText, ShowMessage)
from L70_form_control_description import  C70_FormControlDescription
from L90_operations               import  C90_Operation, C90_Operations
from L90_rules                    import  C90_ProcessingRule


class C80_FormControlDescription(C70_FormControlDescription):
	""" Форма Управление описанием: Логика данных """

	# Правила автозамены описания
	def ShowRules(self):
		""" Отображение правил автозамены описания """
		for self._processing_ido in self.rules.IdosByType(RULES.REPLACE_DESCRIPTION): self.LoadRuleInModel()

	def ApplyRules(self):
		""" Применение правил автозамены описания """
		operations       = C90_Operations()
		dy, dm           = self.workspace.DyDm()
		idos : list[str] = operations.OperationsIdosInDyDmDd(dy, dm)

		dialog_progress  = QProgressDialog(self)
		dialog_progress.setWindowTitle("Финансовые операции: Применение правил автозамены описания")
		dialog_progress.setLabelText("Осталось обработать: --")
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setMaximum(len(idos))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.forceShow()

		for ido in idos:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum() - dialog_progress.value()}")

			operation = C90_Operation(ido)
			operation.ApplyAutoreplaceDescription()

		dialog_progress.close()

		ShowMessage("Применение правил автозамены описания", "Выполнено")

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

	def ApplyRule(self):
		""" Применение правил автозамены описания """
		rule             = C90_ProcessingRule(self._processing_ido)
		data_inputs : list[str] = rule.InputAsStrings()
		data_output : str       = rule.OutputAsString()

		operations       = C90_Operations()
		dy, dm           = self.workspace.DyDm()
		idos : list[str] = operations.OperationsIdosInDyDmDd(dy, dm)

		dialog_progress  = QProgressDialog(self)
		dialog_progress.setWindowTitle("Финансовые операции: Применение правил автозамены описания")
		dialog_progress.setLabelText("Осталось обработать: --")
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setMaximum(len(idos))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.forceShow()

		for ido in idos:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum() - dialog_progress.value()}")

			operation         = C90_Operation(ido)

			description : str = operation.Description()

			for data_input in sorted(data_inputs, key=len):
				description = description.replace(data_input, data_output)

			operation.Description(description)

		dialog_progress.close()

		ShowMessage("Применение правила автозамены описания", "Выполнено")

	# Поиск и замена
	def ExecReplace(self):
		""" Выполнение поиска и замены """
		data_inputs : list[str] = self.edit_control_replace_input.toPlainText().split('\n')
		data_output : str       = self.edit_control_replace_output.text()

		operations       = C90_Operations()
		dy, dm           = self.workspace.DyDm()
		idos : list[str] = operations.OperationsIdosInDyDmDd(dy, dm)

		dialog_progress  = QProgressDialog(self)
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

			description : str = operation.Description()

			for data_input in sorted(data_inputs, key=len):
				description = description.replace(data_input, data_output)

			operation.Description(description)

		dialog_progress.close()

		ShowMessage("Поиск и замена", "Выполнено")

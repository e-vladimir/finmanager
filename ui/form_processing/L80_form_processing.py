# ФОРМА ОБРАБОТКА ДАННЫХ: ЛОГИКА ДАННЫХ
# 22 мар 2025

from PySide6.QtCore      import Qt
from PySide6.QtWidgets   import QProgressDialog

from L70_form_processing import C70_FormProcessing
from L90_operations      import C90_Operation


class C80_FormProcessing(C70_FormProcessing):
	""" Форма Обработка данных: Логика данных """

	# Обработка данных
	def ProcessingOperations(self):
		""" Обработка операций """
		dy, dm           = self.Workspace.DyDm()
		idos : list[str] = self.Operations.Idos(dy, dm)

		dialog_import    = QProgressDialog(self)
		dialog_import.setWindowTitle("Обработка операций")
		dialog_import.setMaximum(len(idos))
		dialog_import.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_import.setLabelText(f"Осталось обработать операций: {dialog_import.maximum()}")
		dialog_import.setMinimumWidth(480)
		dialog_import.forceShow()

		for idx_ido, ido in enumerate(idos):
			dialog_import.setValue(idx_ido + 1)
			dialog_import.setLabelText(f"Осталось обработать операций: {dialog_import.maximum() - dialog_import.value()}")

			operation        = C90_Operation(ido)

			flag_processing : bool = False

			if self._operations_filter_description.enable:
				flag_processing |= self.operations_filter_description in operation.description

			if not flag_processing: continue

			if self._operations_processing_replace_description.enable:
				operation.description = operation.description.replace(self.operations_filter_description, self.operations_processing_replace_description)

			if self._operations_processing_set_description.enable:
				operation.description = self.operations_processing_set_description

			if self._operations_processing_set_color.enable:
				operation.color = self.operations_processing_set_color

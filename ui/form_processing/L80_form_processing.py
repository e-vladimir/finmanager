# ФОРМА ОБРАБОТКА ДАННЫХ: ЛОГИКА ДАННЫХ
# 22 мар 2025

from PySide6.QtCore      import Qt
from PySide6.QtWidgets   import QProgressDialog

from L00_form_processing import OBJECTS_TYPE, PROCESSING_FIELDS
from L70_form_processing import C70_FormProcessing
from L90_operations      import C90_Operation


class C80_FormProcessing(C70_FormProcessing):
	""" Форма Обработка данных: Логика данных """

	# Параметры ручной обработки данных
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

	# Ручная обработка данных
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
			description : str       = operation.description
			labels      : set[str]  = set(operation.labels)

			flag_skip   : bool      = False

			if flag_skip: continue

			operation.description = description
			operation.labels      = list(labels)

	def ManualProcessing(self):
		""" Выполнение ручной обработки данных """
		match self.processing_objects_type:
			case OBJECTS_TYPE.OPERATIONS: self.ManualProcessingOperations()

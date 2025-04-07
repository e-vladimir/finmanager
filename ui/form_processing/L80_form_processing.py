# ФОРМА ОБРАБОТКА ДАННЫХ: ЛОГИКА ДАННЫХ
# 22 мар 2025

from PySide6.QtCore      import Qt
from PySide6.QtWidgets   import QProgressDialog

from L00_form_processing import OBJECTS_TYPE, PROCESSING_FIELDS
from L70_form_processing import C70_FormProcessing
from L90_operations      import C90_Operation


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

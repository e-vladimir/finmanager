# ФОРМА ОБРАБОТКА ДАННЫХ: ЛОГИКА ДАННЫХ
# 22 мар 2025

from PySide6.QtCore      import Qt
from PySide6.QtWidgets   import QProgressDialog

from L00_colors          import COLORS
from L00_form_processing import OBJECTS_TYPE, PROCESSING_FIELDS
from L70_form_processing import C70_FormProcessing
from L90_operations      import C90_Operation


class C80_FormProcessing(C70_FormProcessing):
	""" Форма Обработка данных: Логика данных """

	# Параметры ручной обработки
	def EditOptionsManual(self):
		match self.processing_field:
			case PROCESSING_FIELDS.DESCRIPTION_EXCLUDE: self.SetManualDescriptionExclude()
			case PROCESSING_FIELDS.DESCRIPTION_INCLUDE: self.SetManualDescriptionInclude()

			case PROCESSING_FIELDS.DESTINATION_ADD    : self.SetManualDestinationAdd()
			case PROCESSING_FIELDS.DESTINATION_EXCLUDE: self.SetManualDestinationExclude()
			case PROCESSING_FIELDS.DESTINATION_INCLUDE: self.SetManualDestinationInclude()
			case PROCESSING_FIELDS.DESTINATION_REPLACE: self.SetManualDestinationReplace()
			case PROCESSING_FIELDS.DESTINATION_SET    : self.SetManualDestinationSet()

			case PROCESSING_FIELDS.LABELS_ADD         : self.SetManualLabelsAdd()
			case PROCESSING_FIELDS.LABELS_EXCLUDE     : self.SetManualLabelsExclude()
			case PROCESSING_FIELDS.LABELS_INCLUDE     : self.SetManualLabelsInclude()
			case PROCESSING_FIELDS.LABELS_REMOVE      : self.SetManualLabelsRemove()
			case PROCESSING_FIELDS.LABELS_REPLACE     : self.SetManualLabelsReplace()

			case PROCESSING_FIELDS.COLOR_SET          : self.SetManualColorSet()

			case PROCESSING_FIELDS.SKIP_SET               : self.SwitchManualSkipSet()

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
			destination             = operation.destination.lower()
			labels      : set[str]  = set(label.lower() for label in operation.labels)

			flag_skip   : bool      = True

			if self._manual_description_include.enable:
				flag_skip &= not any([item.lower()  in description for item  in self._manual_description_include.data])

			if self._manual_description_exclude.enable:
				flag_skip |=     any([item.lower()  in description for item  in self._manual_description_exclude.data])

			if self._manual_destination_include.enable:
				flag_skip &= not any([item.lower()  in destination for item  in self._manual_destination_include.data])

			if self._manual_destination_exclude.enable:
				flag_skip |=     any([item.lower()  in destination for item  in self._manual_destination_exclude.data])

			if self._manual_labels_include.enable:
				flag_skip &= not any([label.lower() in labels      for label in self._manual_labels_include.data])

			if self._manual_labels_exclude.enable:
				flag_skip |=     any([label.lower() in labels      for label in self._manual_labels_exclude.data])

			if flag_skip: continue

			destination             = operation.destination
			labels      : set[str]  = set(operation.labels)

			if self._manual_destination_replace.enable and self._manual_destination_include.enable:
				for src in self._manual_destination_include.data:
					destination = destination.replace(src, self._manual_destination_replace.data)

			if self._manual_destination_set.enable:
				destination = self._manual_destination_set.data

			if self._manual_destination_add.enable:
				destination += self._manual_destination_add.data

			if self._manual_labels_add.enable:
				labels.update(self._manual_labels_add.data)

			if self._manual_labels_replace.enable and self._manual_labels_include.enable:
				for src in self._manual_labels_include.data:
					if src not in labels: continue

					labels.remove(src)
					labels.add(self._manual_labels_replace.data)

			if self._manual_labels_remove.enable:
				labels.difference_update(self._manual_labels_remove.data)

			if self._manual_color_set.enable:
				operation.color = COLORS(self._manual_color_set.data)

			operation.destination = destination
			operation.labels      = list(labels)

	def ManualProcessing(self):
		""" Выполнение ручной обработки данных """
		match self.processing_objects_type:
			case OBJECTS_TYPE.OPERATIONS: self.ManualProcessingOperations()

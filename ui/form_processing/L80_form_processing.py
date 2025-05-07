# ФОРМА ОБРАБОТКА ДАННЫХ: ЛОГИКА ДАННЫХ
# 22 мар 2025

from PySide6.QtCore      import Qt
from PySide6.QtWidgets   import QProgressDialog

from L00_colors          import COLORS
from L00_form_processing import OBJECTS_TYPE, PROCESSING_FIELDS
from L00_operations      import OPERATIONS
from L70_form_processing import C70_FormProcessing
from L90_operations      import C90_Operation


class C80_FormProcessing(C70_FormProcessing):
	""" Форма Обработка данных: Логика данных """

	# Параметры ручной обработки
	def EditOptionsManual(self):
		match self.processing_field:
			case PROCESSING_FIELDS.SRC_DESCRIPTION_EXCLUDE: self.SetManualSrcDescriptionExclude()
			case PROCESSING_FIELDS.SRC_DESCRIPTION_INCLUDE: self.SetManualSrcDescriptionInclude()

			case PROCESSING_FIELDS.DESCRIPTION_ADD        : self.SetManualDescriptionAdd()
			case PROCESSING_FIELDS.DESCRIPTION_EXCLUDE    : self.SetManualDescriptionExclude()
			case PROCESSING_FIELDS.DESCRIPTION_INCLUDE    : self.SetManualDescriptionInclude()
			case PROCESSING_FIELDS.DESCRIPTION_REPLACE    : self.SetManualDescriptionReplace()
			case PROCESSING_FIELDS.DESCRIPTION_SET        : self.SetManualDescriptionSet()

			case PROCESSING_FIELDS.COLOR_SET              : self.SetManualColorSet()

			case PROCESSING_FIELDS.SKIP_SET               : self.SwitchManualSkipSet()

	# Ручная обработка
	def ManualProcessingOperations(self):
		""" Выполнение ручной обработки данных операций """
		dy, dm           = self.Workspace.DyDm()
		idos : list[str] = self.Operations.Idos(dy, dm, use_cache=True, type_operation=OPERATIONS.ALL)

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
			src_description : str   = operation.src_description.lower()
			description             = operation.description.lower()

			flag_skip       : bool  = True

			if self._manual_src_description_include.enable:
				flag_skip &= not any([item.lower() in src_description for item in self._manual_src_description_include.data])

			if self._manual_src_description_exclude.enable:
				flag_skip |=     any([item.lower() in src_description for item in self._manual_src_description_exclude.data])

			if self._manual_description_include.enable:
				flag_skip &= not any([item.lower() in description for item in self._manual_description_include.data])

			if self._manual_description_exclude.enable:
				flag_skip |=     any([item.lower() in description for item in self._manual_description_exclude.data])

			if self._manual_operations_all.enable:
				flag_skip  = False

			if flag_skip: continue

			description             = operation.description

			if self._manual_description_clear.enable:
				description = ""

			if self._manual_description_replace.enable and self._manual_description_include.enable:
				for src in self._manual_description_include.data:
					description = description.replace(src, self._manual_description_replace.data)

			if self._manual_description_set.enable:
				description  = self._manual_description_set.data

			if self._manual_description_add.enable:
				description += self._manual_description_add.data

			if self._manual_color_set.enable:
				operation.color = COLORS(self._manual_color_set.data)

			if self._manual_destination_clear.enable:
				operation.destination = []

			operation.description = description

			operation.Caching()

	def ManualProcessing(self):
		""" Выполнение ручной обработки данных """
		match self.processing_objects_type:
			case OBJECTS_TYPE.OPERATIONS: self.ManualProcessingOperations()

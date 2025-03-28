# ФОРМА ОБРАБОТКА ДАННЫХ: МОДЕЛЬ ДАННЫХ
# 22 мар 2025

from L00_form_processing import OBJECTS_TYPE, PROCESSING_FIELDS
from L20_PySide6         import C20_StandardItemModel
from L20_form_processing import T20_ProcessingItem
from L41_form_processing import C41_FormProcessing
from L90_operations      import C90_Operations
from L90_workspace       import C90_Workspace


class C42_FormProcessing(C41_FormProcessing):
	""" Форма Обработка данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_object_type     : OBJECTS_TYPE       = OBJECTS_TYPE.NONE
		self._processing_field           : PROCESSING_FIELDS  = PROCESSING_FIELDS.NONE

		self._manual_description_add     : T20_ProcessingItem = T20_ProcessingItem(False, "")
		self._manual_description_include : T20_ProcessingItem = T20_ProcessingItem(False, [])
		self._manual_description_exclude : T20_ProcessingItem = T20_ProcessingItem(False, [])
		self._manual_description_replace : T20_ProcessingItem = T20_ProcessingItem(False, "")
		self._manual_description_set     : T20_ProcessingItem = T20_ProcessingItem(False, "")

		self._manual_labels_add          : T20_ProcessingItem = T20_ProcessingItem(False, [])
		self._manual_labels_exclude      : T20_ProcessingItem = T20_ProcessingItem(False, [])
		self._manual_labels_include      : T20_ProcessingItem = T20_ProcessingItem(False, [])
		self._manual_labels_remove       : T20_ProcessingItem = T20_ProcessingItem(False, [])
		self._manual_labels_replace      : T20_ProcessingItem = T20_ProcessingItem(False, "")

		self._processing_ido             : str                = ""

	def Init_10(self):
		super().Init_10()

		self.ModelDataManual = C20_StandardItemModel()

		self.Operations      = C90_Operations()
		self.Workspace       = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.Workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.TreeDataManual.setModel(self.ModelDataManual)

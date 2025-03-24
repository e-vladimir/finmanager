# ФОРМА ОБРАБОТКА ДАННЫХ: МЕХАНИКА ДАННЫХ
# 22 мар 2025

from L00_form_processing import OBJECTS_TYPE
from L50_form_processing import C50_FormProcessing


class C60_FormProcessing(C50_FormProcessing):
	""" Форма Обработка данных: Механика данных """

	# Объект обработки данных
	@property
	def processing_objects_type(self) -> OBJECTS_TYPE:
		return self._processing_object_type

	@processing_objects_type.setter
	def processing_objects_type(self, objects_type: OBJECTS_TYPE):
		self._processing_object_type = objects_type

	def SwitchProcessingObjectsTypeToOperations(self):
		""" Смена типа объектов на операции """
		self.processing_objects_type = OBJECTS_TYPE.OPERATIONS

		self.on_ProcessingObjectsTypeChanged()

	def SwitchProcessingObjectsTypeToLabels(self):
		""" Смена типа объектов на метки """
		self.processing_objects_type = OBJECTS_TYPE.LABELS

		self.on_ProcessingObjectsTypeChanged()

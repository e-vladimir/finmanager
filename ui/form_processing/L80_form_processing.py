# ФОРМА ОБРАБОТКА ДАННЫХ: ЛОГИКА ДАННЫХ
# 22 мар 2025

from L00_form_processing import PROCESSING_FIELDS
from L70_form_processing import C70_FormProcessing


class C80_FormProcessing(C70_FormProcessing):
	""" Форма Обработка данных: Логика данных """

	# Параметры ручной обработки данных
	def EditOptionsManual(self):
		match self.processing_field:
			case PROCESSING_FIELDS.DESCRIPTION_INCLUDE: self.SetManualDescriptionInclude()
			case PROCESSING_FIELDS.DESCRIPTION_REPLACE: self.SetManualDescriptionReplace()
			case PROCESSING_FIELDS.DESCRIPTION_SET    : self.SetManualDescriptionSet()

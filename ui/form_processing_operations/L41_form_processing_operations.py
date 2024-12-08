# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: МОДЕЛЬ UI

from L20_PySide6                    import C20_PySideForm
from L40_form_processing_operations import Ui_frm_processing_operations


class C41_FormProcessingOperations(C20_PySideForm, Ui_frm_processing_operations):
	""" Форма Обработка операций: Модель UI """

	def InitUi(self): self.setupUi(self)

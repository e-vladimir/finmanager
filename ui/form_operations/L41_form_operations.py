# ФОРМА ОПЕРАЦИЙ ПО СЧЕТАМ: МОДЕЛЬ UI

from L20_PySide6         import C20_PySideForm
from L40_form_operations import Ui_frm_operations


class C41_FormOperations(C20_PySideForm, Ui_frm_operations):
	""" Форма Операции по счетам: Модель UI """

	def InitUi(self): self.setupUi(self)

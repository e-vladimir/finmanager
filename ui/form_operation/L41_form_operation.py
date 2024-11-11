# ФОРМА ФИНАНСОВАЯ ОПЕРАЦИЯ: МОДЕЛЬ UI

from L20_PySide6        import C20_PySideForm
from L40_form_operation import Ui_frm_operation


class C41_FormOperation(C20_PySideForm, Ui_frm_operation):
	""" Форма Финансовая операция: Модель UI """

	def InitUi(self): self.setupUi(self)

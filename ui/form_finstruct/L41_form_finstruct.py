# ФОРМА ФИНСТРУКТУРА: МОДЕЛЬ UI

from L20_PySide6 import C20_PySideForm
from L40_form_finstruct    import Ui_frm_finstruct


class C41_FormFinstruct(C20_PySideForm, Ui_frm_finstruct):
	""" Форма Финструктура: Модель UI """

	def InitUi(self): self.setupUi(self)

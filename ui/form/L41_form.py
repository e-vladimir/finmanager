# ФОРМА : МОДЕЛЬ UI

from L20_PySide6 import C20_PySideForm
from L40_form    import Ui_frm


class C41_Form(C20_PySideForm, Ui_frm):
	""" Форма : Модель UI """

	def InitUi(self): self.setupUi(self)

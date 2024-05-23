# ФОРМА СБРОС ДАННЫХ: МОДЕЛЬ UI

from L20_PySide6    import C20_PySideForm
from L40_form_reset import Ui_frm_reset


class C41_FormReset(C20_PySideForm, Ui_frm_reset):
	""" Форма Сброс данных: Модель UI """

	def InitUi(self): self.setupUi(self)

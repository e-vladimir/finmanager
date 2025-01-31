# ФОРМА АНАЛИТИКА: МОДЕЛЬ UI

from L20_PySide6 import C20_PySideForm
from L40_form_analytics    import Ui_frm_analytics


class C41_FormAnalytics(C20_PySideForm, Ui_frm_analytics):
	""" Форма Аналитика: Модель UI """

	def InitUi(self): self.setupUi(self)

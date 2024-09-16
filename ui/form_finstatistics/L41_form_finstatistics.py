# ФОРМА ФИНСТАТИСТИКА: МОДЕЛЬ UI

from L20_PySide6            import C20_PySideForm
from L40_form_finstatistics import Ui_form_finstatistics


class C41_FormFinstatistics(C20_PySideForm, Ui_form_finstatistics):
	""" Форма Финстатистика: Модель UI """

	def InitUi(self): self.setupUi(self)

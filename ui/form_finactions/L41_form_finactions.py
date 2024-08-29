# ФОРМА ФИНДЕЙСТВИЯ: МОДЕЛЬ UI

from L20_PySide6 import C20_PySideForm
from L40_form_finactions    import Ui_frm_finactions


class C41_FormFinactions(C20_PySideForm, Ui_frm_finactions):
	""" Форма Финдействия: Модель UI """

	def InitUi(self): self.setupUi(self)

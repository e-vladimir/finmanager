# ФОРМА ФИНСТАТИСТИКА: МОДЕЛЬ UI

from L20_PySide6           import C20_PySideForm
from L40_form_finstatistic import Ui_frm_finstatistic


class C41_FormFinstatistic(C20_PySideForm, Ui_frm_finstatistic):
	""" Форма Финстатистика: Модель UI """

	def InitUi(self): self.setupUi(self)

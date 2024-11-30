# ФОРМА УПРАВЛЕНИЕ АВТОЗАМЕНОЙ: МОДЕЛЬ UI

from L20_PySide6 import C20_PySideForm
from L40_form_control_autoreplace    import Ui_frm_control_autoreplace


class C41_FormControlAutoreplace(C20_PySideForm, Ui_frm_control_autoreplace):
	""" Форма Управление автозаменой: Модель UI """

	def InitUi(self): self.setupUi(self)

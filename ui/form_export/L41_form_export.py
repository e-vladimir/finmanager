# ФОРМА ЭКСПОРТА: МОДЕЛЬ UI

from L20_PySide6     import C20_PySideForm
from L40_form_export import Ui_frm_export


class C41_FormExport(C20_PySideForm, Ui_frm_export):
	""" Форма экспорта: Модель UI """

	def InitUi(self): self.setupUi(self)

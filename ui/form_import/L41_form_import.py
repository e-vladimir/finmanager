# ФОРМА ИМПОРТ ДАННЫХ: МОДЕЛЬ UI

from L20_PySide6     import C20_PySideForm
from L40_form_import import Ui_frm_import


class C41_FormImport(C20_PySideForm, Ui_frm_import):
	""" Форма Импорт данных: Модель UI """

	def InitUi(self): self.setupUi(self)

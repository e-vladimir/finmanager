# ФОРМА ИМПОРТ ДАННЫХ: МОДЕЛЬ UI
# 14 мар 2025

from L20_PySide6     import C20_PySideForm
from L40_form_import import Ui_form_import


class C41_FormImport(C20_PySideForm, Ui_form_import):
	""" Форма Импорт данных: Модель UI """

	def InitUi(self): self.setupUi(self)

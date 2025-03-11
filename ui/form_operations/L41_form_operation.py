# ФОРМА ОПЕРАЦИИ: МОДЕЛЬ UI
# 11 мар 2025

from L20_PySide6        import C20_PySideForm
from L40_form_operation import Ui_form_operations


class C41_FormOperation(C20_PySideForm, Ui_form_operations):
	""" Форма Операции: Модель UI """

	def InitUi(self): self.setupUi(self)

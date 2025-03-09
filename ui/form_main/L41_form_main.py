# ФОРМА ОСНОВНАЯ: МОДЕЛЬ UI
# 12 фев 2025

from L20_PySide6   import C20_PySideForm
from L40_form_main import Ui_FormMain


class C41_FormMain(C20_PySideForm, Ui_FormMain):
	""" Форма Основная: Модель UI """

	def InitUi(self): self.setupUi(self)

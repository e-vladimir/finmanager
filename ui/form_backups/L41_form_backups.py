# ФОРМА КОПИИ АРХИВА ДАННЫХ: МОДЕЛЬ UI
# 18 мар 2025

from L20_PySide6      import C20_PySideForm
from L40_form_backups import Ui_FormBackups


class C41_FormBackups(C20_PySideForm, Ui_FormBackups):
	""" Форма Копии архива данных: Модель UI """

	def InitUi(self): self.setupUi(self)

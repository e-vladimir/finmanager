# ФОРМА РЕЗЕРВНОЕ КОПИРОВАНИЕ: МОДЕЛЬ UI

from L20_PySide6     import C20_PySideForm
from L40_form_backup import Ui_form_backup


class C41_FormBackup(C20_PySideForm, Ui_form_backup):
	""" Форма Резервное копирование: Модель UI """

	def InitUi(self): self.setupUi(self)

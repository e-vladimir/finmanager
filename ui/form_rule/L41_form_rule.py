# ФОРМА ПРАВИЛО ОБРАБОТКИ ДАННЫХ: МОДЕЛЬ UI

from L20_PySide6   import C20_PySideForm
from L40_form_rule import Ui_frm_rule


class C41_FormRule(C20_PySideForm, Ui_frm_rule):
	""" Форма Правило обработки данных: Модель UI """

	def InitUi(self): self.setupUi(self)

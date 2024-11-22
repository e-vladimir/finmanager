# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МОДЕЛЬ UI

from L20_PySide6    import C20_PySideForm
from L40_form_rules import Ui_frm_rules


class C41_FormRules(C20_PySideForm, Ui_frm_rules):
	""" Форма Правила обработки данных: Модель UI """

	def InitUi(self): self.setupUi(self)

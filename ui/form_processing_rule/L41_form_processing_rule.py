# ФОРМА ПРАВИЛО ОБРАБОТКИ: МОДЕЛЬ UI

from L20_PySide6              import C20_PySideForm
from L40_form_processing_rule import Ui_frm_processing_rule


class C41_FormProcessingRule(C20_PySideForm, Ui_frm_processing_rule):
	""" Форма Правило обработки: Модель UI """

	def InitUi(self): self.setupUi(self)

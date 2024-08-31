# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: МОДЕЛЬ UI

from L20_PySide6                import C20_PySideForm
from L40_form_finactions_record import Ui_frm_finactions_record


class C41_FormFinactionsRecord(C20_PySideForm, Ui_frm_finactions_record):
	""" Форма Запись финдействий: Модель UI """

	def InitUi(self): self.setupUi(self)

# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: МОДЕЛЬ UI

from L20_PySide6                import C20_PySideForm
from L40_form_record_finactions import Ui_frm_record_finactions


class C41_FormRecordFinactions(C20_PySideForm, Ui_frm_record_finactions):
	""" Форма Запись финдействий: Модель UI """

	def InitUi(self): self.setupUi(self)

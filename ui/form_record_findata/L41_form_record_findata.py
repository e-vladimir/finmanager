# ФОРМА ЗАПИСИ ФИНДАННЫХ: МОДЕЛЬ UI

from L20_PySide6             import C20_PySideForm
from L40_form_record_findata import Ui_form_record_findata


class C41_FormRecordFindata(C20_PySideForm, Ui_form_record_findata):
	""" Форма записи финданных: Модель UI """

	def InitUi(self): self.setupUi(self)

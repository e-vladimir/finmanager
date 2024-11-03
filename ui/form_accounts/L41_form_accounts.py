# ФОРМА СЧЕТА: МОДЕЛЬ UI

from L20_PySide6       import C20_PySideForm
from L40_form_accounts import Ui_frm_accounts


class C41_FormAccounts(C20_PySideForm, Ui_frm_accounts):
	""" Форма Счета: Модель UI """

	def InitUi(self): self.setupUi(self)

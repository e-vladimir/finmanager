# ПРИЛОЖЕНИЕ: МОДЕЛЬ ДАННЫХ
# 12 фев 2025

from L20_PySide6       import C20_PySideApplication
from L90_form_accounts import C90_FormAccounts
from L90_form_main     import C90_FormMain


class C40_Application(C20_PySideApplication):
	""" Приложение: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.FormMain     = C90_FormMain(self)
		self.FormAccounts = C90_FormAccounts(self)

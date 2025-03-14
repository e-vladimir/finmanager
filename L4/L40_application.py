# ПРИЛОЖЕНИЕ: МОДЕЛЬ ДАННЫХ
# 12 фев 2025

from L20_PySide6        import C20_PySideApplication
from L90_form_accounts  import C90_FormAccounts
from L90_form_import    import C90_FormImport
from L90_form_main      import C90_FormMain
from L90_form_operation import C90_FormOperation


class C40_Application(C20_PySideApplication):
	""" Приложение: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.FormMain       = C90_FormMain(self)
		self.FormAccounts   = C90_FormAccounts(self)
		self.FormOperations = C90_FormOperation(self)
		self.FormImport     = C90_FormImport(self)

# ПРИЛОЖЕНИЕ: МОДЕЛЬ ДАННЫХ

from L20_PySide6         import C20_PySideApplication
from L90_form_accounts   import C90_FormAccounts
from L90_form_backups    import C90_FormArchives
from L90_form_main       import C90_FormMain
from L90_form_operations import C90_FormOperations


class C40_Application(C20_PySideApplication):
	""" Приложение: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.form_main       = C90_FormMain(self)
		self.form_archives   = C90_FormArchives(self)
		self.form_accounts   = C90_FormAccounts(self)
		self.form_operations = C90_FormOperations(self)

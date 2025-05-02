# ПРИЛОЖЕНИЕ: МОДЕЛЬ ДАННЫХ
# 12 фев 2025

from L20_PySide6         import C20_PySideApplication
from L90_data_completer  import C90_DataCompleter
from L90_form_accounts   import C90_FormAccounts
from L90_form_analytics  import C90_FormAnalytics
from L90_form_backups    import C90_FormBackups
from L90_form_export     import C90_FormExport
from L90_form_import     import C90_FormImport
from L90_form_main       import C90_FormMain
from L90_form_operation  import C90_FormOperation
from L90_form_processing import C90_FormProcessing


class C40_Application(C20_PySideApplication):
	""" Приложение: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.DataCompleter  = C90_DataCompleter()

		self.FormAccounts   = C90_FormAccounts(self)
		self.FormAnalytics  = C90_FormAnalytics(self)
		self.FormBackups    = C90_FormBackups(self)
		self.FormExport     = C90_FormExport(self)
		self.FormImport     = C90_FormImport(self)
		self.FormMain       = C90_FormMain(self)
		self.FormOperations = C90_FormOperation(self)
		self.FormProcessing = C90_FormProcessing(self)

# ФОРМА СЧЕТА: МЕХАНИКА УПРАВЛЕНИЯ

from L60_form_accounts import C60_FormAccounts


class C70_FormAccounts(C60_FormAccounts):
	""" Форма Счета: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Счета - {self.workspace.DmDyToString()}")

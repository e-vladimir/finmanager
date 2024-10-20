# ПРИЛОЖЕНИЕ: МОДЕЛЬ ДАННЫХ

from L20_PySide6      import C20_PySideApplication
from L90_form_backups import C90_FormBackups
from L90_form_main    import C90_FormMain


class C40_Application(C20_PySideApplication):
	""" Приложение: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.form_main    = C90_FormMain(self)
		self.form_backups = C90_FormBackups(self)

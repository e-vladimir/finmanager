# ФОРМА АРХИВ ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui    import QCursor

from L60_form_backups import C60_FormBackups


class C70_FormBackups(C60_FormBackups):
	""" Форма Архив данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle("Архив данных")

	# Меню архива данных
	def AdjustMenuBackups_Text(self):
		""" Архива данных: Настройка элементов """
		pass

	def AdjustMenuBackups_Enable(self):
		""" Архива данных: Настройка доступности элементов """
		pass

	def ShowMenuBackups(self):
		""" Отображение меню архива данных """
		self.menu_data.exec_(QCursor().pos())

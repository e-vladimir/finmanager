# ФОРМА КОПИИ АРХИВА ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ
# 18 мар 2025

from PySide6.QtGui    import QCursor

from L60_form_backups import C60_FormBackups


class C70_FormBackups(C60_FormBackups):
	""" Форма Копии архива данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle("Копии архива данных")

	# Меню Копии архива данных
	def AdjustMenuBackups(self):
		""" Настройка меню Копии архива данных """
		self.MenuBackups.clear()

		if bool(self.processing_filename):
			self.MenuBackups.addSection(self.processing_name)
			self.MenuBackups.addAction(self.ActionRestoreFromBackup)
			self.MenuBackups.addAction(self.ActionDeleteBackup)
			self.MenuBackups.addSeparator()

		self.MenuBackups.addAction(self.ActionCreateBackup)

	def ShowMenuBackups(self):
		""" Отображение меню Копий архива данных """
		self.MenuBackups.exec_(QCursor().pos())

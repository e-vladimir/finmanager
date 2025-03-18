# ФОРМА КОПИИ АРХИВА ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ
# 18 мар 2025

from L60_form_backups import C60_FormBackups


class C70_FormBackups(C60_FormBackups):
	""" Форма Копии архива данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle("Копии архива данных")

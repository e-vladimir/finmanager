# ФОРМА ОСНОВНАЯ: ЛОГИКА УПРАВЛЕНИЯ
# 12 фев 2025

from L80_form_main import C80_FormMain


class C90_FormMain(C80_FormMain):
	""" Форма Основная: Логика управления """

	# Форма
	def on_RequestOpen(self):
		""" Открытие формы """
		self.ShowTitle()
		self.ShowDyDm()

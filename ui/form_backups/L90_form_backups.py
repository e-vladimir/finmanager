# ФОРМА КОПИИ АРХИВА ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 18 мар 2025

from L80_form_backups import C80_FormBackups


class C90_FormBackups(C80_FormBackups):
	""" Форма Копии архива данных: Логика управления """

	# Форма
	def on_Opened(self):
		self.InitModelData()
		self.LoadModelData()

		self.ShowTitle()

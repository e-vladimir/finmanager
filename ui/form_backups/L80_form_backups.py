# ФОРМА КОПИИ АРХИВА ДАННЫХ: ЛОГИКА ДАННЫХ
# 18 мар 2025

from L20_PySide6      import RequestConfirm, ShowMessage
from L70_form_backups import C70_FormBackups


class C80_FormBackups(C70_FormBackups):
	""" Форма Копии архива данных: Логика данных """

	# Копия архива данных
	def RestoreFromBackup(self):
		""" Восстановление архива данных из копии """
		if not RequestConfirm("Восстановление архива данных",
		                      f"Восстановление архива данных на {self.processing_name}"): return

		if self.Application.RestoreBackup(self.processing_filename): ShowMessage("Восстановление архива данных",
		                                                                         f"Архив данных восстановлен на {self.processing_name}")

	def DeleteBackup(self):
		""" Удаление копии архива данных """
		if not RequestConfirm("Удаление архива данных",
		                      f"Удаление архива данных на {self.processing_name}"): return

		self.Application.DeleteBackup(self.processing_filename)

		self.on_BackupsChanged()

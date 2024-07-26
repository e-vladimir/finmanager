# ФОРМА РЕЗЕРВНЫЕ КОПИИ: ЛОГИКА ДАННЫХ
from PySide6.QtCore import Qt

from L20_PySide6      import RequestConfirm
from L70_form_backups import C70_FormBackups


class C80_FormBackups(C70_FormBackups):
	""" Форма Резервные копии: Логика данных """

	# Резервные копии
	def ShowBackups(self):
		""" Отображение списка резервных копий """
		for self._filename_processing in self.application.Backups(): self.LoadBackup()

	def DeleteBackup(self):
		""" Удаление резервной копии """
		if not self._filename_processing: return

		item_selected = self.model_backups.itemByIdo(self._filename_processing)

		if not RequestConfirm("Резервные копии", f"Удаление резервной копии {item_selected.data(Qt.ItemDataRole.DisplayRole)}"): return

		self.application.DeleteBackup(self._filename_processing)
		self.on_RequestShowBackups()

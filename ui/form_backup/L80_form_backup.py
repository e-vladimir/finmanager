# ФОРМА РЕЗЕРВНОЕ КОПИРОВАНИЕ: ЛОГИКА ДАННЫХ

from L20_PySide6     import ShowMessage, RequestConfirm
from L70_form_backup import C70_FormBackup


class C80_FormBackup(C70_FormBackup):
	""" Форма Резервное копирование: Логика данных """

	# Резервная копия
	def RestoreBackup(self):
		""" Восстановление резервной копии """
		if not self._processing_filename: return

		if self.application.RestoreBackup(self._processing_filename): ShowMessage("Резервное копирование", "Восстановление резервной копии завершено успешно", f"Резервная копия от {self._processing_name}")
		else                                                        : ShowMessage("Резервное копирование", "Ошибка восстановления резервной копии",            f"Резервная копия от {self._processing_name}")

	def DeleteBackup(self):
		""" Удаление резервной копии """
		if not self._processing_filename: return

		if not RequestConfirm("Резервное копирование", f"Удаление резервной копии от {self._processing_name}"): return

		self.application.DeleteBackup(self._processing_filename)

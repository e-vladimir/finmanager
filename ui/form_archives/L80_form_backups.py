# ФОРМА АРХИВЫ ДАННЫХ: ЛОГИКА ДАННЫХ

from L20_PySide6      import ShowMessage
from L70_form_backups import C70_FormArchives


class C80_FormArchives(C70_FormArchives):
	""" Форма Архив данных: Логика данных """

	# Архив данных
	def CopyDataFromArchive(self):
		""" Копирование данных из архива """
		if not self.application.CopyDataFromArchive(self._processing_filename): return

		ShowMessage("Архив данных", f"Копирование данных из архива завершено.\n\nАрхив: {self._processing_name}")

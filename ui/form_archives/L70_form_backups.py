# ФОРМА АРХИВЫ ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

import os

from   pathlib          import Path

from   PySide6.QtGui    import QCursor

from   L20_PySide6      import ShowMessage
from   L60_form_backups import C60_FormArchives


class C70_FormArchives(C60_FormArchives):
	""" Форма Архив данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle("Архивы данных")

	# Меню архива данных
	def AdjustMenuArchives_Text(self):
		""" Архива данных: Настройка элементов """
		self.submenu_archive.setTitle("Архив данных")

		if not self._processing_name: return

		self.submenu_archive.setTitle(self._processing_name)

	def AdjustMenuArchives_Enable(self):
		""" Архива данных: Настройка доступности элементов """
		flag_selected : bool = bool(self._processing_filename)

		self.action_archive_copy_from_archive.setEnabled(flag_selected)
		self.action_archive_delete.setEnabled(flag_selected)

	def ShowMenuArchives(self):
		""" Отображение меню архива данных """
		self.menu_archives.exec_(QCursor().pos())

	# Архив данных
	def CopyDataFromArchive(self):
		""" Копирование данных из архива """
		if not self.application.CopyDataFromArchive(self._processing_filename): return

		ShowMessage("Архив данных", f"Копирование данных от {self._processing_name} из архива завершено.")

	def DeleteArchive(self):
		""" Удаление архива данных """
		path_archives : Path = self.application._path_common.joinpath("archives")
		path_archive  : Path = path_archives.joinpath(self._processing_filename)

		if not path_archive.exists(): return

		try   : os.remove(path_archive)
		except: pass

		ShowMessage("Архив данных", f"Архив данных от {self._processing_name} удалён.")

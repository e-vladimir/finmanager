# ФОРМА АРХИВЫ ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui    import QCursor

from L60_form_backups import C60_FormArchives


class C70_FormArchives(C60_FormArchives):
	""" Форма Архив данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle("Архивы данных")

	# Меню архива данных
	def AdjustMenuArchives_Text(self):
		""" Архива данных: Настройка элементов """
		self.menu_archive.setTitle("Архив данных")

		if not self._processing_name: return

		self.menu_archive.setTitle(self._processing_name)

	def AdjustMenuArchives_Enable(self):
		""" Архива данных: Настройка доступности элементов """
		flag_selected : bool = bool(self._processing_filename)

		self.menu_archive_copy_from_archive.setEnabled(flag_selected)
		self.menu_archive_delete.setEnabled(flag_selected)

	def ShowMenuArchives(self):
		""" Отображение меню архива данных """
		self.menu_data.exec_(QCursor().pos())

# ФОРМА АРХИВЫ ДАННЫХ: МОДЕЛЬ UI

from PySide6.QtGui     import QIcon, QAction
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_backups  import Ui_form_archives


class C41_FormArchives(C20_PySideForm, Ui_form_archives):
	""" Форма Архив данных: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		super().InitMenus()

		self.InitMenuArchives()

	def InitMenuArchives(self):
		""" Инициализация меню архива данных """
		icon_2_2      = QIcon("./L0/icons/grid_2_2.svg")
		icon_3_3      = QIcon("./L0/icons/grid_3_3.svg")
		icon_delete   = QIcon("./L0/icons/item_delete.svg")
		icon_download = QIcon("./L0/icons/download.svg")
		icon_upload   = QIcon("./L0/icons/upload.svg")

		self.action_archives_copy_to_archive            = QAction(icon_download, "Создать архив")
		self.action_archive_copy_from_archive           = QAction(icon_upload, "Восстановить данные")
		self.action_archive_delete                      = QAction(icon_delete, "Удалить архив")

		self.menu_archives                              = QMenu()
		self.submenu_archives                           = self.menu_archives.addMenu(icon_2_2, "Архивы данных")
		self.submenu_archives.addAction(self.action_archives_copy_to_archive)

		self.submenu_archive                            = self.menu_archives.addMenu(icon_3_3, "Архив данных")
		self.submenu_archive.addAction(self.action_archive_copy_from_archive)
		self.submenu_archive.addAction(self.action_archive_delete)

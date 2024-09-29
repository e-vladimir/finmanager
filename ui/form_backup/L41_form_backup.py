# ФОРМА РЕЗЕРВНОЕ КОПИРОВАНИЕ: МОДЕЛЬ UI

from PySide6.QtGui     import QIcon, QAction
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_backup   import Ui_form_backup


class C41_FormBackup(C20_PySideForm, Ui_form_backup):
	""" Форма Резервное копирование: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuBackup()

	def InitMenuBackup(self):
		""" Инициализацию меню финсостава """
		icon_blocks   = QIcon("./L0/icons/blocks.svg")
		icon_delete   = QIcon("./L0/icons/item_delete.svg")
		icon_download = QIcon("./L0/icons/download.svg")
		icon_grid_13  = QIcon("./L0/icons/grid_1_3.svg")
		icon_upload   = QIcon("./L0/icons/upload.svg")

		self.menu_backup = QMenu()
		self.menu_backups_header : QMenu   = self.menu_backup.addMenu(icon_grid_13, "Резервные копии")
		self.menu_backups_create : QAction = self.menu_backups_header.addAction(icon_download, "Создать копию")

		self.menu_backup_header  : QMenu   = self.menu_backup.addMenu(icon_blocks, "Резервная копия")
		self.menu_backup_restore : QAction = self.menu_backup_header.addAction(icon_upload, "Восстановить")
		self.menu_backup_delete  : QAction = self.menu_backup_header.addAction(icon_delete, "Удалить")

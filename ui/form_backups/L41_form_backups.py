# ФОРМА РЕЗЕРВНЫЕ КОПИИ: МОДЕЛЬ UI

from PySide6.QtGui     import QIcon, QAction
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_backups  import Ui_frm_backups


class C41_FormBackups(C20_PySideForm, Ui_frm_backups):
	""" Форма Резервные копии: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuBackups()

	def InitMenuBackups(self):
		""" Меню финданных """
		icon_download = QIcon("./ui/icons/download.png")
		icon_trash    = QIcon("./ui/icons/trash.png")
		icon_upload   = QIcon("./ui/icons/upload.png")

		self.mnu_backups                          = QMenu(self.lst_backups)

		self.mnu_backups_header         : QAction = self.mnu_backups.addSection("Резервное копирование")
		self.mnu_backups_create_backup  : QAction = self.mnu_backups.addAction(icon_download, "Создать резервную копию")

		self.mnu_backups_backup_header  : QAction = self.mnu_backups.addSection("Резервная копия")
		self.mnu_backups_backup_restore : QAction = self.mnu_backups.addAction(icon_upload,   "Восстановить резервную копию")
		self.mnu_backups_backup_delete  : QAction = self.mnu_backups.addAction(icon_trash,    "Удалить резервную копию")

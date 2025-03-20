# ФОРМА КОПИИ АРХИВА ДАННЫХ: МОДЕЛЬ UI
# 18 мар 2025

from PySide6.QtGui     import QAction, QIcon
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_backups  import Ui_FormBackups


class C41_FormBackups(C20_PySideForm, Ui_FormBackups):
	""" Форма Копии архива данных: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuBackups()

	def InitMenuBackups(self):
		""" Инициализация меню копий архива данных """
		icon_download    = QIcon("./L0/icons/download.svg")
		icon_upload      = QIcon("./L0/icons/upload.svg")
		icon_item_delete = QIcon("./L0/icons/item_delete.svg")

		self.ActionCreateBackup      = QAction(icon_download,    "Создать копию архива данных")
		self.ActionRestoreFromBackup = QAction(icon_upload,      "Восстановить архив данных из копии")
		self.ActionDeleteBackup      = QAction(icon_item_delete, "Удалить копию архива данных")

		self.MenuBackups             = QMenu("Копии архива данных")

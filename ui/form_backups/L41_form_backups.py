# ФОРМА АРХИВ ДАННЫХ: МОДЕЛЬ UI

from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_backups  import Ui_form_backups


class C41_FormBackups(C20_PySideForm, Ui_form_backups):
	""" Форма Архив данных: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		super().InitMenus()

		self.InitMenuBackups()

	def InitMenuBackups(self):
		""" Инициализация меню архива данных """
		icon_plus = QIcon("./L0/icons/item_plus.svg")
		icon_2_2  = QIcon("./L0/icons/grid_2_2.svg")
		icon_3_3  = QIcon("./L0/icons/grid_3_3.svg")

		self.menu_data                            = QMenu()

		self.menu_backups                         = self.menu_data.addMenu(icon_2_2, "Архив данных")
		self.menu_backups_create_backup : QAction = self.menu_backups.addAction(icon_plus, "Создать архив данных")

		self.menu_backup                          = self.menu_data.addMenu(icon_3_3, "Архив")

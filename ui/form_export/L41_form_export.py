# ФОРМА ЭКСПОРТ ДАННЫХ: МОДЕЛЬ UI
# 01 апр 2025

from PySide6.QtGui     import QAction, QIcon
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_export   import Ui_FormExport


class C41_FormExport(Ui_FormExport, C20_PySideForm):
	""" Форма экспорт данных: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuOperations()

	def InitMenuOperations(self):
		""" Инициализация меню экспорта операций """
		icon_arrow_lr    = QIcon("./L0/icons/arrow_left_right.svg")
		icon_blocks      = QIcon("./L0/icons/blocks.svg")
		icon_folder      = QIcon("./L0/icons/folder.svg")
		icon_upload      = QIcon("./L0/icons/upload.svg")

		self.ActionOperationsEditInterval  = QAction(icon_arrow_lr, "Установить интервал")
		self.ActionOperationsEditAccounts  = QAction(icon_blocks,   "Указать счета")
		self.ActionOperationsEditDirectory = QAction(icon_folder,   "Указать директорию")
		self.ActionExportOperations        = QAction(icon_upload,   "Выполнить экспорт операций")

		self.MenuOperations                = QMenu("Экспорт операций")
		self.MenuOperations.addAction(self.ActionOperationsEditInterval)
		self.MenuOperations.addAction(self.ActionOperationsEditAccounts)
		self.MenuOperations.addAction(self.ActionOperationsEditDirectory)
		self.MenuOperations.addSeparator()

		self.MenuOperations.addAction(self.ActionExportOperations)

# ФОРМА ИМПОРТ ДАННЫХ: МОДЕЛЬ UI
# 14 мар 2025

from PySide6.QtGui     import QAction, QIcon
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_import   import Ui_form_import


class C41_FormImport(C20_PySideForm, Ui_form_import):
	""" Форма Импорт данных: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuOperations()

	def InitMenuOperations(self):
		""" Инициализацию меню операций """
		icon_download = QIcon("./L0/icons/download.svg")
		icon_open     = QIcon("./L0/icons/open.svg")
		icon_edit     = QIcon("./L0/icons/edit.svg")

		self.ActionLoadOperationsFromFile    = QAction(icon_open,     "Открыть файл")
		self.ActionImportOperations          = QAction(icon_download, "Импорт операций")
		self.ActionEditOperationsStructField = QAction(icon_edit,     "Указать поле")

		self.MenuOperations                  = QMenu("Операции")
		self.MenuOperations.addAction(self.ActionLoadOperationsFromFile)
		self.MenuOperations.addSeparator()
		self.MenuOperations.addAction(self.ActionEditOperationsStructField)
		self.MenuOperations.addSeparator()
		self.MenuOperations.addAction(self.ActionImportOperations)

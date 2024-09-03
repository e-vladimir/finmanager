# ФОРМА ИМПОРТ ДАННЫХ: МОДЕЛЬ UI

from PySide6.QtGui     import QIcon, QAction
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_import   import Ui_form_import


class C41_FormImport(C20_PySideForm, Ui_form_import):
	""" Форма Импорт данных: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuImportFinactionsData()

	def InitMenuImportFinactionsData(self):
		""" Инициализацию меню финсостава """
		icon_file      = QIcon("./ui/icons/file.svg")

		self.menu_import_finactions                     = QMenu()
		self.menu_import_finactions_open_file : QAction = self.menu_import_finactions.addAction(icon_file, "Открыть локальный файл")

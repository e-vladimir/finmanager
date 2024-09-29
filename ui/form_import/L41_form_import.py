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
		icon_file      = QIcon("./L0/icons/file.svg")
		icon_open      = QIcon("./L0/icons/open.svg")
		icon_delete    = QIcon("./L0/icons/item_delete.svg")
		icon_download  = QIcon("./L0/icons/download.svg")
		icon_grid_33   = QIcon("./L0/icons/grid_3_3.svg")
		icon_grid_13   = QIcon("./L0/icons/grid_1_3.svg")

		self.menu_import_finactions                                    = QMenu()
		self.menu_import_finactions_source_header                      = self.menu_import_finactions.addMenu(icon_open, "Источник данных")
		self.menu_import_finactions_source_open_file         : QAction = self.menu_import_finactions_source_header.addAction(icon_file,    "Открыть локальный файл")

		self.menu_import_finactions_column_header            : QMenu   = self.menu_import_finactions.addMenu(icon_grid_33,  "Колонка данных")
		self.menu_import_finactions_column_set_field         : QAction = self.menu_import_finactions_column_header.addAction(icon_grid_13, "Указать тип поля")
		self.menu_import_finactions_column_reset_field       : QAction = self.menu_import_finactions_column_header.addAction(icon_delete,  "Не учитывать поле")
		self.menu_import_finactions.addSeparator()

		self.menu_import_finactions_exec_import              : QAction = self.menu_import_finactions.addAction(icon_download,    "Выполнить импорт")

# ФОРМА ИМПОРТ ДАННЫХ: МОДЕЛЬ UI

from PySide6.QtGui     import QAction, QIcon
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_import   import Ui_frm_import


class C41_FormImport(C20_PySideForm, Ui_frm_import):
	""" Форма Импорт данных: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuOperation()

	def InitMenuOperation(self):
		""" Инициализация меню Импорта операций """
		icon_download                                           = QIcon("./L0/icons/download.svg")
		icon_edit                                               = QIcon("./L0/icons/edit.svg")
		icon_grid_3_3                                           = QIcon("./L0/icons/grid_3_3.svg")
		icon_list                                               = QIcon("./L0/icons/list.svg")
		icon_open                                               = QIcon("./L0/icons/open.svg")
		icon_reload                                             = QIcon("./L0/icons/reload.svg")

		self.menu_operations                                    = QMenu("Финансовые операции")

		self.submenu_operations_operations                      = self.menu_operations.addMenu(icon_list, "Финансовые операции")
		self.action_operations_operations_open_file   : QAction = self.submenu_operations_operations.addAction(icon_open,     "Открыть файл")
		self.action_operations_operations_switch_data : QAction = self.submenu_operations_operations.addAction(icon_reload,   "Сменить набор данных")
		self.submenu_operations_operations.addSeparator()
		self.action_operations_operations_exec_import : QAction = self.submenu_operations_operations.addAction(icon_download, "Импортировать данные")

		self.submenu_operations_header                          = self.menu_operations.addMenu(icon_grid_3_3, "Элемент заголовка файла")
		self.action_operations_header_set_field       : QAction = self.submenu_operations_header.addAction(icon_edit, "Указать тип данных")

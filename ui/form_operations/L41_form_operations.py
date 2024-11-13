# ФОРМА ФИНАНСОВЫЕ ОПЕРАЦИИ: МОДЕЛЬ UI

from PySide6.QtGui       import QIcon, QAction
from PySide6.QtWidgets   import QMenu

from L20_PySide6         import C20_PySideForm
from L40_form_operations import Ui_frm_operations


class C41_FormOperations(C20_PySideForm, Ui_frm_operations):
	""" Форма Финансовые операции: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		super().InitMenus()

		self.Init_MenuOperations()

	def Init_MenuOperations(self):
		""" Инициализация меню Финансовые операции """
		icon_open      = QIcon("./L0/icons/open.svg")
		icon_edit      = QIcon("./L0/icons/edit.svg")
		icon_list      = QIcon("./L0/icons/list.svg")
		icon_blocks    = QIcon("./L0/icons/blocks.svg")
		icon_item_plus = QIcon("./L0/icons/item_plus.svg")
		icon_grid_3_3  = QIcon("./L0/icons/grid_3_3.svg")
		icon_delete    = QIcon("./L0/icons/item_delete.svg")
		icon_black     = QIcon("./L0/icons/square_black.svg")
		icon_blue      = QIcon("./L0/icons/square_blue.svg")
		icon_gray      = QIcon("./L0/icons/square_gray.svg")
		icon_green     = QIcon("./L0/icons/square_green.svg")
		icon_red       = QIcon("./L0/icons/square_red.svg")

		self.menu_operations                              = QMenu("Операции")

		self.submenu_operations                           = self.menu_operations.addMenu(icon_blocks, "Операции")
		self.action_operations_create_operation : QAction = self.submenu_operations.addAction(icon_item_plus, "Создать операцию")

		self.submenu_operation                            = self.menu_operations.addMenu(icon_grid_3_3, "Операция")
		self.action_operation_open_operation    : QAction = self.submenu_operation.addAction(icon_open,   "Открыть операцию")
		self.action_operation_set_description   : QAction = self.submenu_operation.addAction(icon_edit,   "Редактировать описание")
		self.action_operation_set_labels        : QAction = self.submenu_operation.addAction(icon_list,   "Редактировать метки")
		self.action_operation_delete_operation  : QAction = self.submenu_operation.addAction(icon_delete, "Удалить операцию")
		self.submenu_operation.addSeparator()
		self.submenu_operation_colors                     = self.submenu_operation.addMenu(icon_gray, "Цветовая метка")
		self.action_operation_colors_set_black  : QAction = self.submenu_operation_colors.addAction(icon_black, "Чёрный")
		self.action_operation_colors_set_gray   : QAction = self.submenu_operation_colors.addAction(icon_gray,  "Серый")
		self.submenu_operation_colors.addSeparator()
		self.action_operation_colors_set_red    : QAction = self.submenu_operation_colors.addAction(icon_red,   "Красный")
		self.action_operation_colors_set_blue   : QAction = self.submenu_operation_colors.addAction(icon_blue,  "Синий")
		self.action_operation_colors_set_green  : QAction = self.submenu_operation_colors.addAction(icon_green, "Зелёный")

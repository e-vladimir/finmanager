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
		icon_blocks    = QIcon("./L0/icons/blocks.svg")
		icon_item_plus = QIcon("./L0/icons/item_plus.svg")
		icon_grid_3_3  = QIcon("./L0/icons/grid_3_3.svg")
		icon_delete    = QIcon("./L0/icons/item_delete.svg")

		self.menu_operations                              = QMenu("Операции")

		self.submenu_operations                           = self.menu_operations.addMenu(icon_blocks, "Операции")
		self.action_operations_create_operation : QAction = self.submenu_operations.addAction(icon_item_plus, "Создать операцию")

		self.submenu_operation                            = self.menu_operations.addMenu(icon_grid_3_3, "Операция")
		self.action_operations_open_operation   : QAction = self.submenu_operation.addAction(icon_open,   "Открыть операцию")
		self.action_operations_delete_operation : QAction = self.submenu_operation.addAction(icon_delete, "Удалить операцию")

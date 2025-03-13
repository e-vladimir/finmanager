# ФОРМА ОПЕРАЦИИ: МОДЕЛЬ UI
# 11 мар 2025

from PySide6.QtGui      import QAction, QIcon
from PySide6.QtWidgets  import QMenu

from L20_PySide6        import C20_PySideForm
from L40_form_operation import Ui_form_operations


class C41_FormOperation(C20_PySideForm, Ui_form_operations):
	""" Форма Операции: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		""" Инициализация меню """
		self.InitMenuOperations()

	def InitMenuOperations(self):
		""" Инициализацию меню операций """
		icon_grid_1_3    = QIcon("./L0/icons/grid_1_3.svg")
		icon_item_plus   = QIcon("./L0/icons/item_plus.svg")

		self.ActionCreateOperation = QAction(icon_item_plus,   "Создать операцию")

		self.MenuOperation         = QMenu("Операции")

		self.SubmenuOperations     = QMenu("Операции",         icon=icon_grid_1_3)
		self.SubmenuOperations.addAction(self.ActionCreateOperation)

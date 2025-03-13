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
		icon_grid_3_3    = QIcon("./L0/icons/grid_3_3.svg")
		icon_edit        = QIcon("./L0/icons/edit.svg")
		icon_item_delete = QIcon("./L0/icons/item_delete.svg")
		icon_item_plus   = QIcon("./L0/icons/item_plus.svg")

		self.ActionCreateOperation          = QAction(icon_item_plus,   "Создать операцию")
		self.ActionDeleteOperation          = QAction(icon_item_delete, "Удалить операцию")
		self.ActionEditOperationDd          = QAction(icon_edit,        "Редактировать дату")
		self.ActionEditOperationAmount      = QAction(icon_edit,        "Редактировать сумму")
		self.ActionEditOperationAccounts    = QAction(icon_edit,        "Редактировать счета")
		self.ActionEditOperationDescription = QAction(icon_edit,        "Редактировать описание")

		self.MenuOperation                  = QMenu("Операции")

		self.SubmenuOperations              = QMenu("Операции",         icon=icon_grid_1_3)
		self.SubmenuOperations.addAction(self.ActionCreateOperation)

		self.SubmenuOperation               = QMenu("Операция",         icon=icon_grid_3_3)
		self.SubmenuOperation.addAction(self.ActionEditOperationDd)
		self.SubmenuOperation.addAction(self.ActionEditOperationAmount)
		self.SubmenuOperation.addAction(self.ActionEditOperationAccounts)
		self.SubmenuOperation.addAction(self.ActionEditOperationDescription)
		self.SubmenuOperation.addSeparator()
		self.SubmenuOperation.addAction(self.ActionDeleteOperation)

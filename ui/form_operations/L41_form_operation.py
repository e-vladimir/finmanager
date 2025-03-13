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
		icon_wallet      = QIcon("./L0/icons/wallet.svg")
		icon_money       = QIcon("./L0/icons/money.svg")
		icon_item_delete = QIcon("./L0/icons/item_delete.svg")
		icon_item_plus   = QIcon("./L0/icons/item_plus.svg")
		icon_color_black = QIcon("./L0/icons/square_black.svg")
		icon_color_gray  = QIcon("./L0/icons/square_gray.svg")
		icon_color_green = QIcon("./L0/icons/square_green.svg")
		icon_color_blue  = QIcon("./L0/icons/square_blue.svg")
		icon_color_red   = QIcon("./L0/icons/square_red.svg")

		self.ActionCreateOperation          = QAction(icon_item_plus,   "Создать операцию")
		self.ActionDeleteOperation          = QAction(icon_item_delete, "Удалить операцию")
		self.ActionEditOperationAmount      = QAction(icon_money,       "Редактировать сумму")
		self.ActionEditOperationAccounts    = QAction(icon_wallet,      "Редактировать счета")
		self.ActionEditOperationDescription = QAction(icon_edit,        "Редактировать описание")
		self.ActionSetOperationColorBlack   = QAction(icon_color_black, "Чёрный")
		self.ActionSetOperationColorGray    = QAction(icon_color_gray,  "Серый")
		self.ActionSetOperationColorGreen   = QAction(icon_color_green, "Зелёный")
		self.ActionSetOperationColorBlue    = QAction(icon_color_blue,  "Синий")
		self.ActionSetOperationColorRed     = QAction(icon_color_red,   "Красный")

		self.MenuOperation                  = QMenu("Операции")

		self.SubmenuOperations              = QMenu("Операции",         icon=icon_grid_1_3)
		self.SubmenuOperations.addAction(self.ActionCreateOperation)

		self.SubmenuOperation               = QMenu("Операция",         icon=icon_grid_3_3)
		self.SubmenuOperation.addAction(self.ActionEditOperationAmount)
		self.SubmenuOperation.addAction(self.ActionEditOperationAccounts)
		self.SubmenuOperation.addAction(self.ActionEditOperationDescription)
		self.SubmenuOperation.addSeparator()
		self.SubmenuOperation.addAction(self.ActionSetOperationColorBlack)
		self.SubmenuOperation.addAction(self.ActionSetOperationColorGray)
		self.SubmenuOperation.addAction(self.ActionSetOperationColorGreen)
		self.SubmenuOperation.addAction(self.ActionSetOperationColorBlue)
		self.SubmenuOperation.addAction(self.ActionSetOperationColorRed)
		self.SubmenuOperation.addSeparator()
		self.SubmenuOperation.addAction(self.ActionDeleteOperation)

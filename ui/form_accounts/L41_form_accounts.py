# ФОРМА СЧЕТА: МОДЕЛЬ UI

from PySide6.QtGui     import QIcon, QAction
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_accounts import Ui_frm_accounts


class C41_FormAccounts(C20_PySideForm, Ui_frm_accounts):
	""" Форма Счета: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		super().InitMenus()

		self.Init_MenuAccounts()

	def Init_MenuAccounts(self):
		""" Инициализация меню Счёта """
		icon_blocks      = QIcon("./L0/icons/blocks.svg")
		icon_edit        = QIcon("./L0/icons/edit.svg")
		icon_reload      = QIcon("./L0/icons/reload.svg")
		icon_arrow_lr    = QIcon("./L0/icons/arrow_left_right.svg")
		icon_item_delete = QIcon("./L0/icons/item_delete.svg")
		icon_grid_2_2    = QIcon("./L0/icons/grid_2_2.svg")
		icon_grid_3_3    = QIcon("./L0/icons/grid_3_3.svg")
		icon_item_plus   = QIcon("./L0/icons/item_plus.svg")

		self.menu_accounts                                 = QMenu("Счета")

		self.menu_accounts_struct                          = self.menu_accounts.addMenu(icon_blocks,   "Структура счетов")
		self.menu_accounts_struct_create_account : QAction = self.menu_accounts_struct.addAction(icon_item_plus, "Создать счёт")
		self.menu_accounts_struct.addSeparator()
		self.menu_accounts_struct_reset          : QAction = self.menu_accounts_struct.addAction(icon_reload, "Сброс данных")

		self.menu_accounts_group                           = self.menu_accounts.addMenu(icon_grid_2_2, "Группа счетов")
		self.menu_account_group_rename           : QAction = self.menu_accounts_group.addAction(icon_edit, "Переименовать группу")

		self.menu_account                                  = self.menu_accounts.addMenu(icon_grid_3_3, "Счет")
		self.menu_account_rename                 : QAction = self.menu_account.addAction(icon_edit,        "Переименовать счёт")
		self.menu_account_delete                 : QAction = self.menu_account.addAction(icon_item_delete, "Удалить счёт")
		self.menu_account.addSeparator()
		self.menu_account_change_group           : QAction = self.menu_account.addAction(icon_arrow_lr,    "Переместить в другую группу")

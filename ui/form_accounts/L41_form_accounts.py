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
		icon_arrow_l     = QIcon("./L0/icons/arrow_left.svg")
		icon_arrow_lr    = QIcon("./L0/icons/arrow_left_right.svg")
		icon_arrow_r     = QIcon("./L0/icons/arrow_right.svg")
		icon_blocks      = QIcon("./L0/icons/blocks.svg")
		icon_edit        = QIcon("./L0/icons/edit.svg")
		icon_grid_2_2    = QIcon("./L0/icons/grid_2_2.svg")
		icon_grid_3_3    = QIcon("./L0/icons/grid_3_3.svg")
		icon_item_delete = QIcon("./L0/icons/item_delete.svg")
		icon_item_plus   = QIcon("./L0/icons/item_plus.svg")
		icon_reload      = QIcon("./L0/icons/reload.svg")

		self.action_accounts_struct_create_account   = QAction(icon_item_plus, "Создать счёт")
		self.action_accounts_struct_transfer_prev_dm = QAction(icon_arrow_l, "Перенести в прошлый месяц")
		self.action_accounts_struct_transfer_next_dm = QAction(icon_arrow_r, "Перенести в следующий месяц")
		self.action_accounts_struct_reset            = QAction(icon_reload, "Сброс данных")
		self.action_account_group_rename             = QAction(icon_edit, "Переименовать")
		self.action_account_group_transfer_prev_dm   = QAction(icon_arrow_l, "Перенести в прошлый месяц")
		self.action_account_group_transfer_next_dm   = QAction(icon_arrow_r, "Перенести в следующий месяц")
		self.action_account_set_balance_initial      = QAction(icon_edit, "Установить остаток начальный")
		self.action_account_rename                   = QAction(icon_edit, "Переименовать")
		self.action_account_delete                   = QAction(icon_item_delete, "Удалить")
		self.action_account_change_group             = QAction(icon_arrow_lr, "Перенести в другую группу")
		self.action_account_transfer_prev_dm         = QAction(icon_arrow_l, "Перенести в прошлый месяц")
		self.action_account_transfer_next_dm         = QAction(icon_arrow_r, "Перенести в следующий месяц")

		self.menu_accounts                           = QMenu("Счета")
		self.submenu_accounts                        = self.menu_accounts.addMenu(icon_blocks, "Счета")
		self.submenu_accounts.addAction(self.action_accounts_struct_create_account)
		self.submenu_accounts.addSeparator()
		self.submenu_accounts.addAction(self.action_accounts_struct_transfer_prev_dm)
		self.submenu_accounts.addAction(self.action_accounts_struct_transfer_next_dm)
		self.submenu_accounts.addSeparator()
		self.submenu_accounts.addAction(self.action_accounts_struct_reset)

		self.submenu_account_group                   = self.menu_accounts.addMenu(icon_grid_2_2, "Группа счетов")
		self.submenu_account_group.addAction(self.action_account_group_rename)
		self.submenu_account_group.addSeparator()
		self.submenu_account_group.addAction(self.action_account_group_transfer_prev_dm)
		self.submenu_account_group.addAction(self.action_account_group_transfer_next_dm)

		self.submenu_account                         = self.menu_accounts.addMenu(icon_grid_3_3, "Счет")
		self.submenu_account.addAction(self.action_account_set_balance_initial)
		self.submenu_account.addSeparator()
		self.submenu_account.addAction(self.action_account_rename)
		self.submenu_account.addAction(self.action_account_delete)
		self.submenu_account.addSeparator()
		self.submenu_account.addAction(self.action_account_change_group)
		self.submenu_account.addSeparator()
		self.submenu_account.addAction(self.action_account_transfer_prev_dm)
		self.submenu_account.addAction(self.action_account_transfer_next_dm)

# ФОРМА СЧЕТА: МОДЕЛЬ UI
# 14 фев 2025

from PySide6.QtGui     import QAction, QIcon
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_accounts import Ui_FormAccounts


class C41_FormAccounts(C20_PySideForm, Ui_FormAccounts):
	""" Форма Счета: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuAccounts()

	def InitMenuAccounts(self):
		""" Инициализация меню Счета """
		icon_item_plus   = QIcon("./L0/icons/item_plus.svg")
		icon_item_delete = QIcon("./L0/icons/item_delete.svg")
		icon_edit        = QIcon("./L0/icons/edit.svg")
		icon_grid_1_3    = QIcon("./L0/icons/grid_1_3.svg")
		icon_grid_2_2    = QIcon("./L0/icons/grid_2_2.svg")
		icon_grid_3_3    = QIcon("./L0/icons/grid_3_3.svg")

		self.ActionCreateAccount     = QAction(icon_item_plus,   "Создать счёт")
		self.ActionSetNameAccount    = QAction(icon_edit,        "Переименовать счёт")
		self.ActionDeleteAccount     = QAction(icon_item_delete, "Удалить счёт")
		self.ActionSetInitialBalance = QAction(icon_edit,        "Установить баланс начальный")

		self.ActionSetNameGroup      = QAction(icon_edit,        "Переименовать группу счетов")

		self.MenuAccounts            = QMenu("Счета")

		self.SubmenuAccounts         = QMenu("Счета",         icon=icon_grid_1_3)
		self.SubmenuAccounts.addAction(self.ActionCreateAccount)

		self.SubmenuGroup            = QMenu("Группа счетов", icon=icon_grid_2_2)
		self.SubmenuGroup.addAction(self.ActionCreateAccount)
		self.SubmenuGroup.addSeparator()
		self.SubmenuGroup.addAction(self.ActionSetNameGroup)

		self.SubmenuAccount          = QMenu("Счёт",          icon=icon_grid_3_3)
		self.SubmenuAccount.addAction(self.ActionSetNameAccount)
		self.SubmenuAccount.addAction(self.ActionDeleteAccount)
		self.SubmenuAccount.addSeparator()
		self.SubmenuAccount.addAction(self.ActionSetInitialBalance)

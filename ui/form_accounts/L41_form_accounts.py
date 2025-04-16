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
		icon_edit        = QIcon("./L0/icons/edit.svg")
		icon_file        = QIcon("./L0/icons/file.svg")
		icon_grid_1_3    = QIcon("./L0/icons/grid_1_3.svg")
		icon_grid_2_2    = QIcon("./L0/icons/grid_2_2.svg")
		icon_grid_3_3    = QIcon("./L0/icons/grid_3_3.svg")
		icon_item_delete = QIcon("./L0/icons/item_delete.svg")
		icon_item_plus   = QIcon("./L0/icons/item_plus.svg")
		icon_left        = QIcon("./L0/icons/arrow_left.svg")
		icon_reload      = QIcon("./L0/icons/reload.svg")
		icon_right       = QIcon("./L0/icons/arrow_right.svg")
		icon_star        = QIcon("./L0/icons/star.svg")

		self.ActionResetAccounts             = QAction(icon_reload,      "Сбросить данные")
		self.ActionTransferAccountsToPrevDm  = QAction(icon_left,        "Перенести в прошлый месяц")
		self.ActionTransferAccountsToNextDm  = QAction(icon_right,       "Перенести в следующий месяц")
		self.ActionGenerateReportBalances    = QAction(icon_file,        "Отчёт по остаткам")
		self.ActionGenerateReportDm          = QAction(icon_file,        "Отчёт за месяц")

		self.ActionEditGroupName             = QAction(icon_edit,        "Изменить наименование")
		self.ActionTransferGroupToPrevDm     = QAction(icon_left,        "Перенести в прошлый месяц")
		self.ActionTransferGroupToNextDm     = QAction(icon_right,       "Перенести в следующий месяц")

		self.ActionCreateAccount             = QAction(icon_item_plus,   "Создать счёт")
		self.ActionEditAccountName           = QAction(icon_edit,        "Изменить наименование")
		self.ActionEditAccountGroup          = QAction(icon_edit,        "Изменить группу счетов")
		self.ActionEditAccountInitialBalance = QAction(icon_edit,        "Изменить остаток начальный")
		self.ActionDeleteAccount             = QAction(icon_item_delete, "Удалить счёт")
		self.ActionTransferAccountToPrevDm   = QAction(icon_left,        "Перенести в прошлый месяц")
		self.ActionTransferAccountToNextDm   = QAction(icon_right,       "Перенести в следующий месяц")
		self.ActionSwitchAccountPriority     = QAction(icon_star,        "Установить как приоритетный")

		self.MenuAccounts                    = QMenu("Счета")

		self.SubmenuAccounts                 = QMenu("Счета",         icon=icon_grid_1_3)
		self.SubmenuAccounts.addAction(self.ActionCreateAccount)
		self.SubmenuAccounts.addSeparator()
		self.SubmenuAccounts.addAction(self.ActionTransferAccountsToPrevDm)
		self.SubmenuAccounts.addAction(self.ActionTransferAccountsToNextDm)
		self.SubmenuAccounts.addSeparator()
		self.SubmenuAccounts.addAction(self.ActionGenerateReportBalances)
		self.SubmenuAccounts.addAction(self.ActionGenerateReportDm)
		self.SubmenuAccounts.addSeparator()
		self.SubmenuAccounts.addAction(self.ActionResetAccounts)

		self.SubmenuGroup                    = QMenu("Группа счетов", icon=icon_grid_2_2)
		self.SubmenuGroup.addAction(self.ActionCreateAccount)
		self.SubmenuGroup.addSeparator()
		self.SubmenuGroup.addAction(self.ActionEditGroupName)
		self.SubmenuGroup.addSeparator()
		self.SubmenuGroup.addAction(self.ActionTransferGroupToPrevDm)
		self.SubmenuGroup.addAction(self.ActionTransferGroupToNextDm)

		self.SubmenuAccount                  = QMenu("Счёт",          icon=icon_grid_3_3)
		self.SubmenuAccount.addAction(self.ActionEditAccountName)
		self.SubmenuAccount.addAction(self.ActionEditAccountGroup)
		self.SubmenuAccount.addAction(self.ActionEditAccountInitialBalance)
		self.SubmenuAccount.addSeparator()
		self.SubmenuAccount.addAction(self.ActionTransferAccountToPrevDm)
		self.SubmenuAccount.addAction(self.ActionTransferAccountToNextDm)
		self.SubmenuAccount.addSeparator()
		self.SubmenuAccount.addAction(self.ActionDeleteAccount)

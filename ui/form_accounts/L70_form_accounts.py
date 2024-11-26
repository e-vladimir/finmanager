# ФОРМА СЧЕТА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui     import Qt, QCursor, QColor
from PySide6.QtWidgets import QHeaderView

from L20_PySide6       import C20_StandardItem
from L60_form_accounts import C60_FormAccounts


class C70_FormAccounts(C60_FormAccounts):
	""" Форма Счета: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Счета - {self.workspace.DmDyToString()}")

	# Дерево данных
	def AdjustTreeData_Size(self):
		""" Дерево данных: Настройка размера """
		self.tree_data.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

		self.tree_data.setColumnWidth(1, 100)
		self.tree_data.setColumnWidth(2, 100)
		self.tree_data.setColumnWidth(3, 100)
		self.tree_data.setColumnWidth(4, 100)
		self.tree_data.setColumnWidth(5, 100)

	def AdjustTreeData_Color(self):
		""" Дерево данных: Настройка цветового оформления """
		self.model_data.adjustGroupView(True, True, True)

		for index_group in range(self.model_data.rowCount()):
			item_group : C20_StandardItem = self.model_data.item(index_group, 0)

			for index_account in range(item_group.rowCount()):
				item_amount : C20_StandardItem = item_group.child(index_account, 1)
				color_text                     = QColor(200, 0, 0) if '-' in item_amount.text() else QColor(0, 0, 0)

				item_amount.setForeground(color_text)

	def AdjustTreeData_Sort(self):
		""" Дерево данных: Настройка сортировки """
		self.tree_data.sortByColumn(0, Qt.SortOrder.AscendingOrder)

	def AdjustTreeData_Expand(self):
		""" Дерево данных: Настройка раскрытия структуры """
		self.tree_data.expandAll()

	def ProcessingTreeDataDbClick(self):
		""" Обработка двойного клика по дереву данных """
		flag_select_account : bool = bool(self._processing_ido)

		match self._processing_column:
			case 0:
				if flag_select_account: self.on_RequestRenameAccount()
				else                  : self.on_RequestRenameAccountsGroup()

			case 1:
				if flag_select_account: self.on_RequestSetBalanceInitial()

	# Меню Счета
	def AdjustMenuAccounts_Text(self):
		""" Меню Счета: Настройка наименования """
		self.submenu_account_group.setTitle("Группа счетов")
		self.submenu_account.setTitle("Счёт")

		if bool(self._processing_group):
			self.submenu_account_group.setTitle(self._processing_group)

		if bool(self._processing_name):
			self.submenu_account.setTitle(self._processing_name)

	def AdjustMenuAccounts_Enable(self):
		""" Меню Счета: Настройка доступности """
		flag_selected_group   : bool = bool(self._processing_group)
		flag_selected_account : bool = bool(self._processing_name)

		self.action_account_group_rename.setEnabled(flag_selected_group)
		self.action_account_group_transfer_prev_dm.setEnabled(flag_selected_group)
		self.action_account_group_transfer_next_dm.setEnabled(flag_selected_group)

		self.action_account_rename.setEnabled(flag_selected_account)
		self.action_account_delete.setEnabled(flag_selected_account)
		self.action_account_change_group.setEnabled(flag_selected_account)
		self.action_account_transfer_prev_dm.setEnabled(flag_selected_account)
		self.action_account_transfer_next_dm.setEnabled(flag_selected_account)

	def ShowMenuAccounts(self):
		""" Отображение меню Счета """
		self.menu_accounts.exec_(QCursor().pos())

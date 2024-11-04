# ФОРМА СЧЕТА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui     import Qt, QCursor

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
		pass

	def AdjustTreeData_Color(self):
		""" Дерево данных: Настройка цветового оформления """
		self.model_data.adjustGroupView(True, True, True)

	def AdjustTreeData_Sort(self):
		""" Дерево данных: Настройка сортировки """
		self.tree_data.sortByColumn(0, Qt.SortOrder.AscendingOrder)

	def AdjustTreeData_Expand(self):
		""" Дерево данных: Настройка раскрытия структуры """
		self.tree_data.expandAll()

	# Меню Счета
	def AdjustMenuAccounts_Text(self):
		""" Меню Счета: Настройка наименования """
		self.menu_accounts_group.setTitle("Группа счетов")
		self.menu_account.setTitle("Счёт")

		if bool(self._processing_group):
			self.menu_accounts_group.setTitle(self._processing_group)

		if bool(self._processing_name):
			self.menu_account.setTitle(self._processing_name)

	def AdjustMenuAccounts_Enable(self):
		""" Меню Счета: Настройка доступности """
		flag_selected_group   : bool = bool(self._processing_group)
		flag_selected_account : bool = bool(self._processing_name)

		self.menu_account_group_rename.setEnabled(flag_selected_group)

		self.menu_account_rename.setEnabled(flag_selected_account)
		self.menu_account_delete.setEnabled(flag_selected_account)
		self.menu_account_change_group.setEnabled(flag_selected_account)
		self.menu_account_transfer_next_dm.setEnabled(flag_selected_account)

	def ShowMenuAccounts(self):
		""" Отображение меню Счета """
		self.menu_accounts.exec_(QCursor().pos())

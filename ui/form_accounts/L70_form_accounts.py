# ФОРМА СЧЕТА: МЕХАНИКА УПРАВЛЕНИЯ
# 14 фев 2025

from PySide6.QtCore    import Qt
from PySide6.QtGui     import QCursor
from PySide6.QtWidgets import QHeaderView

from L60_form_accounts import C60_FormAccounts
from L90_account       import C90_Account


class C70_FormAccounts(C60_FormAccounts):
	""" Форма Счета: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Счета - {self.Workspace.DmDyToString()}")

	# Меню Счета
	def AdjustMenuAccounts(self):
		""" Настройка меню Счета """
		self.MenuAccounts.clear()

		if   self._processing_ido :
			account = C90_Account(self.processing_ido)

			self.MenuAccounts.addSection(account.name)
			self.MenuAccounts.addAction(self.ActionEditAccountInitialBalance)
			self.MenuAccounts.addAction(self.ActionEditAccountGroup)
			self.MenuAccounts.addAction(self.ActionTransferAccountToNextDm)
			self.MenuAccounts.addAction(self.ActionSwitchAccountPriority)

		elif self.processing_group:
			self.MenuAccounts.addSection(self.processing_group)
			self.MenuAccounts.addAction(self.ActionEditGroupName)
			self.MenuAccounts.addAction(self.ActionCreateAccount)
		else                      :
			self.MenuAccounts.addAction(self.ActionCreateAccount)

		self.MenuAccounts.addSection("Управление")
		self.MenuAccounts.addMenu(self.SubmenuAccounts)

		if self.processing_group:
			self.MenuAccounts.addMenu(self.SubmenuGroup)

		if self.processing_ido:
			self.MenuAccounts.addMenu(self.SubmenuAccount)

	def AdjustMenuAccounts_Enable(self):
		""" Меню Счета: Настройка доступности """
		flag_exists_accounts  : bool = self.ModelData.rowCount()

		self.ActionResetAccounts.setEnabled(flag_exists_accounts)

	def AdjustMenuAccounts_Text(self):
		""" Меню Счета: Настройка текста """
		account = C90_Account(self.processing_ido)

		self.SubmenuGroup.setTitle(self.processing_group)
		self.SubmenuAccount.setTitle(account.name)

		self.ActionSwitchAccountPriority.setText("Установить приоритетным" if (account.priority == 0) else "Отменить приоритетность")

	def ShowMenuAccounts(self):
		""" Отображение меню Счета """
		self.MenuAccounts.exec_(QCursor().pos())

	# Дерево данных
	def AdjustTreeData_Color(self):
		""" Дерево Данных: Настройка цвета """
		self.ModelData.adjustGroupView(True, True, True)

	def AdjustTreeData_Expand(self):
		""" Дерево Данных: Настройка раскрытия """
		self.TreeData.expandAll()

	def AdjustTreeData_Size(self):
		""" Дерево Данных: Настройка размера """
		self.TreeData.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

		for idx_column in range(1, 4):
			self.TreeData.header().setSectionResizeMode(idx_column, QHeaderView.ResizeMode.Fixed)
			self.TreeData.setColumnWidth(idx_column, 100)

	def AdjustTreeData_Sort(self):
		""" Дерево Данных: Настройка сортировки """
		self.TreeData.sortByColumn(0, Qt.SortOrder.AscendingOrder)

	def ControlProcessingIdp(self):
		""" Контроль рабочего IDP """
		account = C90_Account()

		if   bool(self.processing_ido):
			if   self.processing_idp == account.FName.Idp().data          : self.on_RequestEditAccountName()
			elif self.processing_idp == account.FInitialBalance.Idp().data: self.on_RequestEditAccountInitialBalance()

		elif bool(self.processing_group):
			self.on_RequestEditGroupName()

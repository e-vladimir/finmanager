# ФОРМА ОПЕРАЦИИ: МЕХАНИКА УПРАВЛЕНИЯ
# 11 мар 2025

from PySide6.QtGui      import QCursor, Qt
from PySide6.QtWidgets  import QHeaderView

from L20_PySide6        import ROLES
from L60_form_operation import C60_FormOperation
from L90_operations     import C90_Operation


class C70_FormOperation(C60_FormOperation):
	""" Форма Операции: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Операции - {self.Workspace.DmDyToString()}")

	# Меню операций
	def AdjustMenuOperations(self):
		""" Настройка меню операций """
		self.MenuOperation.clear()

		if self.processing_ido:
			self.MenuOperation.addAction(self.ActionEditOperationAmount)
			self.MenuOperation.addAction(self.ActionEditOperationAccounts)
			self.MenuOperation.addAction(self.ActionEditOperationDescription)
			self.MenuOperation.addSeparator()
			self.MenuOperation.addAction(self.ActionSetOperationColorBlack)
			self.MenuOperation.addAction(self.ActionSetOperationColorGray)
			self.MenuOperation.addAction(self.ActionSetOperationColorGreen)
			self.MenuOperation.addAction(self.ActionSetOperationColorBlue)
			self.MenuOperation.addAction(self.ActionSetOperationColorRed)
			self.MenuOperation.addSeparator()
			self.MenuOperation.addAction(self.ActionCreateOperation)
			self.MenuOperation.addSeparator()

		self.MenuOperation.addAction(self.ActionCreateOperation)
		self.MenuOperation.addAction(self.ActionImportOperations)
		self.MenuOperation.addSeparator()

		self.MenuOperation.addMenu(self.SubmenuOperations)

		if self.processing_ido:
			self.MenuOperation.addMenu(self.SubmenuOperation)

	def AdjustMenuOperation_Enable(self):
		""" Настройка меню операций: Доступность """
		pass

	def AdjustMenuOperation_Text(self):
		""" Настройка меню операций: Название """
		pass

	def ShowMenuOperation(self):
		""" Отображению меню операций """
		self.MenuOperation.exec_(QCursor().pos())

	# Дерево данных
	def ControlOperationIdp(self):
		""" Контроль рабочего IDP при двойном клике по дереву данных """
		if not self.processing_ido: return

		operation             = C90_Operation()
		idp_amount      : str = operation.FAmount.Idp().data
		idp_accounts    : str = operation.FAccountIdos.Idp().data
		idp_description : str = operation.FDescription.Idp().data

		if   self.processing_idp == idp_amount     : self.on_RequestEditOperationAmount()
		elif self.processing_idp == idp_accounts   : self.on_RequestEditOperationAccounts()
		elif self.processing_idp == idp_description: self.on_RequestEditOperationDescriptions()

	def AdjustTreeData_Sort(self):
		""" Настройка дерева данных: Сортировка """
		self.ModelData.setSortRole(ROLES.SORT_INDEX)
		self.ModelData.sort(0, Qt.SortOrder.AscendingOrder)

	def AdjustTreeData_Expand(self):
		""" Настройка дерева данных: Раскрытие """
		self.TreeData.expandAll()

	def AdjustTreeData_Colors(self):
		""" Настройка дерева данных: Цветовая схема """
		self.ModelData.adjustGroupView(True, True, True)

	def AdjustTreeData_Size(self):
		""" Настройка дерева данных: Размеры """
		self.TreeData.resizeColumnToContents(0)
		self.TreeData.resizeColumnToContents(1)

		self.TreeData.header().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

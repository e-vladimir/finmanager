# ФОРМА ОПЕРАЦИИ: МЕХАНИКА УПРАВЛЕНИЯ
# 11 мар 2025

from PySide6.QtGui      import QCursor, Qt

from L20_PySide6        import ROLES
from L60_form_operation import C60_FormOperation


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

		self.MenuOperation.addMenu(self.SubmenuOperations)

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

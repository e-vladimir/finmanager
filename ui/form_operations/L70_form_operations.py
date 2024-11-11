# ФОРМА ФИНАНСОВЫЕ ОПЕРАЦИИ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui       import QCursor

from G10_math_linear     import CalcBetween

from L60_form_operations import C60_FormOperations


class C70_FormOperations(C60_FormOperations):
	""" Форма Финансовые операции: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Финансовые операции - {self.workspace.DmDyToString()}")

	# Дерево данных
	def AdjustTreeData_Size(self):
		""" Настройка дерева данных: Размеры """
		sizes_min : list[int] = [ 75, 200, 200]
		sizes_max : list[int] = [100, 300, 300]

		for index_col in range(self.model_data.columnCount() - 1):
			self.tree_data.resizeColumnToContents(index_col)

			column_size : int = self.tree_data.columnWidth(index_col)
			column_size       = CalcBetween(sizes_min[index_col], column_size, sizes_max[index_col])

			self.tree_data.setColumnWidth(index_col, column_size)

	def AdjustTreeData_Color(self):
		""" Настройка дерева данных: Цвета """
		self.model_data.adjustGroupView(True, True, True)

	def AdjustTreeData_Expand(self):
		""" Настройка дерева данных: Раскрытие """
		self.tree_data.expandAll()

	# Меню Финансовые операции
	def AdjustMenuOperations_Text(self):
		""" Меню операций по счетам: Настройка текста """
		pass

	def AdjustMenuOperations_Enable(self):
		""" Меню операций по счетам: Настройка доступности """
		pass

	def ShowMenuOperations(self):
		""" Меню операций по счетам: Отображение """
		self.menu_operations.exec_(QCursor().pos())

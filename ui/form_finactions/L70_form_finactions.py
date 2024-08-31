# ФОРМА ФИНДЕЙСТВИЯ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui       import QCursor

from G10_math_linear     import CalcBetween

from L60_form_finactions import C60_FormFinactions


class C70_FormFinactions(C60_FormFinactions):
	""" Форма Финдействия: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Финдействия - {self.workspace.DmDyToString()}")

	# Меню финдействий
	def AdjustMenuFinactionsEnable(self):
		""" Меню финдействий: Настройка доступности """
		pass

	def AdjustMenuFinactionsText(self):
		""" Меню финдействий: Настройка наименования """
		pass

	def ShowMenuFinactions(self):
		""" Меню финдействий: Отображение """
		self.menu_finactions.exec_(QCursor().pos())

	# Дерево данных
	def AdjustTreeData_Size(self):
		""" Дерево данных: Настройка размера """
		sizes_min : list[int] = [100, 100, 100]
		sizes_max : list[int] = [100, 200, 250]

		for index_col in range(self.model_data.columnCount() - 1):
			self.tree_data.resizeColumnToContents(index_col)

			col_size : int = self.tree_data.columnWidth(index_col)
			col_size       = CalcBetween(sizes_min[index_col], col_size, sizes_max[index_col])

			self.tree_data.setColumnWidth(index_col, col_size)

	def AdjustTreeData_Expand(self):
		""" Дерево данных: Настройка раскрытия """
		self.tree_data.expandAll()

	def AdjustTreeData_Color(self):
		""" Дерево данных: Настройка цветовой палитры """
		self.model_data.setGroupsView(True, True, True)

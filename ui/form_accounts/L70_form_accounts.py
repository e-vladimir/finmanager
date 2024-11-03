# ФОРМА СЧЕТА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui     import Qt

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

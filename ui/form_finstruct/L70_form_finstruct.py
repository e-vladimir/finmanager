# ФОРМА ФИНСТРУКТУРА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore     import Qt

from L60_form_finstruct import C60_FormFinstruct


class C70_FormFinstruct(C60_FormFinstruct):
	""" Форма Финструктура: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Финструктура - {self.workspace.DmDyToString()}")

	# Дерево финструктуры
	def AdjustTreeDataSort(self):
		""" Настройка сортировки данных в дереве финструктуры """
		self.tree_data.sortByColumn(0, Qt.SortOrder.AscendingOrder)

	def AdjustTreeDataExpand(self):
		""" Настройка раскрытия данных в дереве финструктуры """
		self.tree_data.expandAll()

	def AdjustTreeDataColors(self):
		""" Настройка цветовой схемы дерева финструктуры """
		self.model_data.setGroupsView(True, True)

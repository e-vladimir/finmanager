# ФОРМА ФИНСТАТИСТИКА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore        import QModelIndex, Qt
from PySide6.QtWidgets     import QHeaderView

from L60_form_finstatistic import C60_FormFinstatistic


class C70_FormFinstatistic(C60_FormFinstatistic):
	""" Форма Финстатистика: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Финстатистика - {self.workspace.DmDyToString()}")

	# Дерево финстатистики
	def AdjustTreeFinstatisticSize(self):
		""" Настройка размеров дерева финстатистики """
		self.tree_finstatistic.setColumnWidth(2, 100)
		self.tree_finstatistic.setColumnWidth(1, 100)

		self.tree_finstatistic.header().setSectionResizeMode(0, QHeaderView.Stretch)

	def AdjustTreeFinstatisticExpand(self):
		""" Настройка раскрытия дерева финстатистики """
		self.tree_finstatistic.expandAll()

	def HideZeroRowsInTreeFinstatistic(self):
		""" Скрытие нулевых строк в дереве финстатистики """
		flag_iteration : bool = True

		while flag_iteration:
			flag_iteration = False

			for index_finstatistic in self.model_finstatistic.indexes():
				if not index_finstatistic.isValid()   : continue

				index_parent          : QModelIndex = index_finstatistic.parent()
				index_row             : int         = index_finstatistic.row()

				subindex_finstatistic : QModelIndex = index_finstatistic.sibling(0, 0)
				if     subindex_finstatistic.isValid(): continue

				index_income          : QModelIndex = self.model_finstatistic.index(index_row, 1, index_parent)
				index_outcome         : QModelIndex = self.model_finstatistic.index(index_row, 2, index_parent)

				amount_income         : str         = index_income.data(Qt.DisplayRole)
				amount_outcome        : str         = index_outcome.data(Qt.DisplayRole)

				if not (amount_income == "0" and amount_outcome == "0"): continue

				self.model_finstatistic.removeRow(index_row, index_parent)

				flag_iteration = True

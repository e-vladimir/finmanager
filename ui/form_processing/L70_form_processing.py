# ФОРМА ОБРАБОТКА ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui       import QColor, QCursor, Qt
from PySide6.QtWidgets   import QHeaderView

from L00_form_processing import OPERATIONS
from L60_form_processing import C60_FormProcessing


class C70_FormProcessing(C60_FormProcessing):
	""" Форма Обработка данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Обработка данных - {self.workspace.DmDyToString()}")

	# Дерево данных Обработка операций
	def AdjustTreeDataOperations_Size(self):
		""" Настройка размеров дерева данных Обработка операций """
		self.tree_data_operations.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
		self.tree_data_operations.header().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

		self.tree_data_operations.resizeColumnToContents(0)

	def AdjustTreeDataOperations_Expand(self):
		""" Дерево параметров Обработка операций: Настройка вложенности """
		self.tree_data_operations.expandAll()

	def AdjustTreeDataOperations_Color(self):
		""" Настройка цветовой схемы дерева данных Обработка операций """
		color_disable = QColor(200, 200, 200)
		color_enable  = QColor(  0,   0,   0)

		self.model_operations.adjustGroupView(True, True, True)

		indexes     = self.model_operations.indexesInRowByIdo(OPERATIONS.INCLUDE)
		item_value  = self.model_operations.itemFromIndex(indexes[0])
		idx_row     = item_value.row()
		item_parent = item_value.parent()
		self.model_operations.setRowColor(item_parent, idx_row, color_fg=color_enable if self._operations_include else color_disable)

		indexes     = self.model_operations.indexesInRowByIdo(OPERATIONS.EXCLUDE)
		item_value  = self.model_operations.itemFromIndex(indexes[0])
		idx_row     = item_value.row()
		item_parent = item_value.parent()
		self.model_operations.setRowColor(item_parent, idx_row, color_fg=color_enable if self._operations_exclude else color_disable)

		indexes     = self.model_operations.indexesInRowByIdo(OPERATIONS.DESTINATION)
		item_value  = self.model_operations.itemFromIndex(indexes[0])
		idx_row     = item_value.row()
		item_parent = item_value.parent()
		self.model_operations.setRowColor(item_parent, idx_row, color_fg=color_enable if item_value.checkState() == Qt.CheckState.Checked else color_disable)

		indexes     = self.model_operations.indexesInRowByIdo(OPERATIONS.DETAIL)
		item_value  = self.model_operations.itemFromIndex(indexes[0])
		idx_row     = item_value.row()
		item_parent = item_value.parent()
		self.model_operations.setRowColor(item_parent, idx_row, color_fg=color_enable if item_value.checkState() == Qt.CheckState.Checked else color_disable)

		indexes     = self.model_operations.indexesInRowByIdo(OPERATIONS.OBJECT_INT)
		item_value  = self.model_operations.itemFromIndex(indexes[0])
		idx_row     = item_value.row()
		item_parent = item_value.parent()
		self.model_operations.setRowColor(item_parent, idx_row, color_fg=color_enable if item_value.checkState() == Qt.CheckState.Checked else color_disable)

		indexes     = self.model_operations.indexesInRowByIdo(OPERATIONS.OBJECT_EXT)
		item_value  = self.model_operations.itemFromIndex(indexes[0])
		idx_row     = item_value.row()
		item_parent = item_value.parent()
		self.model_operations.setRowColor(item_parent, idx_row, color_fg=color_enable if item_value.checkState() == Qt.CheckState.Checked else color_disable)

		indexes     = self.model_operations.indexesInRowByIdo(OPERATIONS.COLOR)
		item_value  = self.model_operations.itemFromIndex(indexes[0])
		idx_row     = item_value.row()
		item_parent = item_value.parent()
		self.model_operations.setRowColor(item_parent, idx_row, color_fg=color_enable if item_value.checkState() == Qt.CheckState.Checked else color_disable)

	def ProcessingTreeDataOperations_DbClick(self):
		""" Обработка двойного клика по дереву данных Обработка операций """
		match self._processing_ido:
			case OPERATIONS.INCLUDE    : self.on_RequestEditOperationsInclude()
			case OPERATIONS.EXCLUDE    : self.on_RequestEditOperationsExclude()
			case OPERATIONS.DESTINATION: self.on_RequestEditOperationsDestination()
			case OPERATIONS.DETAIL     : self.on_RequestEditOperationsDetail()
			case OPERATIONS.OBJECT_INT : self.on_RequestEditOperationsObjectInt()
			case OPERATIONS.OBJECT_EXT : self.on_RequestEditOperationsObjectExt()
			case OPERATIONS.COLOR      : self.on_RequestEditOperationsColor()
			case OPERATIONS.INTERVAL   : self.on_RequestEditOperationsInterval()

	# Меню Обработка операций
	def AdjustMenuOperations_Text(self):
		""" Настройка элементов меню Обработка операций """
		pass

	def AdjustMenuOperations_Enable(self):
		""" Настройка доступности меню Обработка операций """
		self.action_operations_processing.setEnabled(bool(self._operations_include.strip()))

	def ShowMenuOperations(self):
		""" Отображение меню Обработка операций """
		self.menu_operations.exec_(QCursor().pos())

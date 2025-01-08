# ФОРМА АНАЛИТИКА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore     import Qt
from PySide6.QtGui      import QCursor
from PySide6.QtWidgets  import QHeaderView

from L60_form_analytics import C60_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C70_FormAnalytics(C60_FormAnalytics):
	""" Форма Аналитика: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка """
		self.setWindowTitle(f"Аналитика - {self.workspace.DmDyToString()}")

	# Таблица элементов аналитики
	def AdjustTableItems_Size(self):
		""" Таблица элементов аналитики: Настройка размера """
		self.table_items.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.table_items.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
		self.table_items.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)

		self.table_items.setColumnWidth(1, 200)
		self.table_items.setColumnWidth(2, 200)

		self.table_items.resizeRowsToContents()

		for idx_row in range(self.model_items.rowCount()):
			self.table_items.setRowHeight(idx_row, 25 * (self.table_items.rowHeight(idx_row) // 25))

	def AdjustTableItems_Sort(self):
		""" Таблица элементов аналитики: Сортировка """
		self.table_items.sortByColumn(0, Qt.SortOrder.AscendingOrder)

	def ProcessingTableItems_DbClick(self):
		""" Таблица Элементы аналитики """
		if not self._processing_ido: return

		match self._processing_column:
			case 0: self.on_RequestEditNameAnalyticsItem()
			case 1: self.on_RequestEditIncludeAnalyticsItem()
			case 2: self.on_RequestEditExcludeAnalyticsItem()

	# Меню Элементы аналитики
	def AdjustMenuItems_Text(self):
		""" Меню Элементы аналитики: Настройка текста """
		self.submenu_items_item.setTitle("Элемент аналитики")

		if self._processing_ido:
			analytics_item = C90_AnalyticsItem(self._processing_ido)
			self.submenu_items_item.setTitle(analytics_item.Name())

	def AdjustMenuItems_Enable(self):
		""" Меню Элементы аналитики: Настройка доступности """
		flag_selected : bool = bool(self._processing_ido)

		self.action_items_item_edit_name.setEnabled(flag_selected)
		self.action_items_item_edit_include.setEnabled(flag_selected)
		self.action_items_item_edit_exclude.setEnabled(flag_selected)
		self.action_items_item_delete.setEnabled(flag_selected)

	def ShowMenuItems(self):
		""" Меню Элементы аналитики: Отображение """
		self.menu_items.exec_(QCursor().pos())

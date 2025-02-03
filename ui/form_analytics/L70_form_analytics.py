# ФОРМА АНАЛИТИКА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore     import Qt
from PySide6.QtGui      import QCursor
from PySide6.QtWidgets  import QHeaderView

from L00_form_analytics import ANALYTICS
from L60_form_anaytics  import C60_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C70_FormAnalytics(C60_FormAnalytics):
	""" Форма Аналитика: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Аналитика - {self.workspace.DmDyToString()}")

	# Список элементов аналитики
	def AdjustListItems_Sort(self):
		""" Список элементов аналитики: Настройка сортировки """
		self.model_items.sort(0, Qt.SortOrder.AscendingOrder)

	# Дерево параметров элемента аналитики
	def AdjustTreeDataItem_Size(self):
		""" Дерево парамеров элемент аналитики: Настройка размеров """
		self.tree_data_item.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.tree_data_item.header().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

	def AdjustTreeDataItem_Expand(self):
		""" Дерево параметров элемент аналитики: Настройка вложенности """
		self.tree_data_item.expandAll()

	def AdjustTreeDataItem_Color(self):
		""" Дерево параметров элемент аналитики: Настройка цветовой схемы """
		self.model_item.adjustGroupView(True, True, True)

	def ProcessingTreeDataItem_DbClick(self):
		""" Обработка двойного клика по дереву параметров элемента аналитики """
		match self._processing_ido:
			case ANALYTICS.INCLUDE: self.on_RequestEditAnalyticsItemInclude()
			case ANALYTICS.EXCLUDE: self.on_RequestEditAnalyticsItemExclude()
			case ANALYTICS.UNIT   : self.on_RequestEditAnalyticsItemMeasurementUnit()
			case ANALYTICS.VALUE  : self.on_RequestEditAnalyticsItemMeasurementValue()

	# Меню Элементы аналитики
	def AdjustMenuItems_Enable(self):
		""" Настройка доступности меню Элементы аналитики """
		flag_selected = bool(self._processing_ido)

		self.action_items_edit_item_name.setEnabled(flag_selected)
		self.action_items_delete_item.setEnabled(flag_selected)

	def AdjustMenuItems_Text(self):
		""" Настройка текстов меню Элементы аналитики """
		analytics_item = C90_AnalyticsItem(self._processing_ido)

		self.submenu_items_item.setTitle(analytics_item.Name() or "Элемент аналитики")

	def ShowMenuItems(self):
		""" Отображение меню Элементы аналитики """
		self.menu_items_items.exec_(QCursor().pos())

	# Дерево данных Структура месяца
	def AdjustTreeDataDm_Size(self):
		""" Настройка размеров дерева данных Структура месяца """
		self.tree_data_dm.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.tree_data_dm.header().setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
		self.tree_data_dm.header().setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)

		self.tree_data_dm.setColumnWidth(1, 100)
		self.tree_data_dm.setColumnWidth(2, 100)

	def AdjustTreeDataDm_Expand(self):
		""" Дерево параметров Структура месяца: Настройка вложенности """
		self.tree_data_dm.expandAll()

	def AdjustTreeDataDm_Color(self):
		""" Настройка цветовой схемы дерева данных Структура месяца """
		self.model_dm.adjustGroupView(True, True, True)

	def AdjustTreeDataDm_Sort(self):
		""" Настройка сортировки дерева данных Структура месяца """
		self.tree_data_dm.sortByColumn(0, Qt.SortOrder.AscendingOrder)

	# Дерево данных Динамика
	def AdjustTreeDataDy_Size(self):
		""" Настройка размеров дерева данных Структура месяца """
		self.tree_data_dy.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.tree_data_dy.header().setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
		self.tree_data_dy.header().setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)

		self.tree_data_dy.setColumnWidth(1, 100)
		self.tree_data_dy.setColumnWidth(2, 100)

	def AdjustTreeDataDy_Expand(self):
		""" Дерево параметров Структура месяца: Настройка вложенности """
		self.tree_data_dy.expandAll()

	def AdjustTreeDataDy_Color(self):
		""" Настройка цветовой схемы дерева данных Структура месяца """
		self.model_dy.adjustGroupView(True, True, True)

	# Панель вкладок
	def AdjustTabsMain_Text(self):
		""" Настройка заголовков вкладок """
		self.tabs_main.setTabText(2, f"Динамика{' - ' + self._processing_object if self._processing_object else ''}")
		self.tabs_main.setTabText(3, f"Аналитика{' - ' + self._processing_object if self._processing_object else ''} ({self._processing_mode})")

	def SwitchTabsMainToFirst(self):
		""" Переключение вкладок """
		self.tabs_main.setCurrentIndex(0)

	# Дерево данных Аналитика
	def AdjustTreeDataAnalytics_Size(self):
		""" Дерево данных аналитики: Настройка размеров """
		self.tree_data_analytics.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.tree_data_analytics.header().setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
		self.tree_data_analytics.header().setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
		self.tree_data_analytics.header().setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
		self.tree_data_analytics.header().setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)

		self.tree_data_analytics.setColumnWidth(1, 75)
		self.tree_data_analytics.setColumnWidth(2, 75)
		self.tree_data_analytics.setColumnWidth(3, 75)
		self.tree_data_analytics.setColumnWidth(4, 75)

	def AdjustTreeDataAnalytics_Expand(self):
		""" Дерево данных аналитики: Настройка вложенности """
		self.tree_data_analytics.expandAll()

	def AdjustTreeDataAnalytics_Color(self):
		""" Дерево данных аналитики: Настройка цветовой схемы """
		self.model_analytics.adjustGroupView(True, True, True)


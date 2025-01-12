# ФОРМА АНАЛИТИКА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui      import QCursor, Qt
from PySide6.QtWidgets  import QHeaderView

from L00_form_analytics import IDOS_ANALYTICS
from L60_form_analytics import C60_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C70_FormAnalytics(C60_FormAnalytics):
	""" Форма Аналитика: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Аналитика - {self.workspace.DmDyToString()}")

	# Вкладки
	def SwitchTabsToOptions(self):
		""" Переключение на вкладку Параметры """
		self.tabs_data.setCurrentIndex(0)

	# Меню Элементы аналитики
	def AdjustMenuItems_Text(self):
		""" Меню Элементы аналитики: Настройка текста """
		analytics_item = C90_AnalyticsItem(self._processing_ido)

		self.submenu_items_item.setTitle(analytics_item.Name() or "Элемент аналитики")

	def AdjustMenuItems_Enable(self):
		""" Меню Элементы аналитики: Настройка доступности """
		flag_selected : bool = bool(self._processing_ido)

		self.action_items_item_edit_name.setEnabled(flag_selected)
		self.action_items_item_delete.setEnabled(flag_selected)

	def ShowMenuItems(self):
		""" Меню Элементы аналитики: Отображение """
		self.menu_items.exec_(QCursor().pos())

	# Меню Параметры
	def AdjustMenuOptions_Text(self):
		""" Меню Параметры: Настройка текста """
		pass

	def AdjustMenuOptions_Enable(self):
		""" Меню Параметры: Настройка доступности """
		flag_selected : bool = bool(self._processing_ido)

		self.action_options_edit_include.setEnabled(flag_selected)
		self.action_options_edit_exclude.setEnabled(flag_selected)

	def ShowMenuOptions(self):
		""" Меню Параметры: Отображение меню """
		self.menu_options.exec_(QCursor().pos())

	# Дерево параметров
	def AdjustTreeOptions_Size(self):
		""" Дерево данных Параметры: Настройка размеров """
		self.tree_data_options.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.tree_data_options.header().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

	def AdjustTreeOptions_Expand(self):
		""" Дерево данных Параметры: Настройка раскрытия """
		self.tree_data_options.expandAll()

	def AdjustTreeOptions_Color(self):
		""" Дерево данных Параметры: Настройка цвета """
		self.model_data_options.adjustGroupView(True, True)

	def ProcessingTreeOptions_DbClick(self):
		""" Дерево параметров: Обработка двойного клика """
		match self._processing_ido:
			case IDOS_ANALYTICS.INCLUDE: self.on_RequestEditOptionsInclude()
			case IDOS_ANALYTICS.EXCLUDE: self.on_RequestEditOptionsExclude()

	# Список элементов аналитики
	def AdjustListItems_Sort(self):
		""" Список элементы аналитики: Сортировка """
		self.model_items.sort(0, Qt.SortOrder.AscendingOrder)

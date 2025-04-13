# ФОРМА АНАЛИТИКА ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ
# 11 апр 2025

from PySide6.QtCore     import Qt
from PySide6.QtGui      import QCursor
from PySide6.QtWidgets  import QHeaderView

from L00_form_analytics import ANALYTICS_FIELDS
from L60_form_analytics import C60_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C70_FormAnalytics(C60_FormAnalytics):
	""" Форма Аналитика данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Аналитика данных - {self.Workspace.DmDyToString()}")


	# Список элементов аналитики
	def AdjustListItems_Sort(self):
		""" Настройка сортировки списка элементов аналитики """
		self.ModelDataItems.sort(0, Qt.SortOrder.AscendingOrder)


	# Меню Элементы аналитики
	def AdjustMenuItems(self):
		""" Настройка меню элементов аналитики """
		if self.processing_ido:
			self.MenuItems.addAction(self.ActionEditItemName)
			self.MenuItems.addAction(self.ActionDeleteItem)
			self.MenuItems.addSeparator()

		self.MenuItems.addAction(self.ActionCreateItem)

	def AdjustMenuItems_Text(self):
		""" Настройка заголовков меню элементов аналитики """
		analytics_item = C90_AnalyticsItem(self.processing_ido)

		self.ActionEditItemName.setText(f"Переименовать {analytics_item.name}")
		self.ActionDeleteItem.setText(f"Удалить {analytics_item.name}")

	def AdjustMenuItems_Enable(self):
		""" Настройка доступности меню элементов аналитики """
		pass

	def ShowMenuItems(self):
		""" Отображению меню элементов аналитики """
		self.MenuItems.exec_(QCursor().pos())


	# Меню Элемент аналитики
	def AdjustMenuItem(self):
		""" Настройка меню элементов аналитики """
		self.MenuItem.clear()

		if not self.processing_ido: return

		self.MenuItem.addAction(self.ActionEditItemName)
		self.MenuItem.addSeparator()
		self.MenuItem.addAction(self.ActionEditItemInclude)
		self.MenuItem.addAction(self.ActionEditItemExclude)

	def AdjustMenuItem_Text(self):
		""" Настройка заголовков меню элементов аналитики """
		pass

	def AdjustMenuItem_Enable(self):
		""" Настройка доступности меню элементов аналитики """
		pass

	def ShowMenuItem(self):
		""" Отображению меню элементов аналитики """
		self.MenuItem.exec_(QCursor().pos())


	# Основные вкладки
	def SwitchTabsMainToItems(self):
		""" Переключение вкладки на Элементы аналитики """
		self.TabsMain.setCurrentIndex(0)


	# Дерево параметров элемента аналитики
	def AdjustTreeDataItem_Color(self):
		""" Настройка цветовой схемы дерева параметров элемента аналитики """
		self.ModelDataItem.adjustGroupView(True, True, True)

	def AdjustTreeDataItem_Expand(self):
		""" Настройка раскрытия дерева параметров элемента аналитики """
		self.TreeDataItem.expandAll()

	def AdjustTreeDataItem_Size(self):
		""" Настройка размеров дерева параметров элемента аналитики """
		self.TreeDataItem.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.TreeDataItem.header().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)


	# Элемент аналитики
	def EditItem(self):
		""" Редактирование элемента аналитики """
		match self.processing_field:
			case ANALYTICS_FIELDS.INCLUDE: self.on_RequestEditItemInclude()
			case ANALYTICS_FIELDS.EXCLUDE: self.on_RequestEditItemExclude()

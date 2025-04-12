# ФОРМА АНАЛИТИКА ДАННЫХ: МОДЕЛЬ UI
# 11 апр 2025

from PySide6.QtGui      import QAction, QIcon
from PySide6.QtWidgets  import QMenu

from L20_PySide6        import C20_PySideForm
from L40_form_analytics import Ui_FormAnalytics


class C41_FormAnalytics(C20_PySideForm, Ui_FormAnalytics):
	""" Форма Аналитика данных: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuItems()

	def InitMenuItems(self):
		""" Инициализация меню элементов аналитики """
		icon_item_plus   = QIcon("./L0/icons/item_plus.svg")
		icon_item_delete = QIcon("./L0/icons/item_delete.svg")
		icon_edit        = QIcon("./L0/icons/edit.svg")

		self.ActionCreateItem   = QAction(icon_item_plus,   "Создать элемент аналитики")
		self.ActionDeleteItem   = QAction(icon_item_delete, "Удалить элемент аналитики")
		self.ActionEditItemName = QAction(icon_edit,        "Переименовать элемент аналитики")

		self.MenuItems        = QMenu("Элементы аналитики")
		self.MenuItems.addAction(self.ActionCreateItem)

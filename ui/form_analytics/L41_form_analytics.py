# ФОРМА АНАЛИТИКА: МОДЕЛЬ UI

from PySide6.QtGui      import QAction, QIcon
from PySide6.QtWidgets  import QMenu

from L20_PySide6        import C20_PySideForm
from L40_form_analytics import Ui_frm_analytics


class C41_FormAnalytics(C20_PySideForm, Ui_frm_analytics):
	""" Форма Аналитика: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		""" Инициализацию меню """
		self.InitMenuItems()
		self.InitMenuItem()

	def InitMenuItems(self):
		""" Инициализацию меню Элементы аналитики """
		icon_item_plus   = QIcon("./L0/icons/item_plus.svg")
		icon_item_delete = QIcon("./L0/icons/item_delete.svg")
		icon_edit        = QIcon("./L0/icons/edit.svg")
		icon_grid_1_3    = QIcon("./L0/icons/grid_1_3.svg")
		icon_grid_3_3    = QIcon("./L0/icons/grid_3_3.svg")

		self.action_items_create_item       = QAction(icon_item_plus,   "Создать элемент аналитики")
		self.action_items_delete_item       = QAction(icon_item_delete, "Удалить")
		self.action_items_edit_item_name    = QAction(icon_edit,        "Редактировать название")

		self.menu_items_items               = QMenu("Элементы аналитики")
		self.submenu_items_items            = self.menu_items_items.addMenu(icon_grid_1_3, "Элементы аналитики")
		self.submenu_items_items.addAction(self.action_items_create_item)

		self.submenu_items_item            = self.menu_items_items.addMenu(icon_grid_3_3, "Элемент аналитики")
		self.submenu_items_item.addAction(self.action_items_edit_item_name)
		self.submenu_items_item.addSeparator()
		self.submenu_items_item.addAction(self.action_items_delete_item)

	def InitMenuItem(self):
		""" Инициализация меню Элемент аналитики """
		pass

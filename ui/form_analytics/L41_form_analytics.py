# ФОРМА АНАЛИТИКА: МОДЕЛЬ UI

from PySide6.QtGui      import QAction, QIcon
from PySide6.QtWidgets  import QMenu

from L20_PySide6        import C20_PySideForm
from L40_form_analytics import Ui_form_analytics


class C41_FormAnalytics(C20_PySideForm, Ui_form_analytics):
	""" Форма Аналитика: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuItems()
		self.InitMenuOptions()

	def InitMenuItems(self):
		""" Инициализация меню Элементы аналитики """
		icon_grid_1_3    = QIcon("./L0/icons/grid_1_3.svg")
		icon_grid_3_3    = QIcon("./L0/icons/grid_3_3.svg")
		icon_edit        = QIcon("./L0/icons/edit.svg")
		icon_item_plus   = QIcon("./L0/icons/item_plus.svg")
		icon_item_delete = QIcon("./L0/icons/item_delete.svg")

		self.action_items_create_item    = QAction(icon_item_plus,   "Создать элемент аналитики")
		self.action_items_item_edit_name = QAction(icon_edit,        "Редактирование название")
		self.action_items_item_delete    = QAction(icon_item_delete, "Удалить")

		self.menu_items                  = QMenu("")
		self.submenu_items               = self.menu_items.addMenu(icon_grid_1_3, "Элементы аналитики")
		self.submenu_items.addAction(self.action_items_create_item)

		self.submenu_items_item          = self.menu_items.addMenu(icon_grid_3_3, "Элемент аналитики")
		self.submenu_items_item.addAction(self.action_items_item_edit_name)
		self.submenu_items_item.addSeparator()
		self.submenu_items_item.addAction(self.action_items_item_delete)

	def InitMenuOptions(self):
		""" Инициализация меню Параметры """
		icon_blocks    = QIcon("./L0/icons/blocks.svg")
		icon_checked   = QIcon("./L0/icons/checked_check.svg")
		icon_unchecked = QIcon("./L0/icons/checked_uncheck.svg")

		self.action_options_edit_include = QAction(icon_checked,   "Редактировать параметры включения")
		self.action_options_edit_exclude = QAction(icon_unchecked, "Редактировать параметры исключения")

		self.menu_options = QMenu("Параметры")
		self.submenu_option_main = self.menu_options.addMenu(icon_blocks, "Параметры основные")
		self.submenu_option_main.addAction(self.action_options_edit_include)
		self.submenu_option_main.addAction(self.action_options_edit_exclude)

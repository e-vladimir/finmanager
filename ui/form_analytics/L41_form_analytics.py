# ФОРМА АНАЛИТИКА ДАННЫХ: МОДЕЛЬ UI
# 27 апр 2025

from PySide6.QtGui      import QAction, QIcon
from PySide6.QtWidgets  import QMenu

from L20_PySide6        import C20_PySideForm
from L40_form_analytics import Ui_FormAnalytics


class C41_FormAnalytics(Ui_FormAnalytics, C20_PySideForm):
	""" Форма Аналитика данных: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuStruct()

	def InitMenuStruct(self):
		""" Инициализация меню структуры """
		icon_grid_1_3    = QIcon("./L0/icons/grid_1_3.svg")
		icon_grid_2_2    = QIcon("./L0/icons/grid_2_2.svg")
		icon_grid_3_3    = QIcon("./L0/icons/grid_3_3.svg")
		icon_edit        = QIcon("./L0/icons/edit.svg")
		icon_item_plus   = QIcon("./L0/icons/item_plus.svg")
		icon_item_delete = QIcon("./L0/icons/item_delete.svg")
		icon_square_plus = QIcon("./L0/icons/square_plus.svg")
		icon_reload      = QIcon("./L0/icons/reload.svg")

		self.ActionResetDestinations        = QAction(icon_reload,      "Сбросить данные")

		self.ActionCreateTopDestination     = QAction(icon_item_plus,   "Создать общее назначение")
		self.ActionCreateDestination        = QAction(icon_item_plus,   "Уточнить назначение")
		self.ActionCreateSubDestination     = QAction(icon_square_plus, "Уточнить назначение")
		self.ActionEditDestinationName      = QAction(icon_edit,        "Редактировать название")
		self.ActionDeleteDestination        = QAction(icon_item_delete, "Удалить назначение")

		self.MenuStruct                     = QMenu("Структура аналитики")
		self.SubmenuStruct                  = QMenu("Структура аналитики", icon=icon_grid_1_3)
		self.SubmenuStruct.addAction(self.ActionCreateTopDestination)
		self.SubmenuStruct.addSeparator()
		self.SubmenuStruct.addAction(self.ActionResetDestinations)

		self.SubmenuStructGroup             = QMenu("Группа назначения",   icon=icon_grid_2_2)
		self.SubmenuStructGroup.addAction(self.ActionCreateDestination)

		self.SubmenuStructItem              = QMenu("Назначение",          icon=icon_grid_3_3)
		self.SubmenuStructItem.addAction(self.ActionCreateSubDestination)
		self.SubmenuStructItem.addSeparator()
		self.SubmenuStructItem.addAction(self.ActionEditDestinationName)
		self.SubmenuStructItem.addSeparator()
		self.SubmenuStructItem.addAction(self.ActionDeleteDestination)

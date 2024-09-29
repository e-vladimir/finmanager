# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МОДЕЛЬ UI

from PySide6.QtGui     import QIcon, QAction
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_rules    import Ui_form_rules


class C41_FormRules(C20_PySideForm, Ui_form_rules):
	""" Форма Правила обработки данных: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuRules()

	def InitMenuRules(self):
		""" Инициализацию меню правил обработки данных """
		icon_plus    = QIcon("./L0/icons/item_plus.svg")
		icon_delete  = QIcon("./L0/icons/item_delete.svg")
		icon_grid_22 = QIcon("./L0/icons/grid_2_2.svg")
		icon_grid_33 = QIcon("./L0/icons/grid_3_3.svg")
		icon_r_1     = QIcon("./L0/icons/arrow_right.svg")
		icon_r_2     = QIcon("./L0/icons/arrow_right_2.svg")
		icon_reload    = QIcon("./L0/icons/reload.svg")

		self.menu_rules                         = QMenu()
		self.menu_rules_header        : QMenu   = self.menu_rules.addMenu(icon_grid_22, "Правила обработки данных")
		self.menu_rules_create        : QAction = self.menu_rules_header.addAction(icon_plus, "Создать правило")

		self.menu_rule_header         : QMenu   = self.menu_rules.addMenu(icon_grid_33, "Правило обработки данных")
		self.menu_rule_edit_input     : QAction = self.menu_rule_header.addAction(icon_r_1, "Редактировать вход")
		self.menu_rule_edit_output    : QAction = self.menu_rule_header.addAction(icon_r_2, "Редактировать выход")
		self.menu_rule_header.addSeparator()
		self.menu_rule_delete         : QAction = self.menu_rule_header.addAction(icon_delete, "Удалить")

		self.menu_rules_reset_header  : QMenu   = self.menu_rules.addMenu(icon_reload, "Сброс данных")
		self.menu_rules_reset_by_type : QAction = self.menu_rules_reset_header.addAction(icon_reload,  "Сбросить тип правил")

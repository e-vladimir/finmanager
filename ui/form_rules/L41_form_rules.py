# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МОДЕЛЬ UI

from PySide6.QtGui     import QIcon, QAction
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_rules    import Ui_frm_rules


class C41_FormRules(C20_PySideForm, Ui_frm_rules):
	""" Форма Правила обработки данных: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuRules()

	def InitMenuRules(self):
		""" Инициализация меню Правила обработки данных """
		icon_arrow_r                                 = QIcon("./L0/icons/arrow_right.svg")
		icon_arrow_r_2                               = QIcon("./L0/icons/arrow_right_2.svg")
		icon_item_plus                               = QIcon("./L0/icons/item_plus.svg")
		icon_grid_2_2                                = QIcon("./L0/icons/grid_2_2.svg")
		icon_grid_3_3                                = QIcon("./L0/icons/grid_3_3.svg")
		icon_reload                                  = QIcon("./L0/icons/reload.svg")

		self.menu_rules                              = QMenu("Финансовые операции")

		self.submenu_rules_type                      = self.menu_rules.addMenu(icon_grid_2_2, "Тип правил")
		self.action_rules_type_create_rule : QAction = self.submenu_rules_type.addAction(icon_item_plus, "Создать правило")
		self.submenu_rules_type.addSeparator()
		self.action_rules_type_reset       : QAction = self.submenu_rules_type.addAction(icon_reload,    "Сброс данных")

		self.submenu_rules_rule                      = self.menu_rules.addMenu(icon_grid_3_3, "Правило обработки данных")
		self.action_rules_rule_edit_input  : QAction = self.submenu_rules_rule.addAction(icon_arrow_r,   "Редактировать вход")
		self.action_rules_rule_edit_output : QAction = self.submenu_rules_rule.addAction(icon_arrow_r_2, "Редактировать выход")

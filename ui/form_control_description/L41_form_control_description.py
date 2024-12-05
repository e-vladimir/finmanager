# ФОРМА УПРАВЛЕНИЕ ОПИСАНИЕМ: МОДЕЛЬ UI

from PySide6.QtGui                import QAction, QIcon
from PySide6.QtWidgets            import QMenu

from L20_PySide6                  import C20_PySideForm
from L40_form_control_description import Ui_frm_control_description


class C41_FormControlDescription(C20_PySideForm, Ui_frm_control_description):
	""" Форма Управление описанием: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuRules()

	def InitMenuRules(self):
		""" Инициализация меню правил автозамены описания """
		icon_grid_2_2   = QIcon("./L0/icons/grid_2_2.svg")
		icon_grid_3_3   = QIcon("./L0/icons/grid_3_3.svg")
		icon_item_plus  = QIcon("./L0/icons/item_plus.svg")
		icon_delete     = QIcon("./L0/icons/item_delete.svg")
		icon_edit       = QIcon("./L0/icons/edit.svg")

		self.menu_rules = QMenu("Правила автозамены описания")

		self.submenu_rules_rules                      = self.menu_rules.addMenu(icon_grid_2_2, "Правила автозамены описания")
		self.action_rules_rules_create_rule : QAction = self.submenu_rules_rules.addAction(icon_item_plus, "Создать правило")

		self.submenu_rules_rule                       = self.menu_rules.addMenu(icon_grid_3_3, "Правило автозамены описания")
		self.action_rules_rule_edit_input   : QAction = self.submenu_rules_rule.addAction(icon_edit,   "Редактировать фрагмент поиска")
		self.action_rules_rule_edit_output  : QAction = self.submenu_rules_rule.addAction(icon_edit,   "Редактировать фрагмент замены")
		self.submenu_rules_rule.addSeparator()
		self.action_rules_rule_delete_rule  : QAction = self.submenu_rules_rule.addAction(icon_delete, "Удалить правило")

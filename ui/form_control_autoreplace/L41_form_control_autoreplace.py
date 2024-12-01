# ФОРМА УПРАВЛЕНИЕ АВТОЗАМЕНОЙ: МОДЕЛЬ UI

from PySide6.QtGui                import QIcon, QAction
from PySide6.QtWidgets            import QMenu

from L20_PySide6                  import C20_PySideForm
from L40_form_control_autoreplace import Ui_frm_control_autoreplace


class C41_FormControlAutoreplace(C20_PySideForm, Ui_frm_control_autoreplace):
	""" Форма Управление автозаменой: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuRules()

	def InitMenuRules(self):
		""" Инициализация меню Финансовые операции """
		icon_grid_2_2                           = QIcon("./L0/icons/grid_2_2.svg")
		icon_grid_3_3                           = QIcon("./L0/icons/grid_3_3.svg")
		icon_item_plus                          = QIcon("./L0/icons/item_plus.svg")
		icon_edit                               = QIcon("./L0/icons/edit.svg")

		self.menu_rules                         = QMenu("Правила автозамены")

		self.submenu_rules                      = self.menu_rules.addMenu(icon_grid_2_2, "Правила автозамены")
		self.action_rules_create_rule : QAction = self.submenu_rules.addAction(icon_item_plus,  "Создать правило")

		self.submenu_rule                       = self.menu_rules.addMenu(icon_grid_3_3, "Правило автозамены")
		self.action_rule_edit_input   : QAction = self.submenu_rule.addAction(icon_edit, "Редактировать фрагменты поиска")
		self.action_rule_edit_output  : QAction = self.submenu_rule.addAction(icon_edit, "Редактировать фрагменты замены")

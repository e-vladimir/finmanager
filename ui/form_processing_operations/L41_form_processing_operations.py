# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: МОДЕЛЬ UI

from PySide6.QtGui                  import QAction, QIcon
from PySide6.QtWidgets              import QMenu

from L00_rules                      import RULES

from L20_PySide6                    import C20_PySideForm
from L40_form_processing_operations import Ui_frm_processing_operations


class C41_FormProcessingOperations(C20_PySideForm, Ui_frm_processing_operations):
	""" Форма Обработка операций: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuRules()

	def InitMenuRules(self):
		""" Инициализация меню правил обработки """
		icon_grid_2_2                                 = QIcon("./L0/icons/grid_2_2.svg")
		icon_grid_3_3                                 = QIcon("./L0/icons/grid_3_3.svg")
		icon_item_plus                                = QIcon("./L0/icons/item_plus.svg")
		icon_open                                     = QIcon("./L0/icons/open.svg")
		icon_list                                     = QIcon("./L0/icons/list.svg")
		icon_blocks                                   = QIcon("./L0/icons/blocks.svg")
		icon_delete                                   = QIcon("./L0/icons/item_delete.svg")
		icon_processing                               = QIcon("./L0/icons/processing.svg")

		self.menu_rules                               = QMenu("Правила обработки")

		self.submenu_rules_types                      = self.menu_rules.addMenu(icon_blocks, "Тип правил")
		self.action_rules_types_description : QAction = self.submenu_rules_types.addAction(icon_list, f"{RULES.REPLACE_DESCRIPTION.value}")
		self.action_rules_types_destination : QAction = self.submenu_rules_types.addAction(icon_list, f"{RULES.MATCH_DESTINATION.value}")
		self.action_rules_types_labels      : QAction = self.submenu_rules_types.addAction(icon_list, f"{RULES.DETECT_LABEL.value}")

		self.submenu_rules_rules                      = self.menu_rules.addMenu(icon_grid_2_2, "Правила обработки")
		self.action_rules_rules_create      : QAction = self.submenu_rules_rules.addAction(icon_item_plus,  "Создать правило")
		self.submenu_rules_rules.addSeparator()
		self.action_rules_rules_apply       : QAction = self.submenu_rules_rules.addAction(icon_processing, "Применить правила")

		self.submenu_rules_rule                       = self.menu_rules.addMenu(icon_grid_3_3, "Правило обработки")
		self.action_rules_rule_open         : QAction = self.submenu_rules_rule.addAction(icon_open,   "Открыть правило")
		self.action_rules_rule_delete       : QAction = self.submenu_rules_rule.addAction(icon_delete, "Удалить правило")

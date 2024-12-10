# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: МОДЕЛЬ UI

from PySide6.QtGui                  import QAction, QActionGroup, QIcon
from PySide6.QtWidgets              import QMenu

from L00_rules                      import RULES

from L20_PySide6                    import C20_PySideForm
from L40_form_processing_operations import Ui_frm_processing_operations


class C41_FormProcessingOperations(C20_PySideForm, Ui_frm_processing_operations):
	""" Форма Обработка операций: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuRules()
		self.InitMenuTools()

	def InitMenuRules(self):
		""" Инициализация меню правил обработки """
		icon_grid_2_2                                 = QIcon("./L0/icons/grid_2_2.svg")
		icon_grid_3_3                                 = QIcon("./L0/icons/grid_3_3.svg")
		icon_item_plus                                = QIcon("./L0/icons/item_plus.svg")
		icon_open                                     = QIcon("./L0/icons/open.svg")
		icon_blocks                                   = QIcon("./L0/icons/blocks.svg")
		icon_delete                                   = QIcon("./L0/icons/item_delete.svg")
		icon_processing                               = QIcon("./L0/icons/processing.svg")

		self.menu_rules                               = QMenu("Правила обработки")

		self.submenu_rules_types                      = self.menu_rules.addMenu(icon_blocks, "Тип правил")
		self.action_rules_types_description : QAction = self.submenu_rules_types.addAction(f"{RULES.REPLACE_DESCRIPTION.value}")
		self.action_rules_types_destination : QAction = self.submenu_rules_types.addAction(f"{RULES.MATCH_DESTINATION.value}")
		self.action_rules_types_labels      : QAction = self.submenu_rules_types.addAction(f"{RULES.DETECT_LABEL.value}")

		self.actions_rules_types = QActionGroup(self.submenu_rules_types)
		self.actions_rules_types.addAction(self.action_rules_types_description)
		self.actions_rules_types.addAction(self.action_rules_types_destination)
		self.actions_rules_types.addAction(self.action_rules_types_labels)

		for action in self.actions_rules_types.actions(): action.setCheckable(True)

		self.action_rules_types_description.setChecked(True)

		self.submenu_rules_rules                      = self.menu_rules.addMenu(icon_grid_2_2, "Правила обработки")
		self.action_rules_rules_create      : QAction = self.submenu_rules_rules.addAction(icon_item_plus,  "Создать правило")
		self.submenu_rules_rules.addSeparator()
		self.action_rules_rules_apply       : QAction = self.submenu_rules_rules.addAction(icon_processing, "Применить правила")

		self.submenu_rules_rule                       = self.menu_rules.addMenu(icon_grid_3_3, "Правило обработки")
		self.action_rules_rule_open         : QAction = self.submenu_rules_rule.addAction(icon_open,   "Открыть правило")
		self.action_rules_rule_delete       : QAction = self.submenu_rules_rule.addAction(icon_delete, "Удалить правило")

	def InitMenuTools(self):
		""" Инициализация меню инструментов """
		icon_arrow_r_1                                         = QIcon("./L0/icons/arrow_right.svg")
		icon_arrow_r_2                                         = QIcon("./L0/icons/arrow_right_2.svg")
		icon_grid_2_2                                          = QIcon("./L0/icons/grid_2_2.svg")
		icon_grid_3_3                                          = QIcon("./L0/icons/grid_3_3.svg")
		icon_processing                                        = QIcon("./L0/icons/processing.svg")
		icon_list                                              = QIcon("./L0/icons/list.svg")

		self.action_tools_description_include_edit   : QAction = QAction(icon_arrow_r_1,  "Редактировать")
		self.action_tools_description_include_select : QAction = QAction(icon_list,       "Выбрать")
		self.action_tools_description_applies_edit   : QAction = QAction(icon_arrow_r_2,  "Редактировать")
		self.action_tools_description_processing     : QAction = QAction(icon_processing, "Выполнить обработку описания")

		self.action_tools_destination_include_edit   : QAction = QAction(icon_arrow_r_1,  "Редактировать")
		self.action_tools_destination_include_select : QAction = QAction(icon_list,       "Выбрать")
		self.action_tools_destination_applies_edit   : QAction = QAction(icon_arrow_r_2,  "Редактировать")
		self.action_tools_destination_processing     : QAction = QAction(icon_processing, "Выполнить обработку описания")

		self.action_tools_labels_mode_replace        : QAction = QAction("Замена")
		self.action_tools_labels_mode_append         : QAction = QAction("Добавление")
		self.action_tools_labels_mode_expand         : QAction = QAction("Расширение")
		self.action_tools_labels_include_edit        : QAction = QAction(icon_arrow_r_1,  "Редактировать")
		self.action_tools_labels_include_select      : QAction = QAction(icon_list,       "Выбрать")
		self.action_tools_labels_applies_edit        : QAction = QAction(icon_arrow_r_2,  "Редактировать")
		self.action_tools_labels_applies_select      : QAction = QAction(icon_list,       "Выбрать метки")
		self.action_tools_labels_processing          : QAction = QAction(icon_processing, "Выполнить обработку меток")

		actions_tools_labels_mode                              = QActionGroup(self)
		actions_tools_labels_mode.addAction(self.action_tools_labels_mode_replace)
		actions_tools_labels_mode.addAction(self.action_tools_labels_mode_append)
		actions_tools_labels_mode.addAction(self.action_tools_labels_mode_expand)
		for action in actions_tools_labels_mode.actions(): action.setCheckable(True)
		self.action_tools_labels_mode_replace.setChecked(True)

		self.menu_tools                                        = QMenu("Правила обработки")
		self.submenu_tools_description                         = self.menu_tools.addMenu(icon_grid_2_2, "Обработка описания")
		self.submenu_tools_description.addSection("Содержит")
		self.submenu_tools_description.addAction(self.action_tools_description_include_edit)
		self.submenu_tools_description.addAction(self.action_tools_description_include_select)
		self.submenu_tools_description.addSection("Применяется")
		self.submenu_tools_description.addAction(self.action_tools_description_applies_edit)
		self.submenu_tools_description.addSeparator()
		self.submenu_tools_description.addAction(self.action_tools_description_processing)

		self.submenu_tools_destination                         = self.menu_tools.addMenu(icon_grid_2_2, "Обработка назначения")
		self.submenu_tools_destination.addSection("Содержит")
		self.submenu_tools_destination.addAction(self.action_tools_destination_include_edit)
		self.submenu_tools_destination.addAction(self.action_tools_destination_include_select)
		self.submenu_tools_destination.addSection("Применяется")
		self.submenu_tools_destination.addAction(self.action_tools_destination_applies_edit)
		self.submenu_tools_destination.addSeparator()
		self.submenu_tools_destination.addAction(self.action_tools_destination_processing)

		self.submenu_tools_labels                              = self.menu_tools.addMenu(icon_grid_3_3, "Обработка меток")
		self.submenu_tools_labels.addSection("Режим обработки")
		self.submenu_tools_labels.addAction(self.action_tools_labels_mode_replace)
		self.submenu_tools_labels.addAction(self.action_tools_labels_mode_append)
		self.submenu_tools_labels.addAction(self.action_tools_labels_mode_expand)
		self.submenu_tools_labels.addSection("Содержит")
		self.submenu_tools_labels.addAction(self.action_tools_labels_include_edit)
		self.submenu_tools_labels.addAction(self.action_tools_labels_include_select)
		self.submenu_tools_labels.addSection("Применяется")
		self.submenu_tools_labels.addAction(self.action_tools_labels_applies_edit)
		self.submenu_tools_labels.addAction(self.action_tools_labels_applies_select)
		self.submenu_tools_labels.addSeparator()
		self.submenu_tools_labels.addAction(self.action_tools_labels_processing)

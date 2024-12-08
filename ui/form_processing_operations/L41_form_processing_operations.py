# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: МОДЕЛЬ UI

from PySide6.QtGui                  import QAction, QIcon
from PySide6.QtWidgets              import QMenu

from L20_PySide6                    import C20_PySideForm
from L40_form_processing_operations import Ui_frm_processing_operations


class C41_FormProcessingOperations(C20_PySideForm, Ui_frm_processing_operations):
	""" Форма Обработка операций: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuRules()

	def InitMenuRules(self):
		""" Инициализация меню правил обработки """
		icon_grid_2_2   = QIcon("./L0/icons/grid_2_2.svg")
		icon_item_plus  = QIcon("./L0/icons/item_plus.svg")

		self.menu_rules                          = QMenu("Правила обработки")

		self.submenu_rules_rules                 = self.menu_rules.addMenu(icon_grid_2_2, "Правила обработки")
		self.action_rules_rules_create : QAction = self.submenu_rules_rules.addAction(icon_item_plus, "Создать правило")

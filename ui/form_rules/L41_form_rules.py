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
		icon_plus    = QIcon("./ui/icons/item_plus.svg")
		icon_grid_22 = QIcon("./ui/icons/grid_2_2.svg")

		self.menu_rules = QMenu()
		self.menu_rules_header : QMenu   = self.menu_rules.addMenu(icon_grid_22, "Правила обработки данных")
		self.menu_rules_create : QAction = self.menu_rules_header.addAction(icon_plus, "Создать правило")

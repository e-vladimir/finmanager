# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui                  import QCursor
from PySide6.QtWidgets              import QHeaderView

from L60_form_processing_operations import C60_FormProcessingOperations
from L90_rules                      import C90_ProcessingRule


class C70_FormProcessingOperations(C60_FormProcessingOperations):
	""" Форма Обработка операций: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Обработка операций - {self.workspace.DmDyToString()}")

	# Вкладки
	def InitTabsMain(self):
		""" Настройка вкладок """
		self.tabs_main.setCurrentIndex(0)

	# Таблица правил
	def AdjustTableRules_Size(self):
		""" Таблица правил: Настройка размера """
		self.table_rules.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.table_rules.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

		self.table_rules.resizeRowsToContents()

	# Меню правила обработки
	def AdjustMenuRules_Enable(self):
		""" Меню правил обработки: Настройка доступности """
		flag_selected : bool = bool(self._processing_ido)

		self.action_rules_rule_open.setEnabled(flag_selected)
		self.action_rules_rule_delete.setEnabled(flag_selected)

	def AdjustMenuRules_Text(self):
		""" Меню правил обработки: Настройка текстов """
		self.submenu_rules_rules.setTitle(f"{self._processing_rule_types.value}")

		self.submenu_rules_rule.setTitle("Правило обработки")

		if self._processing_ido:
			rule         = C90_ProcessingRule(self._processing_ido)
			output : str = ', '.join(rule.OutputAsStrings())
			suffix : str = '...' if len(output) > 30 else ''
			self.submenu_rules_rule.setTitle(f"{output[:30]}{suffix}")

	def ShowMenuRules(self):
		""" Отображение меню правил обработки """
		self.menu_rules.exec_(QCursor().pos())

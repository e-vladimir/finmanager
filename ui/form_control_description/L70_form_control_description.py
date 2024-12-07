# ФОРМА УПРАВЛЕНИЕ ОПИСАНИЕМ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui                import QCursor, Qt
from PySide6.QtWidgets            import QHeaderView

from L60_form_control_description import C60_FormControlDescription
from L90_rules import C90_ProcessingRule


class C70_FormControlDescription(C60_FormControlDescription):
	""" Форма Управление описанием: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Управление описанием операций - {self.workspace.DmDyToString()}")

	# Вкладки
	def SwitchTabsMainToFirst(self):
		""" Переключение вкладки на первую """
		self.tabs_main.setCurrentIndex(0)

	# Таблица правил
	def AdjustTableRules_Sizes(self):
		""" Таблица правил: Настройка размера """
		self.table_rules.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.table_rules.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

		self.table_rules.resizeRowsToContents()

	def AdjustTableRules_Sort(self):
		""" Таблица правил: Настройка сортировки """
		self.table_rules.sortByColumn(0, Qt.SortOrder.AscendingOrder)

	def ProcessingTableRules_DbClick(self):
		""" Обработка двойного клика по таблице правил """
		match self._processing_column:
			case 0: self.on_RequestEditInput()
			case 1: self.on_RequestEditOutput()

	# Меню правил автозамены описания
	def AdjustMenuRules_Enable(self):
		""" Меню автозамены описания: Настройка доступности """
		flag_selected : bool = bool(self._processing_ido)

		self.action_rules_rule_edit_input.setEnabled(flag_selected)
		self.action_rules_rule_edit_output.setEnabled(flag_selected)
		self.action_rules_rule_delete_rule.setEnabled(flag_selected)
		self.action_rules_rule_apply.setEnabled(flag_selected)

	def AdjustMenuRules_Text(self):
		""" Меню автозамены описания: Настройка текста """
		self.submenu_rules_rule.setTitle("Правило автозамены описания")

		if self._processing_ido:
			rule = C90_ProcessingRule(self._processing_ido)
			self.submenu_rules_rule.setTitle(rule.OutputAsString())

	def ShowMenuRules(self):
		""" Отображение меню правил автозамены описания """
		self.menu_rules.exec_(QCursor().pos())

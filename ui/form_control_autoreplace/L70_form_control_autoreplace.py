# ФОРМА УПРАВЛЕНИЕ АВТОЗАМЕНОЙ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui                import QCursor, Qt
from PySide6.QtWidgets            import QHeaderView

from L60_form_control_autoreplace import C60_FormControlAutoreplace


class C70_FormControlAutoreplace(C60_FormControlAutoreplace):
	""" Форма Управление автозаменой: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle("Управление автозаменой")

	# Таблица данных
	def AdjustTableData_Size(self):
		""" Таблица данных: Настройка размера """
		self.table_data.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.table_data.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

		self.table_data.resizeRowsToContents()

	def AdjustTableData_Sort(self):
		""" Таблица данных: Настройка сортировки """
		self.table_data.sortByColumn(1, Qt.SortOrder.AscendingOrder)

	# Меню правил автозамены
	def AdjustMenuRules_Enable(self):
		""" Меню автозамены: Настройка доступности """
		flag_selected : bool = bool(self._processing_ido)

		self.action_rule_edit_input.setEnabled(flag_selected)
		self.action_rule_edit_output.setEnabled(flag_selected)

	def AdjustMenuRules_Text(self):
		""" Меню автозамены: Настройка текста """
		self.submenu_rule.setTitle("Правило автозамены")

		if self._processing_output:
			self.submenu_rule.setTitle(self._processing_output)

	def ShowMenuRules(self):
		""" Отображение меню правил автозамены """
		self.menu_rules.exec_(QCursor().pos())

# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui  import QCursor, Qt

from L00_rules      import RULES
from L60_form_rules import C60_FormRules


class C70_FormRules(C60_FormRules):
	""" Форма Правила обработки данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		title : str = "Правила обработки данных"

		if self._processing_type is not None: title += f": {self._processing_type}"

		self.setWindowTitle(title)

	# Список типов правил
	def FillListTypes(self):
		""" Заполнение списка типов правил """
		self.list_types.clear()

		self.list_types.addItem(RULES.REPLACE_TEXT)

	# Меню правил обработки данных
	def AdjustMenuRulesText(self):
		""" Меню правил обработки данных: Настройка текста """
		self.menu_rules_header.setTitle("Правила")
		if self._processing_type: self.menu_rules_header.setTitle(self._processing_type)

		self.menu_rule_header.setTitle("Правило")
		if self._processing_name: self.menu_rule_header.setTitle(self._processing_name)

		self.menu_rule_edit_input.setText("Редактировать вход")
		self.menu_rule_edit_output.setText("Редактировать выход")

		match self._processing_type:
			case RULES.REPLACE_TEXT:
				self.menu_rule_edit_input.setText("Редактировать фрагмент поиска")
				self.menu_rule_edit_output.setText("Редактировать фрагмент замены")

		self.menu_rules_reset_by_type.setText("Сброс типа правил")
		match self._processing_type:
			case RULES.REPLACE_TEXT:
				self.menu_rules_reset_by_type.setText(f"Сбросить правила Замены фрагмента текста")

	def AdjustMenuRulesEnable(self):
		""" Меню правил обработки данных: Настройка доступности """
		flag_selected : bool = bool(self._processing_ido)
		self.menu_rule_edit_input.setEnabled(flag_selected)
		self.menu_rule_edit_output.setEnabled(flag_selected)
		self.menu_rule_delete.setEnabled(flag_selected)

		flag_type     : bool = bool(self._processing_type)
		self.menu_rules_reset_by_type.setEnabled(flag_type)

	def ShowMenuRules(self):
		""" Отображение меню правил обработки данных """
		self.menu_rules.exec_(QCursor().pos())

	# Таблица данных
	def AdjustTableDataSize(self):
		""" Таблица данных: Настройка размера """
		self.table_data.resizeColumnsToContents()

		for index_col in range(self.table_data.horizontalHeader().count()):
			column_size : int = self.table_data.columnWidth(index_col)
			column_size       = max((self.table_data.width() - 10) // 2, column_size)

			self.table_data.setColumnWidth(index_col, column_size)

		self.table_data.resizeRowsToContents()

	def AdjustTableDataSort(self):
		""" Таблица данных: Настройка сортировки """
		match self._processing_type:
			case RULES.REPLACE_TEXT: self.table_data.sortByColumn(1, Qt.SortOrder.AscendingOrder)

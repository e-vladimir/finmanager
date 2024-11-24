# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui import QCursor, QColor, Qt
from PySide6.QtWidgets import QHeaderView

from L00_rules         import RULES
from L20_PySide6 import C20_StandardItem
from L60_form_rules    import C60_FormRules


class C70_FormRules(C60_FormRules):
	""" Форма Правила обработки данных: Механика управления """

	# Выпадающий список типов правил обработки данных
	def FillCbboxTypes(self):
		""" Заполнение списка типов правил обработки данных """
		self.cbbox_types.clear()

		self.cbbox_types.addItem(RULES.REPLACE_TEXT)
		self.cbbox_types.addItem(RULES.DETECT_LABEL_BY_TEXT)

	def ShowCbboxTypes(self):
		""" Отображение списка типов правил обработки данных """
		self.cbbox_types.setCurrentText(self._processing_type.value)

	# Таблица данных
	def AdjustTableData_Size(self):
		""" Таблица данных: Настройка размера """
		self.table_data.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.table_data.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

		self.table_data.resizeRowsToContents()

	def AdjustTableData_Order(self):
		""" Таблица данных: Настройка сортировки """
		match self._processing_type:
			case RULES.REPLACE_TEXT        : self.table_data.sortByColumn(1, Qt.SortOrder.AscendingOrder)
			case RULES.DETECT_LABEL_BY_TEXT: self.table_data.sortByColumn(0, Qt.SortOrder.AscendingOrder)

	def AdjustTableData_Color(self):
		""" Таблица данных: Настройка цвета """
		item_root = self.model_data.invisibleRootItem()

		for index_row in range(self.model_data.rowCount()):
			color                          = QColor(0, 0, 0)
			item_input  : C20_StandardItem = self.model_data.item(index_row, 0)
			item_output : C20_StandardItem = self.model_data.item(index_row, 1)

			if   not item_input.text() : color = QColor(120, 120, 120)
			elif not item_output.text(): color = QColor(120, 120, 120)

			self.model_data.setRowColor(item_root, index_row, color_fg=color)

	# Меню правил обработки данных
	def AdjustMenuRules_Text(self):
		""" Меню правил обработки данных: Настройка текста """
		self.submenu_rules_type.setTitle(self._processing_type.value)

	def AdjustMenuRules_Enable(self):
		""" Меню правил обработки данных: Настройка доступности """
		pass

	def ShowMenuRules(self):
		""" Меню правил обработки данных: Отображение меню """
		self.menu_rules.exec_(QCursor().pos())

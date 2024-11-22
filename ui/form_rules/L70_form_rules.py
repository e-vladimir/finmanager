# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtWidgets import QHeaderView

from L00_rules         import RULES
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
		pass

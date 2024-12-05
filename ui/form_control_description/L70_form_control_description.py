# ФОРМА УПРАВЛЕНИЕ ОПИСАНИЕМ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui                import QCursor, Qt
from PySide6.QtWidgets            import QHeaderView

from L60_form_control_description import C60_FormControlDescription


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

	# Меню правил автозамены описания
	def AdjustMenuRules_Enable(self):
		""" Меню автозамены описания: Настройка доступности """
		pass

	def AdjustMenuRules_Text(self):
		""" Меню автозамены описания: Настройка текста """
		pass

	def ShowMenuRules(self):
		""" Отображение меню правил автозамены описания """
		self.menu_rules.exec_(QCursor().pos())

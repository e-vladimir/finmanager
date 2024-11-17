# ФОРМА ИМПОРТ ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui   import QCursor

from L60_form_import import C60_FormImport


class C70_FormImport(C60_FormImport):
	""" Форма Импорт данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle("Импорт данных")

	# Таблица операций
	def AdjustTableOperations_Size(self):
		""" Таблица операций: Настройка размера """
		sizes : list[int] = [200, 200]

		for index_col, size in enumerate(sizes): self.table_operations_data.setColumnWidth(index_col, size)

	# Меню импорта финансовых операций
	def AdjustMenuOperations_Enable(self):
		""" Меню импорт финансовых операций: Настройка доступности """
		pass

	def AdjustMenuOperations_Text(self):
		""" Меню импорт финансовых операций: Настройка текста """
		pass

	def ShowMenuOperations(self):
		""" Отображение меню импорта финансовых операций """
		self.menu_operations.exec_(QCursor().pos())

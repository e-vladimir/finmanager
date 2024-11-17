# ФОРМА ИМПОРТ ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

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
		self.table_operations_data.resizeColumnsToContents()

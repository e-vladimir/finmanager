# ФОРМА ИМПОРТ ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ
# 14 мар 2025

from PySide6.QtGui   import QCursor

from L60_form_import import C60_FormImport


class C70_FormImport(C60_FormImport):
	""" Форма Импорт данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Импорт данных - {self.Workspace.DmDyToString()}")

	# Меню Импорт операций
	def AdjustMenuOperations(self):
		""" Настройка меню операций """
		pass

	def AdjustMenuOperations_Enable(self):
		""" Настройка меню операций: Доступность """
		pass

	def AdjustMenuOperations_Text(self):
		""" Настройка меню операций: Текст """
		pass

	def ShowMenuOperations(self):
		""" Отображение меню операций """
		self.MenuOperations.exec_(QCursor().pos())

	# Таблица данных Импорт операций
	def AdjustTableOperations_Size(self):
		""" Настройка таблицы данных импорта операций: Размеры """
		self.TableDataOperations.resizeColumnsToContents()

		sizes_min : list[int] = [150, 150]

		for idx_col, size_min in enumerate(sizes_min):
			col_size : int = max(self.TableDataOperations.columnWidth(idx_col), size_min)
			self.TableDataOperations.setColumnWidth(idx_col, col_size)

		for idx_row in range(self.ModelDataOperations.rowCount()):
			self.TableDataOperations.setRowHeight(idx_row, 22)

	# Вкладка Импорт операций
	def AdjustLabelOperations(self):
		""" Настройка надписи имени файла """
		self.LabelOperationsFilepath.setVisible(self.operations_filepath is not None)

		self.LabelOperationsFilepath.setText(f"{self.operations_filepath}")

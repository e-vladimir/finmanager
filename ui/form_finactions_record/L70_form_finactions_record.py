# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore             import Qt
from PySide6.QtGui              import QColor

from L60_form_finactions_record import C60_FormFinactionsRecord


class C70_FormFinactionsRecord(C60_FormFinactionsRecord):
	""" Форма Запись финдействий: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Заголовок окна """
		self.setWindowTitle(f"Запись финдействий")

	# Таблица данных
	def AdjustTableData_Size(self):
		""" Таблица данных: Настройка размеров """
		self.table_data.resizeColumnsToContents()
		self.table_data.resizeRowsToContents()

		for index_row in range(self.model_data.rowCount()):
			row_size   = self.table_data.rowHeight(index_row)
			row_size //= 20
			row_size  *= 20

			self.table_data.setRowHeight(index_row, row_size)

	def AdjustTableData_Alignment(self):
		""" Таблица данных: Настройка выравнивания """
		for index_row in range(self.model_data.rowCount()):
			item_data = self.model_data.item(index_row, 0)
			item_data.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

	def AdjustTableData_Color(self):
		""" Таблица данных: Настройка цветов """
		item_root           = self.model_data.invisibleRootItem()

		color_group         = QColor( 38,  38,  38, 255)
		color_item          = QColor( 38,  38,  38,  30)
		color_subitem       = QColor( 38,  38,  38,  20)
		self.model_data.setRowColor(item_root,  0, color_group,    Qt.GlobalColor.white)
		self.model_data.setRowColor(item_root,  1, color_item,     Qt.GlobalColor.black)
		self.model_data.setRowColor(item_root,  2, color_subitem,  Qt.GlobalColor.black)
		self.model_data.setRowColor(item_root,  3, color_item,     Qt.GlobalColor.black)

		color_group         = QColor( 65,  36,  20, 255)
		color_item          = QColor( 65,  36,  20,  30)
		color_subitem       = QColor( 65,  36,  20,  20)
		self.model_data.setRowColor(item_root,  4, color_group,    Qt.GlobalColor.white)
		self.model_data.setRowColor(item_root,  5, color_item,     Qt.GlobalColor.gray)
		self.model_data.setRowColor(item_root,  6, color_subitem,  Qt.GlobalColor.gray)

		color_group         = QColor( 38,  33,  99, 255)
		color_item          = QColor( 38,  33,  99,  30)
		color_subitem       = QColor( 38,  33,  99,  20)
		self.model_data.setRowColor(item_root,  7, color_group,    Qt.GlobalColor.white)
		self.model_data.setRowColor(item_root,  8, color_item,     Qt.GlobalColor.black)
		self.model_data.setRowColor(item_root,  9, color_subitem,  Qt.GlobalColor.black)
		self.model_data.setRowColor(item_root, 10, color_item,     Qt.GlobalColor.black)
		self.model_data.setRowColor(item_root, 11, color_subitem,  Qt.GlobalColor.black)

		headers : list[int] = [0, 4, 7]

		for index_row in range(self.model_data.rowCount()):
			if index_row in headers: continue

			item_data = self.model_data.item(index_row, 0)
			item_data.setForeground(Qt.GlobalColor.gray)

	def AdjustTableData_Font(self):
		""" Таблица данных: Настройка шрифтов """
		headers : list[int] = [0, 4, 7]

		for index_row in headers:
			item_data = self.model_data.item(index_row, 0)
			font_data = item_data.font()
			font_data.setBold(True)
			item_data.setFont(font_data)

# ФОРМА ФИНСТАТИСТИКА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore         import Qt
from PySide6.QtGui          import QColor
from PySide6.QtWidgets      import QHeaderView

from L60_form_finstatistics import C60_FormFinstatistics


class C70_FormFinstatistics(C60_FormFinstatistics):
	""" Форма Финстатистика: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Финстатистика - {self.workspace.DmDyToString()}")

	# Таблица данных
	def AdjustTableData_Size(self):
		""" Таблица данных: Настройка размера """
		self.table_data.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

		self.table_data.setColumnWidth(1, 75)
		self.table_data.setColumnWidth(2, 75)
		self.table_data.setColumnWidth(3, 75)

	def AdjustTableData_Colors(self):
		""" Таблица данных: Настройка цвета """
		color_bg    = QColor( 26,  26,  26)
		color_fg    = QColor(255, 255, 255)

		item_parent = self.model_data.invisibleRootItem()

		self.model_data.setRowColor(item_parent, 0, color_bg, color_fg)
		self.model_data.setRowBold(item_parent, 0)

		dy, dm      = self.workspace.DyDm()
		index_row   = len(self.finstruct.IdosInDyDm(dy, dm)) + 2

		self.model_data.setRowColor(item_parent, index_row , color_bg, color_fg)
		self.model_data.setRowBold(item_parent, index_row)

	def AdjustTableData_Span(self):
		""" Таблица данных: Настройка объединения """
		dy, dm      = self.workspace.DyDm()
		index_row   = len(self.finstruct.IdosInDyDm(dy, dm)) + 1

		self.table_data.setSpan(        0    , 0, 1, 4)
		self.table_data.setSpan(index_row    , 0, 1, 4)
		self.table_data.setSpan(index_row + 1, 0, 1, 4)

	def AdjustTableData_Align(self):
		""" Таблица данных: Настройка выравнивания """
		for index_row in range(self.model_data.rowCount()):
			item_data = self.model_data.item(index_row, 1)
			item_data.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

			item_data = self.model_data.item(index_row, 2)
			item_data.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

			item_data = self.model_data.item(index_row, 3)
			item_data.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

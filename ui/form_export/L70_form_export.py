# ФОРМА ЭКСПОРТ ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore  import Qt
from PySide6.QtGui   import QColor, QCursor

from L00_options     import OPTIONS
from L60_form_export import C60_FormExport


class C70_FormExport(C60_FormExport):
	""" Форма Экспорт данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle("Экспорт данных")

	# Таблица данных экспорта финдействий
	def AdjustTableFinactionsData_Size(self):
		""" Таблица данных финдействий: Настройка размеров """
		self.table_finactions_data.resizeRowsToContents()

		for index_row in range(self.model_finactions.rowCount()):
			row_height : int = self.table_finactions_data.rowHeight(index_row)
			self.table_finactions_data.setRowHeight(index_row, (row_height // 20) * 20)

		self.table_finactions_data.resizeColumnsToContents()

		col_size : int = self.table_finactions_data.columnWidth(0)
		col_size       = max(150, col_size)
		self.table_finactions_data.setColumnWidth(0, col_size)

	def AdjustTableFinactionsData_Span(self):
		""" Таблица данных финдействий: Настройка объединения ячеек """
		self.table_finactions_data.setSpan(4, 0, 1, 2)
		self.table_finactions_data.setSpan(8, 0, 1, 2)

	def AdjustTableFinactionsData_Colors(self):
		""" Таблица данных финдействий: Настройка цвета """
		color_bg : QColor = QColor( 26,  26,  26)
		color_fg : QColor = QColor(255, 255, 255)

		parent_item       = self.model_finactions.invisibleRootItem()

		self.model_finactions.setRowColor(parent_item, 0, color_bg, color_fg)
		self.model_finactions.setRowColor(parent_item, 5, color_bg, color_fg)
		self.model_finactions.setRowColor(parent_item, 9, color_bg, color_fg)

		self.model_finactions.setRowBold(parent_item, 0)
		self.model_finactions.setRowBold(parent_item, 5)
		self.model_finactions.setRowBold(parent_item, 9)

		color_enable  : QColor = QColor(  0,   0,   0)
		color_disable : QColor = QColor(196, 196, 196)
		color_field   : QColor = QColor(127, 127, 127)
		color_bg      : QColor = QColor(255, 255, 255)

		self.model_finactions.setCellColor(parent_item, 1, 0, color_bg, color_field)

		self.model_finactions.setCellColor(parent_item, 2, 0, color_bg, color_field)
		match self._options_finactions_period_mode:
			case OPTIONS.MODE_ALL: self.model_finactions.setCellColor(parent_item, 2, 1, color_bg, color_disable)
			case OPTIONS.MODE_DM : self.model_finactions.setCellColor(parent_item, 2, 1, color_bg, color_enable)
			case OPTIONS.MODE_DY : self.model_finactions.setCellColor(parent_item, 2, 1, color_bg, color_enable)

		self.model_finactions.setCellColor(parent_item, 3, 0, color_bg, color_field)
		match self._options_finactions_period_mode:
			case OPTIONS.MODE_ALL: self.model_finactions.setCellColor(parent_item, 3, 1, color_bg, color_disable)
			case OPTIONS.MODE_DM : self.model_finactions.setCellColor(parent_item, 3, 1, color_bg, color_enable)
			case OPTIONS.MODE_DY : self.model_finactions.setCellColor(parent_item, 3, 1, color_bg, color_disable)

		self.model_finactions.setCellColor(parent_item, 6, 0, color_bg, color_field)

		self.model_finactions.setCellColor(parent_item, 7, 0, color_bg, color_field)
		match self._options_finactions_finstruct_mode:
			case OPTIONS.MODE_ALL    : self.model_finactions.setCellColor(parent_item, 7, 1, color_bg, color_disable)
			case OPTIONS.MODE_SELECT : self.model_finactions.setCellColor(parent_item, 7, 1, color_bg, color_enable)

		self.model_finactions.setCellColor(parent_item, 10, 0, color_bg, color_field)
		self.model_finactions.setCellColor(parent_item, 11, 0, color_bg, color_field)

	def AdjustTableFinactionsData_Align(self):
		""" Таблица данных финдействий: Настройка выравнивания """
		for index_row in range(self.model_finactions.rowCount()):
			item_data = self.model_finactions.item(index_row, 0)
			item_data.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

	def ProcessingDbClickTableFinactionsData(self):
		""" Обработка двойного клика по таблице данных экспорта финдействий """
		match self._processing_row:
			case  1: self.on_RequestSetOptionsFinactionsPeriodMode()
			case  2: self.on_RequestSetOptionsFinactionsPeriodDy()
			case  3: self.on_RequestSetOptionsFinactionsPeriodDm()

			case  6: self.on_RequestSetOptionsFinactionsFinstructMode()
			case  7: self.on_RequestSetOptionsFinactionsFinstructName()

			case 10: self.on_RequestSetOptionsFinactionsFolder()

	# Меню экспорта финдействий
	def AdjustMenuExportFinactions_Enable(self):
		""" Меню экспорта финдействий: Настройка доступности """
		self.menu_export_finactions_exec_export.setEnabled(len(self._options_finactions_filenames) > 0)

	def ShowMenuExportFinactions(self):
		""" Отображение меню экспорта финдействий """
		self.menu_export_finactions.exec_(QCursor().pos())

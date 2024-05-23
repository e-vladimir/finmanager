# ФОРМА ФИНАНАЛИЗ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore        import Qt, QModelIndex
from PySide6.QtGui         import QStandardItem, QCursor, QColor
from PySide6.QtWidgets     import QHeaderView

from L00_dict              import *
from L00_roles             import ROLE_TYPE

from L60_form_finanalytics import C60_FormFinanalytics
from L90_findescription    import C90_RecordFindescription


class C70_FormFinanalytics(C60_FormFinanalytics):
	""" Форма Финанализ: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Заголовок окна """
		self.setWindowTitle("Финаналитика")

	# Таблица Динамика финсостава
	def AdjustTableFindescriptionDynamicSize(self):
		""" Настройка размера """
		header : QHeaderView =  self.table_findescription_dynamic.horizontalHeader()
		header.setSectionResizeMode(0, header.Stretch)

		for index_col in range(1, header.count()):
			self.table_findescription_dynamic.setColumnWidth(index_col, 65)

		self.table_findescription_dynamic.resizeRowsToContents()
		for index_row in range(self.model_findescription_dynamic.rowCount()):
			row_size : int = self.table_findescription_dynamic.rowHeight(index_row)
			if row_size > 30: continue

			self.table_findescription_dynamic.setRowHeight(index_row, 22)

	def AdjustTableFindescriptionDynamicAlign(self):
		""" Настройка выравнивания """
		for index_row in range(self.model_findescription_dynamic.rowCount()):
			for index_col in range(self.model_findescription_dynamic.columnCount()):
				item_data : QStandardItem = self.model_findescription_dynamic.item(index_row, index_col)
				item_data.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

	def AdjustTableFindescriptionDynamicSpan(self):
		""" Настройка объединения ячеек """
		for index_row in range(self.model_findescription_dynamic.rowCount()):
			index_data : QModelIndex = self.model_findescription_dynamic.index(index_row, 0)
			data_index : str | None  = index_data.data(ROLE_TYPE)

			if     data_index is None     : continue
			if not data_index == SEPARATOR: continue

			self.table_findescription_dynamic.setSpan(index_row, 0, 1, self.model_findescription_dynamic.columnCount())

	def AdjustTableFindescriptionDynamicColor(self):
		""" Настройка цветов """
		index_header_income  : QModelIndex | None = self.model_findescription_dynamic.indexByData(f"{HEADER}_{INCOME}", ROLE_TYPE)
		index_footer_income  : QModelIndex | None = self.model_findescription_dynamic.indexByData(f"{FOOTER}_{INCOME}", ROLE_TYPE)
		index_header_outcome : QModelIndex | None = self.model_findescription_dynamic.indexByData(f"{HEADER}_{OUTCOME}", ROLE_TYPE)
		index_footer_outcome : QModelIndex | None = self.model_findescription_dynamic.indexByData(f"{FOOTER}_{OUTCOME}", ROLE_TYPE)

		item_root            : QStandardItem      = self.model_findescription_dynamic.invisibleRootItem()

		if index_header_income  is not None: self.model_findescription_dynamic.setRowColor(item_root, index_header_income.row(),  QColor( 30,  90, 30), QColor(250, 250, 250))
		if index_footer_income  is not None: self.model_findescription_dynamic.setRowColor(item_root, index_footer_income.row(),  QColor( 60, 110, 60), QColor(250, 250, 250))
		if index_header_outcome is not None: self.model_findescription_dynamic.setRowColor(item_root, index_header_outcome.row(), QColor( 90,  30, 30), QColor(250, 250, 250))
		if index_footer_outcome is not None: self.model_findescription_dynamic.setRowColor(item_root, index_footer_outcome.row(), QColor(110,  60, 60), QColor(250, 250, 250))

	# Меню динамики финсостава
	def ShowMenuFindescriptionDynamic(self):
		""" Отображение меню динамики финсостава """
		self.menu_findescription_dynamic.exec_(QCursor().pos())

	def AdjustMenuFindescriptionText(self):
		""" Настройка элементов меню """
		self.menu_findescription_dynamic_record_header.setText("Запись финсостава")

		if not self._oid_processing: return

		record_findescription = C90_RecordFindescription(self._oid_processing)

		self.menu_findescription_dynamic_record_header.setText(record_findescription.Name())

	def AdjustMenuFindescriptionEnable(self):
		""" Настройка доступности элементов """
		flag_selected : bool = bool(self._oid_processing)

		self.menu_findescription_dynamic_record_dec.setEnabled(flag_selected)

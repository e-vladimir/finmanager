# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore             import Qt
from PySide6.QtGui              import QColor, QStandardItem

from L00_findescription        import *
from L00_form_record_finactions import *

from L10_converts               import AmountToString
from L60_form_record_finactions import C60_FormRecordFinactions


class C70_FormRecordFinactions(C60_FormRecordFinactions):
	""" Форма Запись финдействий: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"{AmountToString(self.record_finactions.Amount(), False, True)} от {self.record_finactions.DdDmDyToString()}: {self.record_finactions.Note()}")

	def AdjustSplitterSize(self):
		""" Настройка размера разделителя """
		self.splitter.setStretchFactor(0, 5)
		self.splitter.setStretchFactor(1, 2)

	# Таблица данных
	def AdjustTblDataSpan(self):
		""" Настройка объединения ячеек """
		self.tbl_data.setSpan( 5, 0, 1, 2)
		self.tbl_data.setSpan(11, 0, 1, 2)

	def AdjustTblDataSize(self):
		""" Настройка размеров """
		self.tbl_data.resizeColumnToContents(0)

		self.tbl_data.resizeRowToContents( 8)
		self.tbl_data.resizeRowToContents(13)
		self.tbl_data.resizeRowToContents(14)
		self.tbl_data.resizeRowToContents(15)
		self.tbl_data.resizeRowToContents(16)
		self.tbl_data.resizeRowToContents(17)
		self.tbl_data.resizeRowToContents(18)

		for index_row in range(self.model_data.rowCount()):
			row_size : int = self.tbl_data.rowHeight(index_row)
			row_size       = 20 * (row_size // 20)
			self.tbl_data.setRowHeight(index_row, row_size)

	def AdjustTblDataColor(self):
		""" Настройка цветового оформления """
		self.model_data.setRowColor(self.model_data.invisibleRootItem(),   0,    Qt.darkGray, Qt.white)
		self.model_data.setRowColor(self.model_data.invisibleRootItem(),   1,    Qt.white, Qt.darkGray)
		self.model_data.setRowColor(self.model_data.invisibleRootItem(),   2,    Qt.white, Qt.darkGray)
		self.model_data.setRowColor(self.model_data.invisibleRootItem(),   3,    Qt.white, Qt.darkGray)
		self.model_data.setRowColor(self.model_data.invisibleRootItem(),   4,    Qt.white, Qt.darkGray)

		self.model_data.setRowColor(self.model_data.invisibleRootItem(),   6,    Qt.black, Qt.white)
		self.model_data.setCellColor(self.model_data.invisibleRootItem(),  7, 0, Qt.white, Qt.darkGray)
		self.model_data.setCellColor(self.model_data.invisibleRootItem(),  8, 0, Qt.white, Qt.darkGray)
		self.model_data.setCellColor(self.model_data.invisibleRootItem(),  9, 0, Qt.white, Qt.darkGray)
		self.model_data.setCellColor(self.model_data.invisibleRootItem(), 10, 0, Qt.white, Qt.darkGray)

		self.model_data.setRowColor( self.model_data.invisibleRootItem(), 12,    Qt.darkGray, Qt.white)
		self.model_data.setCellColor(self.model_data.invisibleRootItem(), 13, 0, Qt.white, Qt.darkGray)
		self.model_data.setCellColor(self.model_data.invisibleRootItem(), 14, 0, Qt.white, Qt.darkGray)
		self.model_data.setCellColor(self.model_data.invisibleRootItem(), 15, 0, Qt.white, Qt.darkGray)
		self.model_data.setCellColor(self.model_data.invisibleRootItem(), 16, 0, Qt.white, Qt.darkGray)
		self.model_data.setCellColor(self.model_data.invisibleRootItem(), 17, 0, Qt.white, Qt.darkGray)
		self.model_data.setCellColor(self.model_data.invisibleRootItem(), 18, 0, Qt.white, Qt.darkGray)

	# Дерево значений
	def AdjustTreValuesExpand(self):
		""" Настройка дерева значений: Раскрытие """
		self.tre_values.expandAll()

	def AdjustTreValuesCheckable(self):
		""" Настройка дерева значений: Отметки """
		if self._ido_processing == DATE: return

		for index_value in self.model_values.indexes():
			item_value : QStandardItem = self.model_values.itemFromIndex(index_value)
			item_value.setCheckable(True)

	def ShowCurrentValue(self):
		""" Отображение текущего значения """
		if   self._ido_processing == DATE      : self.ShowCurrentValueDd()

		elif self._ido_processing == FINSTRUCT : self.ShowCurrentValueFinstruct()

		elif self._ido_processing == OBJECT_INT: self.ShowCurrentValueFindescription()
		elif self._ido_processing == FREQUENCY : self.ShowCurrentValueFindescription()
		elif self._ido_processing == PRIORITY  : self.ShowCurrentValueFindescription()
		elif self._ido_processing == PROCESS   : self.ShowCurrentValueFindescription()
		elif self._ido_processing == CATEGORY  : self.ShowCurrentValueFindescription()
		elif self._ido_processing == OBJECT_EXT: self.ShowCurrentValueFindescription()

	def ShowCurrentValueDd(self):
		""" Отображение текущего дня месяца """
		self.tre_values.setCurrentIndex(self.model_values.indexByData(self.record_finactions.DdDmDyToString(), Qt.DisplayRole))

	def ShowCurrentValueFinstruct(self):
		""" Отображение текущей финструктуры """
		finstruct_names : list[str] = self.finstruct.IdosToNames(self.record_finactions.FinstructIdos())

		for finstruct_name in finstruct_names:
			item_value : QStandardItem | None = self.model_values.itemByData(finstruct_name)
			if item_value is None: return

			item_value.setCheckState(Qt.Checked)

	def ShowCurrentValueFindescription(self):
		""" Отображение текущего финсостава """
		findescription_names: list[str] = self.findescription.IdosToNames(self.record_finactions.FindescriptionIdos())

		for findescription_name in findescription_names:
			item_value: QStandardItem | None = self.model_values.itemByData(findescription_name)
			if item_value is None: continue

			item_value.setCheckState(Qt.Checked)

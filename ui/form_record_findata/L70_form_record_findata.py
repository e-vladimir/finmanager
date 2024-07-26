# ФОРМА ЗАПИСИ ФИНДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore          import Qt

from L00_dict                import *

from L10_converts            import AmountToString
from L60_form_record_findata import C60_FormRecordFindata
from L90_finstruct           import C90_RecordFinstruct


class C70_FormRecordFindata(C60_FormRecordFindata):
	""" Форма записи финданных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		record_finstruct = C90_RecordFinstruct(self.record_findata.FinstructIdo())

		self.setWindowTitle(f"{AmountToString(self.record_findata.Amount())} от {self.record_findata.DdDmDyToString()} ({record_finstruct.Name()})")

	def AdjustSplitterSize(self):
		""" Настройка размера разделителя """
		self.splitter.setStretchFactor(0, 5)
		self.splitter.setStretchFactor(1, 3)

	# Таблица данных
	def ShowValueFromRecord(self):
		""" Подсветка текущего значения из записи """
		value_current : str = ""

		if   self._ido_processing == DATE     : value_current = self.record_findata.DdDmDyToString()
		elif self._ido_processing == FINSTRUCT: value_current = C90_RecordFinstruct(self.record_findata.FinstructIdo()).Name()

		self.table_values.clearSelection()

		for index_value in self.model_values.indexes():
			if not index_value.data(Qt.DisplayRole) == value_current: continue

			self.table_values.setCurrentIndex(index_value)

			break

	def AdjustTblDataSpan(self):
		""" Настройка объединения ячеек """
		self.table_data.setSpan(0, 0, 1, 2)
		self.table_data.setSpan(5, 0, 1, 2)
		self.table_data.setSpan(6, 0, 1, 2)

	def AdjustTblDataSize(self):
		""" Настройка размеров """
		self.table_data.setColumnWidth(0, 125)

	def AdjustTblDataColor(self):
		""" Настройка цветового оформления """
		self.model_data.setRowColor(self.model_data.invisibleRootItem(),     0, Qt.black, Qt.white)
		self.model_data.setCellColor(self.model_data.invisibleRootItem(), 1, 0, Qt.white, Qt.darkGray)
		self.model_data.setCellColor(self.model_data.invisibleRootItem(), 2, 0, Qt.white, Qt.darkGray)
		self.model_data.setCellColor(self.model_data.invisibleRootItem(), 3, 0, Qt.white, Qt.darkGray)
		self.model_data.setCellColor(self.model_data.invisibleRootItem(), 4, 0, Qt.white, Qt.darkGray)

		self.model_data.setRowColor(self.model_data.invisibleRootItem(), 6, Qt.darkGray, Qt.white)

		for index_row in range(7, self.model_data.rowCount()):
			self.model_data.setRowColor(self.model_data.invisibleRootItem(), index_row, Qt.white, Qt.darkGray)

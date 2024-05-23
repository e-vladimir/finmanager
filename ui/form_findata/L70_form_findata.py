# ФОРМА ФИНДАННЫЕ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore   import QModelIndex
from PySide6.QtGui    import QColor, QStandardItem, QCursor

from G10_math_linear  import CalcBetween

from L00_roles        import *

from L10_converts     import AmountToString
from L60_form_findata import C60_FormFindata
from L90_finactions   import C90_RecordFinactions
from L90_findata      import C90_RecordFindata


class C70_FormFindata(C60_FormFindata):
	""" Форма Финданные: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовок """
		self.setWindowTitle(f"Финданные - {self.workspace.DmDyToString()}")

	# Дерево данных
	def ProcessingDbClickOnTreeData(self):
		""" Обработка двойного клика по дереву данных """
		flag_edit_note : bool = self._index_col_processing == 8

		if   self._oid_processing_finactions and not flag_edit_note : self.on_RequestOpenRecordFinactions()
		elif self._oid_processing_finactions and     flag_edit_note : self.on_RequestEditNoteRecordFinactions()

		elif self._oid_processing_findata    and not flag_edit_note : self.on_RequestOpenRecordFindata()
		elif self._oid_processing_findata    and     flag_edit_note : self.on_RequestEditNoteRecordFindata()

	def AdjustTreeDataSize(self):
		""" Настройка размера """
		sizes_min : list[int] = [100] * 8
		sizes_max : list[int] = [220] * 8

		for index_col in range(len(sizes_min)):
			self.tree_data.resizeColumnToContents(index_col)

			col_size : int = self.tree_data.columnWidth(index_col)
			col_size       = CalcBetween(sizes_min[index_col], col_size, sizes_max[index_col])

			self.tree_data.setColumnWidth(index_col, col_size)

	def AdjustTreeDataExpand(self):
		""" Раскрытие веток """
		self.tree_data.expandAll()

	def AdjustTreeDataColor(self):
		""" Настройка цветовых меток """
		dy : int = self.workspace.Dy()
		dm : int = self.workspace.Dm()

		for oid in self.findata.OidsInDyDmDd(dy, dm):
			record_findata               = C90_RecordFindata(oid)
			index_record : QModelIndex   = self.model_data.indexByData(oid, ROLE_OID_FINDATA)
			if index_record is None: continue

			index_row    : int           = index_record.row()
			index_parent : QModelIndex   = index_record.parent()

			item_parent  : QStandardItem = self.model_data.itemFromIndex(index_parent)

			color_fg     : QColor        = QColor(150, 150, 150)

			if record_findata.LinkedFinactionsOids():
				color_fg: QColor = QColor(0, 0, 0)

				if abs(record_findata.CalcAmountDeviationByLinks()) > 1: color_fg: QColor = QColor(200, 60, 60)

			self.model_data.setRowColor(item_parent, index_row, color_fg=color_fg)

	# Меню данных
	def ShowMenuData(self):
		"""  """
		self.menu_data.exec_(QCursor().pos())

	def AdjustMenuDataText(self):
		"""  """
		self.menu_data_findata_record_header.setTitle("Запись финданных")
		if self._oid_processing_findata:
			record_findata    = C90_RecordFindata(self._oid_processing_findata)

			self.menu_data_findata_record_header.setTitle(f"Запись финданных: {AmountToString(record_findata.Amount(), False, True)} от {record_findata.DdDmDyToString()}")

		self.menu_data_finactions_record_header.setTitle("Запись финдействий")
		if self._oid_processing_finactions:
			record_finactions = C90_RecordFinactions(self._oid_processing_finactions)

			self.menu_data_finactions_record_header.setTitle(f"Запись финдействий: {AmountToString(record_finactions.Amount(), False, True)} от {record_finactions.DdDmDyToString()}")

	def AdjustMenuDataEnable(self):
		"""  """
		flag_findata_selected             : bool = bool(self._oid_processing_findata)
		flag_finactions_selected          : bool = bool(self._oid_processing_finactions)

		flag_findata_selected_multiple    : bool = len(self._oids_processing_findata) > 0
		flag_finactions_selected_multiple : bool = len(self._oids_processing_finactions) > 0

		self.menu_data_findata_create_finactions_quick.setEnabled(flag_findata_selected_multiple)

		self.menu_data_findata_record_open.setEnabled(flag_findata_selected)
		self.menu_data_findata_record_delete.setEnabled(flag_findata_selected)
		self.menu_data_findata_record_create_finactions.setEnabled(flag_findata_selected)
		self.menu_data_findata_record_create_finactions_quick.setEnabled(flag_findata_selected)

		self.menu_data_finactions_record_open.setEnabled(flag_finactions_selected)
		self.menu_data_finactions_record_delete.setEnabled(flag_finactions_selected)

		self.menu_data_rules_replace_text.setEnabled(flag_findata_selected or flag_findata_selected_multiple)
		self.menu_data_rules_detect_findescription.setEnabled(flag_finactions_selected or flag_finactions_selected_multiple)

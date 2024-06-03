# ФОРМА ФИНДАННЫЕ: МЕХАНИКА ДАННЫХ

from PySide6.QtCore      import QModelIndex, Qt
from PySide6.QtGui import QStandardItem, QColor

from L00_findescription import *
from L00_roles           import *

from L10_converts        import AmountToString
from L20_PySide6         import C20_StandardItem
from L50_form_findata    import C50_FormFindata
from L90_finactions      import C90_RecordFinactions
from L90_findata         import C90_RecordFindata


class C60_FormFindata(C50_FormFindata):
	""" Форма Финданные: Механика данных """

	# Параметры
	def ReadIndexColProcessing(self):
		""" Чтение индекса колонки """
		self._index_col_processing = 0

		current_index : QModelIndex | None = self.tree_data.currentIndex()
		if not current_index.isValid(): return
		if     current_index is None  : return

		self._index_col_processing = current_index.column()

	def ReadDdProcessing(self):
		""" Чтение дня месяца """
		self._dd_processing = 0

		current_index : QModelIndex | None = self.tree_data.currentIndex()
		if not current_index.isValid(): return
		if     current_index is None  : return

		dd            : int         | None = current_index.data(ROLE_DD)
		if     dd is None             : return

		self._dd_processing = dd

	def ReadOidProcessingFindata(self):
		""" Чтение OID записи финданных """
		self._oid_processing_findata = ""

		current_index : QModelIndex | None = self.tree_data.currentIndex()
		if current_index is None: return

		self._oid_processing_findata = current_index.data(ROLE_OID_FINDATA)

	def ReadOidProcessingFinactions(self):
		""" Чтение OID записи финдействий """
		self._oid_processing_finactions = ""

		current_index : QModelIndex | None = self.tree_data.currentIndex()
		if current_index is None: return

		self._oid_processing_finactions = current_index.data(ROLE_OID_FINACTIONS)

	def ReadOidsProcessingFindata(self):
		""" Чтение выбранных записей финданных """
		self._oids_processing_findata.clear()

		for index_data in self.model_data.indexes():
			item_data  : QStandardItem = self.model_data.itemFromIndex(index_data)

			oid_findata : str | None   = item_data.data(ROLE_OID_FINDATA)
			if not oid_findata                         : continue
			if     oid_findata is None                 : continue
			if not item_data.checkState() == Qt.Checked: continue

			self._oids_processing_findata.append(oid_findata)

	def ReadOidsProcessingFinactions(self):
		""" Чтение выбранных записей финдействий """
		self._oids_processing_finactions.clear()

		for index_data in self.model_data.indexes():
			item_data  : QStandardItem = self.model_data.itemFromIndex(index_data)

			oid_finactions : str | None   = item_data.data(ROLE_OID_FINACTIONS)
			if not oid_finactions                      : continue
			if     oid_finactions is None              : continue
			if not item_data.checkState() == Qt.Checked: continue

			self._oids_processing_finactions.append(oid_finactions)

	def SwitchProcessingQuick_On(self):
		""" Переключение флага ускорения """
		self._flag_quick = True

	def SwitchProcessingQuick_Off(self):
		""" Переключение флага ускорения """
		self._flag_quick = False

	def SwitchProcessing_Dec(self):
		""" Переключение режима обработки на Уменьшение """
		self._flag_processing_dec = True

	def SwitchProcessing_Inc(self):
		""" Переключение режима обработки на Увеличение """
		self._flag_processing_dec = False

	def SwitchProcessingSkip_On(self):
		""" Включение пропуска обработки """
		self._flag_processing_skip = True

	def SwitchProcessingSkip_Off(self):
		""" Отключение пропуска обработки """
		self._flag_processing_skip = False

	# Модель данных
	def SetupModelData(self):
		""" Настройка модели """
		self.model_data.setHorizontalHeaderLabels(["Дата/Сумма",
		                                           "Финструктура",
		                                           "Объект внутренний",
		                                           "Периодичность",
		                                           "Приоритет",
		                                           "Процесс",
		                                           "Категории",
		                                           "Объект внешний",
		                                           "Примечание"])

	# День месяца
	def LoadDd(self):
		""" Загрузка дня месяца """
		if not self._dd_processing: return

		dd_label    : str           = f"{self._dd_processing:02d} {self.workspace.DmDyToString()}"

		if self.model_data.indexByData(dd_label) is not None: return

		labels      : list[str]     = [""] * 9
		labels[0]                   = dd_label
		index_row   : int           = self.model_data.rowCount()

		item_parent : QStandardItem = self.model_data.invisibleRootItem()

		for index_col, label in enumerate(labels):
			item_data = C20_StandardItem(label, flag_bold=True)
			item_data.setData(self._dd_processing, ROLE_DD)
			item_parent.setChild(index_row, index_col, item_data)

	def CleanDd(self):
		""" Очистка дня от данных """
		if not self._dd_processing: return

		index_dd  : QModelIndex | None = self.model_data.indexByData(self._dd_processing, ROLE_DD)
		if index_dd is None: return

		count     : int                = self.model_data.rowCount(index_dd)

		self.model_data.removeRows(0, count, index_dd)

	def RemoveDd(self):
		""" Удаление дня из дерева """
		if not self._dd_processing: return

		index_dd  : QModelIndex | None = self.model_data.indexByData(self._dd_processing, ROLE_DD)
		if index_dd is None: return

		index_row : int                = index_dd.row()

		self.model_data.removeRow(index_row, QModelIndex())

	# Запись финданных
	def CleanRecordFindata(self):
		""" Очистка записи финданных """
		if not self._oid_processing_findata: return

		index_record : QModelIndex | None = self.model_data.indexByData(self._oid_processing_findata, ROLE_OID_FINDATA)
		if index_record is None: return

		count        : int                = self.model_data.rowCount(index_record)

		self.model_data.removeRows(0, count, index_record)

	def LoadRecordFindata(self):
		""" Загрузка записи финданных """
		if not self._oid_processing_findata: return

		record_findata                = C90_RecordFindata(self._oid_processing_findata)

		self._dd_processing = record_findata.Dd()
		self.LoadDd()

		labels        : list[str]     = [""] * 9
		labels[0] = AmountToString(record_findata.Amount(), False, True)
		labels[1] = ', '.join(self.finstruct.OidsToNames([record_findata.FinstructOid()]))
		labels[8] = record_findata.Note()

		index_dd      : QModelIndex   = self.model_data.indexByData(record_findata.DdDmDyToString())
		index_findata : QModelIndex   = self.model_data.indexByData(self._oid_processing_findata, ROLE_OID_FINDATA)

		index_row     : int           = self.model_data.rowCount(index_dd) if index_findata is None else index_findata.row()

		item_dd       : QStandardItem = self.model_data.itemFromIndex(index_dd)

		item_parent   : QStandardItem = item_dd

		for index_col, label in enumerate(labels):
			item_data = C20_StandardItem(label, flag_align_right = index_col == 0, flag_checked = False if index_col == 0 else None)
			item_data.setData(self._oid_processing_findata, ROLE_OID_FINDATA)
			item_data.setData(record_findata.Dd(), ROLE_DD)
			item_parent.setChild(index_row, index_col, item_data)

	def UpdateRecordFindata(self):
		""" Обновление данных записи финданных """
		if not self._oid_processing_findata: return

		record_findata                    = C90_RecordFindata(self._oid_processing_findata)

		index_record : QModelIndex | None = self.model_data.indexByData(self._oid_processing_findata, ROLE_OID_FINDATA)
		index_parent : QModelIndex        = index_record.parent()

		index_row    : int                = index_record.row()
		item_parent  : QStandardItem      = self.model_data.itemFromIndex(index_parent)

		item_note    : QStandardItem      = item_parent.child(index_row, 8)
		item_note.setText(record_findata.Note())

	def RemoveRecordFindata(self):
		""" Удаление записи финданных из дерева """
		if not self._oid_processing_findata: return

		index_record : QModelIndex | None = self.model_data.indexByData(self._oid_processing_findata, ROLE_OID_FINDATA)
		if     index_record is None  : return
		if not index_record.isValid(): return

		index_parent : QModelIndex        = index_record.parent()
		index_row    : int                = index_record.row()

		self.model_data.removeRow(index_row, index_parent)

	def SetupRecordFindataColor(self):
		""" Установка цвета записи финданных """
		if not self._oid_processing_findata: return

		index_record: QModelIndex = self.model_data.indexByData(self._oid_processing_findata, ROLE_OID_FINDATA)
		if index_record is None: return

		index_row: int = index_record.row()
		index_parent: QModelIndex = index_record.parent()

		item_parent: QStandardItem = self.model_data.itemFromIndex(index_parent)

		color_fg: QColor = QColor(150, 150, 150)

		record_findata = C90_RecordFindata(self._oid_processing_findata)

		if record_findata.LinkedFinactionsOids():
			color_fg: QColor = QColor(0, 0, 0)

			if abs(record_findata.CalcAmountDeviationByLinks()) > 1: color_fg: QColor = QColor(200, 60, 60)

		self.model_data.setRowColor(item_parent, index_row, color_fg=color_fg)

	# Запись финдействий
	def LoadRecordFinactions(self):
		""" Загрузка записи финдействий """
		if not self._oid_processing_findata: return

		record_findata                  = C90_RecordFindata(self._oid_processing_findata)

		oids_finactions : list[str]     = record_findata.LinkedFinactionsOids()

		index_findata   : QModelIndex   = self.model_data.indexByData(record_findata.Oid().text, ROLE_OID_FINDATA)
		item_findata    : QStandardItem = self.model_data.itemFromIndex(index_findata)

		index_dd        : QModelIndex   = index_findata.parent()
		item_dd         : QStandardItem = self.model_data.itemFromIndex(index_dd)

		if len(oids_finactions) == 0:
			return

		elif len(oids_finactions) == 1:
			index_row : int       = item_findata.row()

			record_finactions     = C90_RecordFinactions(oids_finactions[0])

			labels    : list[str] = [""] * 9
			labels[0]             = AmountToString(record_finactions.Amount(), False, True)
			labels[1]             = ', '.join(self.finstruct.OidsToNames(record_finactions.FinstructOids()))
			labels[2]             = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), OBJECT_INT))
			labels[3]             = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), FREQUENCY))
			labels[4]             = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), PRIORITY))
			labels[5]             = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), PROCESS))
			labels[6]             = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), CATEGORY))
			labels[7]             = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), OBJECT_EXT))
			labels[8]             = record_finactions.Note()

			for index_col, label in enumerate(labels):
				item_data = C20_StandardItem(label, flag_align_right=index_col == 0, flag_checked = False if index_col == 0 else None)
				item_data.setData(record_findata.Dd(),          ROLE_DD)
				item_data.setData(record_findata.Oid().text,    ROLE_OID_FINDATA)
				item_data.setData(record_finactions.Oid().text, ROLE_OID_FINACTIONS)

				item_dd.setChild(index_row, index_col, item_data)

		elif len(oids_finactions) > 1:
			for index_row, oid in enumerate(oids_finactions):
				record_finactions = C90_RecordFinactions(oid)

				labels: list[str] = [""] * 9
				labels[0] = AmountToString(record_finactions.Amount(), False, True)
				labels[1] = ', '.join(self.finstruct.OidsToNames(record_finactions.FinstructOids()))
				labels[2] = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), OBJECT_INT))
				labels[3] = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), FREQUENCY))
				labels[4] = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), PRIORITY))
				labels[5] = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), PROCESS))
				labels[6] = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), CATEGORY))
				labels[7] = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), OBJECT_EXT))
				labels[8] = record_finactions.Note()

				for index_col, label in enumerate(labels):
					item_data = C20_StandardItem(label, flag_align_right = index_col == 0, flag_checked = False if index_col == 0 else None)
					item_data.setData(record_findata.Oid().text, ROLE_OID_FINDATA)
					item_data.setData(record_finactions.Oid().text, ROLE_OID_FINACTIONS)

					item_findata.setChild(index_row, index_col, item_data)

	def UpdateRecordFinactions(self):
		""" Обновление данных записи финдействий """
		if not self._oid_processing_finactions: return

		record_finactions                 = C90_RecordFinactions(self._oid_processing_finactions)

		index_record : QModelIndex | None = self.model_data.indexByData(self._oid_processing_finactions, ROLE_OID_FINACTIONS)
		index_parent : QModelIndex        = index_record.parent()

		index_row    : int                = index_record.row()
		item_parent  : QStandardItem      = self.model_data.itemFromIndex(index_parent)

		labels: list[str] = [""] * 9
		labels[0] = AmountToString(record_finactions.Amount(), False, True)
		labels[1] = ', '.join(self.finstruct.OidsToNames(record_finactions.FinstructOids()))
		labels[2] = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), OBJECT_INT))
		labels[3] = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), FREQUENCY))
		labels[4] = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), PRIORITY))
		labels[5] = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), PROCESS))
		labels[6] = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), CATEGORY))
		labels[7] = ', '.join(self.findescription.OidsToNames(record_finactions.FindescriptionOids(), OBJECT_EXT))
		labels[8] = record_finactions.Note()

		for index_col, label in enumerate(labels):
			item_data = item_parent.child(index_row, index_col)
			item_data.setText(label)

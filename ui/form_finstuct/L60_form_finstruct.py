# ФОРМА ФИНСТРУКТУРЫ: МЕХАНИКА ДАННЫХ

from PySide6.QtCore     import Qt, QModelIndex
from PySide6.QtGui      import QStandardItem, QColor

from L00_containers     import CONTAINER_LOCAL

from L10_converts       import AmountToString
from L20_PySide6        import ItemsFromStandardModel, C20_StandardItem, ROLE_OID
from L50_form_finstruct import C50_FormFinstruct
from L90_finstate       import C90_RecordFinstate
from L90_finstruct      import C90_RecordFinstruct


class C60_FormFinstruct(C50_FormFinstruct):
	""" Форма Финструктуры: Механика данных """

	# Модель финструктуры
	def SetupModelSort(self):
		self.model_data.sort(0)

	def SetupModel(self):
		""" Сброс данных """
		self.model_data.removeAll()

		self.model_data.setHorizontalHeaderLabels(["Запись финструктуры", "Было", "Стало", "Изменилось", "Поступило", "Выбыло"])

		for index_column in range(1, 6):
			header_item : QStandardItem = self.model_data.horizontalHeaderItem(index_column)
			header_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

	def CleanModel(self):
		""" Зачистка модели от пустых записей """
		idos : list[str] = C90_RecordFinstruct().Idos(CONTAINER_LOCAL).items

		for item in reversed(ItemsFromStandardModel(self.model_data)):
			if item.data(ROLE_OID) in idos: continue

			parent    : QStandardItem = item.parent()
			if parent is None : parent = self.model_data.invisibleRootItem()

			index_row : int           = item.row()
			parent.removeRow(index_row)

	# Запись финструктуры
	def LoadRecordFinstruct(self):
		""" Загрузка записи финструктуры """
		if not self._ido_processing: return

		record_finstruct                    = C90_RecordFinstruct(self._ido_processing)

		record_finstate                     = C90_RecordFinstate()
		record_finstate.SwitchByFinstructIdo(record_finstruct.Ido().data)

		ido_parent   : str                  = record_finstruct.ParentIdo()

		index_record : QModelIndex|None     = self.model_data.indexByData(record_finstruct.Ido().data, ROLE_OID)

		item_parent  : QStandardItem | None = self.model_data.itemByData(ido_parent, ROLE_OID) if ido_parent else self.model_data.invisibleRootItem()
		if item_parent is None: return

		index_row    : int                  = item_parent.rowCount() if index_record is None else index_record.row()

		remains_initial : int = record_finstate.RemainsInitial()
		remains_final   : int = record_finstate.CalcRemainFinal()
		remains_delta   : int = remains_final - remains_initial
		amount_income   : int = record_finstate.CalcIncome()
		amount_outcome  : int = record_finstate.CalcOutcome()

		labels : list[str] = [""] * 6
		labels[0] = record_finstruct.Name()
		labels[1] = AmountToString(remains_initial)
		labels[2] = AmountToString(remains_final)
		labels[3] = AmountToString(remains_delta,  flag_sign=True)
		labels[4] = AmountToString(amount_income,  flag_sign=True)
		labels[5] = AmountToString(amount_outcome, flag_sign=True)

		for index_col, label in enumerate(labels):
			item_data = C20_StandardItem(label, record_finstruct.Ido().data, ROLE_OID, index_col > 0)
			item_parent.setChild(index_row, index_col, item_data)

		for self._ido_processing in record_finstruct.SubIdos(): self.LoadRecordFinstruct()

	# Параметры
	def ReadIdoProcessing(self):
		""" Чтение OID выделенной записи """
		self._ido_processing = ""

		index_selected : QModelIndex | None = self.tree_data.currentIndex()
		if index_selected is None: return

		self._ido_processing = index_selected.data(ROLE_OID)

	def ReadColProcessing(self):
		""" Чтение выбранной колонки """
		self._col_processing = ""

		index_selected : QModelIndex | None = self.tree_data.currentIndex()
		if index_selected is None: return

		self._col_processing = index_selected.column()

	def ReadIdoMemory(self):
		""" Запомнить OID записи финсостава """
		self._ido_memory = self._ido_processing

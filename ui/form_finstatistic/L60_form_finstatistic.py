# ФОРМА ФИНСТАТИСТИКА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore        import Qt, QModelIndex
from PySide6.QtGui         import QStandardItem

from L00_roles             import ROLE_SUBOID

from L10_converts          import AmountToString
from L20_PySide6           import ROLE_OID
from L50_form_finstatistic import C50_FormFinstatistic
from L90_findescription    import C90_RecordFindescription


class C60_FormFinstatistic(C50_FormFinstatistic):
	""" Форма Финстатистика: Механика данных """

	# Парамеры
	def ReadIndexProcessing(self):
		"""  """
		self._index_processing : QModelIndex | None = self.tree_finstatistic.currentIndex()
		if self._index_processing.isValid(): return

		self._index_processing                      = None

	def CalcIdosStructProcessingFromSubidos(self):
		""" Вычисление структуры записей финстатистики """
		self._idos_struct_processing.clear()

		index_current : QModelIndex = self.tree_finstatistic.currentIndex()
		if not index_current.isValid(): return

		self._idos_struct_processing.append(index_current.data(ROLE_SUBOID))

		index_parent : QModelIndex = index_current.parent()

		while index_parent.isValid():
			sub_ido : str = index_parent.data(ROLE_SUBOID)
			if not sub_ido: return

			self._idos_struct_processing.insert(0, sub_ido)
			index_parent  = index_parent.parent()

	# Модель финстатистики
	def SetupModelFinstatistic(self):
		""" Настройка модели """
		self.model_finstatistic.setHorizontalHeaderLabels(["Финсостав", "Доход", "Расход"])

	def LoadRecordFinstatistic(self):
		""" Загрузка записи финстатистики в модель финстатистики за финпериод"""
		if not self._ido_processing: return

		record_findescription                 = C90_RecordFindescription(self._ido_processing)

		dy             : int                  = self.workspace.Dy()
		dm             : int                  = self.workspace.Dm()
		amount_income  : int                  = self.finstatistic.CalcIncomeByFindescription(self._ido_processing, dy, dm)
		amount_outcome : int                  = self.finstatistic.CalcOutcomeByFindescription(self._ido_processing, dy, dm)

		subidos        : list[str]            = self.findescription.SubIdos(self._ido_processing)

		item_parent    : QStandardItem | None = self.model_finstatistic.itemByData(record_findescription.ParentIdo(), ROLE_OID)
		if item_parent is None: item_parent = self.model_finstatistic.invisibleRootItem()

		item_record    : QStandardItem        = QStandardItem()
		item_record.setText(record_findescription.Name())
		item_record.setData(self._ido_processing, ROLE_OID)

		if not subidos: item_record.setData(self._ido_processing, ROLE_SUBOID)

		item_income    : QStandardItem        = QStandardItem()
		item_income.setText(AmountToString(amount_income, False, True))
		item_income.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

		item_outcome   : QStandardItem        = QStandardItem()
		item_outcome.setText(AmountToString(amount_outcome, False, True))
		item_outcome.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

		item_parent.appendRow([item_record, item_income, item_outcome])

		for self._ido_processing in subidos: self.LoadRecordFinstatistic()

	def LoadSubRecordFinstatistic(self):
		""" Загрузка вложенной записи """
		if     self._ido_processing in self._idos_struct_processing: return
		if not self._index_processing.isValid()                    : return

		dy             : int = self.workspace.Dy()
		dm             : int = self.workspace.Dm()

		amount_income  : int = self.finstatistic.CalcIncomeByFindescriptions(self._idos_struct_processing + [self._ido_processing], dy, dm)
		amount_outcome : int = self.finstatistic.CalcOutcomeByFindescriptions(self._idos_struct_processing + [self._ido_processing], dy, dm)

		record_findescription = C90_RecordFindescription(self._ido_processing)

		if not amount_income and not amount_outcome: return

		item_parent    : QStandardItem | None = self.model_finstatistic.itemFromIndex(self._index_processing)

		item_record    : QStandardItem        = QStandardItem()
		item_record.setText(record_findescription.Name())
		item_record.setData(self._ido_processing, ROLE_SUBOID)

		item_income    : QStandardItem        = QStandardItem()
		item_income.setText(AmountToString(amount_income, False, True))
		item_income.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

		item_outcome   : QStandardItem        = QStandardItem()
		item_outcome.setText(AmountToString(amount_outcome, False, True))
		item_outcome.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

		item_parent.appendRow([item_record, item_income, item_outcome])

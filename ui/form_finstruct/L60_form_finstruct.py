# ФОРМА ФИНСТРУКТУРА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore     import QModelIndex, Qt

from G11_convertor_data import AmountToString

from L20_PySide6        import C20_StandardItem, ROLE_IDO
from L50_form_finstruct import C50_FormFinstruct
from L90_finstruct      import C90_FinstructRecord


class C60_FormFinstruct(C50_FormFinstruct):
	""" Форма Финструктура: Механика данных """

	# Параметры
	def ReadProcessingIdo(self):
		""" Чтение IDO счёта """
		self._processing_ido = ""

		current_index : QModelIndex = self.tree_data.currentIndex()
		if not current_index.isValid(): return

		current_item                = self.model_data.itemFromIndex(current_index)
		current_row                 = current_item.row()
		parent_item                 = current_item.parent()
		if     parent_item is None    : return

		current_item                = parent_item.child(current_row, 0)

		self._processing_ido = current_item.data(ROLE_IDO)

	def ReadProcessingName(self):
		""" Чтение наименование счёта """
		self._processing_name = ""

		current_index : QModelIndex = self.tree_data.currentIndex()
		if not current_index.isValid(): return

		current_item                = self.model_data.itemFromIndex(current_index)
		current_row                 = current_item.row()
		parent_item                 = current_item.parent()
		if     parent_item is None    : return

		current_item                = parent_item.child(current_row, 0)

		self._processing_name = current_item.text()

	def ReadProcessingGroup(self):
		""" Чтение группы счетов """
		self._processing_group = ""

		current_index : QModelIndex = self.tree_data.currentIndex()
		if not current_index.isValid(): return

		current_item                = self.model_data.itemFromIndex(current_index)
		current_row                 = current_item.row()
		parent_item                 = current_item.parent()

		if parent_item is None:	parent_item = self.model_data.invisibleRootItem()

		current_item                = parent_item.child(current_row, 0)

		result_top    : bool        = parent_item == self.model_data.invisibleRootItem()

		if result_top: self._processing_group = current_item.text()
		else         : self._processing_group = parent_item.text()

	def ReadProcessingRow(self):
		""" Чтение рабочей строки """
		index_index : QModelIndex = self.tree_data.currentIndex()
		self._processing_row = index_index.row()

	def ReadProcessingColumn(self):
		""" Чтение рабочей колонки """
		index_index : QModelIndex = self.tree_data.currentIndex()
		self._processing_column = index_index.column()

	# Модель данных
	def InitModel(self):
		""" Инициализация модели данных """
		self.model_data.removeAll()

		self.model_data.setHorizontalHeaderLabels(["Счёт", "Ост-Н", "Ост-К", "Изменение", "Поступило", "Выбыло"])

	def CleanModel(self):
		""" Очистка модели от несуществующих данных """
		dy, dm = self.workspace.DyDm()
		groups = self.finstruct.Groups(dy, dm)
		idos   = self.finstruct.Idos(dy, dm)

		for index_row in reversed(range(self.model_data.rowCount())):
			index_group = self.model_data.index(index_row, 0)
			group_name  = index_group.data(Qt.ItemDataRole.DisplayRole)

			if group_name not in groups:
				self.model_data.removeRow(index_row)
				continue

			for index_subrow in reversed(range(self.model_data.rowCount(index_group))):
				index_record = self.model_data.index(index_subrow, 0, index_group)
				ido          = index_record.data(ROLE_IDO)

				if ido in idos: continue

				self.model_data.removeRow(index_subrow, index_group)

	def LoadFinstructGroup(self):
		""" Загрузка группы счетов """
		if not self._processing_name  : return

		index_group : QModelIndex | None = self.model_data.itemByData(self._processing_name)
		if     index_group is not None: return

		item_group                       = C20_StandardItem(self._processing_name)
		item_parent                      = self.model_data.invisibleRootItem()

		item_parent.appendRow([item_group, C20_StandardItem(""), C20_StandardItem(""), C20_StandardItem(""), C20_StandardItem(""), C20_StandardItem("")])

	def LoadFinstructRecord(self):
		""" Загрузка счета """
		if not self._processing_ido: return

		record                                = C90_FinstructRecord(self._processing_ido)
		item_group  : C20_StandardItem | None = self.model_data.itemByData(record.Group(), Qt.ItemDataRole.DisplayRole)

		if     item_group is None  : return

		item_record : C20_StandardItem | None = self.model_data.itemByData(self._processing_ido, ROLE_IDO)

		if item_record is None:
			item_record         = C20_StandardItem(record.Name(), self._processing_ido, ROLE_IDO)
			item_balance_start  = C20_StandardItem("0", flag_align_right=True)
			item_balance_calc   = C20_StandardItem("0", flag_align_right=True)
			item_balance_delta  = C20_StandardItem("0", flag_align_right=True)
			item_amount_income  = C20_StandardItem("0", flag_align_right=True)
			item_amount_outcome = C20_StandardItem("0", flag_align_right=True)

			item_group.appendRow([item_record, item_balance_start, item_balance_calc, item_balance_delta, item_amount_income, item_amount_outcome])

		index_row   : int                     = item_record.row()

		balance_start                         = record.BalanceStart()
		balance_calc                          = record.BalanceCalc()
		balance_delta                         = balance_calc - balance_start
		amount_income                         = record.AmountIncome()
		amount_outcome                        = record.AmountOutcome()

		item_record.setText(record.Name())

		item_balance_start                    = item_group.child(index_row, 1)
		item_balance_start.setText(AmountToString(balance_start))

		item_balance_calc                     = item_group.child(index_row, 2)
		item_balance_calc.setText(AmountToString(balance_calc))

		item_balance_delta                    = item_group.child(index_row, 3)
		item_balance_delta.setText(AmountToString(balance_delta))

		item_amount_income                    = item_group.child(index_row, 4)
		item_amount_income.setText(AmountToString(amount_income))

		item_amount_outcome                   = item_group.child(index_row, 5)
		item_amount_outcome.setText(AmountToString(amount_outcome))

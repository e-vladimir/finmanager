# ФОРМА ФИНСТРУКТУРА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore     import QModelIndex, Qt

from L20_PySide6        import C20_StandardItem, ROLE_IDO
from L50_form_finstruct import C50_FormFinstruct
from L90_finstruct      import C90_FinstructRecord


class C60_FormFinstruct(C50_FormFinstruct):
	""" Форма Финструктура: Механика данных """

	# Параметры
	def ReadProcessingIdo(self):
		""" Чтение IDO счёта """
		index_current : QModelIndex = self.tree_data.currentIndex()
		self._processing_ido = index_current.data(ROLE_IDO)

	def ReadProcessingName(self):
		""" Чтение наименование счёта """
		self._processing_name = ""

		index_current : QModelIndex = self.tree_data.currentIndex()
		ido           : str         = index_current.data(ROLE_IDO)

		if not ido: return

		self._processing_name = index_current.data(Qt.ItemDataRole.DisplayRole)

	def ReadGroupProcessing(self):
		""" Чтение группы счетов """
		self._group_processing = ""

		index_current : QModelIndex = self.tree_data.currentIndex()
		ido           : str         = index_current.data(ROLE_IDO)

		if not ido: self._group_processing = index_current.data(Qt.ItemDataRole.DisplayRole)
		else      :	self._group_processing = index_current.parent().data(Qt.ItemDataRole.DisplayRole)

	# Модель данных
	def InitModel(self):
		""" Инициализация модели данных """
		self.model_data.removeAll()

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

		item_parent.appendRow(item_group)

	def LoadFinstructRecord(self):
		""" Загрузка счета """
		if not self._processing_ido: return

		record                                = C90_FinstructRecord(self._processing_ido)
		item_group  : C20_StandardItem | None = self.model_data.itemByData(record.Group(), Qt.ItemDataRole.DisplayRole)

		if     item_group is None  : return

		item_record : C20_StandardItem | None = self.model_data.itemByData(self._processing_ido, ROLE_IDO)

		if item_record is None:
			item_record = C20_StandardItem(record.Name(), self._processing_ido, ROLE_IDO)
			item_group.appendRow(item_record)

		item_record.setText(record.Name())

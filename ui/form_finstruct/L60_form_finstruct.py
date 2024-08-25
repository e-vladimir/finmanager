# ФОРМА ФИНСТРУКТУРА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore     import QModelIndex, Qt

from L20_PySide6        import C20_StandardItem, ROLE_IDO
from L50_form_finstruct import C50_FormFinstruct
from L90_finstruct      import C90_FinstructRecord


class C60_FormFinstruct(C50_FormFinstruct):
	""" Форма Финструктура: Механика данных """

	# Параметры
	def ReadIdoProcessing(self):
		""" Чтение IDO счёта """
		index_current : QModelIndex = self.tree_data.currentIndex()
		self._ido_processing = index_current.data(ROLE_IDO)

	def ReadNameProcessing(self):
		""" Чтение наименование счёта """
		self._name_processing = ""

		index_current : QModelIndex = self.tree_data.currentIndex()
		ido           : str         = index_current.data(ROLE_IDO)

		if not ido: return

		self._name_processing = index_current.data(Qt.ItemDataRole.DisplayRole)

	def ReadGroupProcessing(self):
		""" Чтение группы счетов """
		self._name_processing = ""

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
		pass

	def LoadFinstructGroup(self):
		""" Загрузка группы счетов """
		if not self._name_processing  : return

		index_group : QModelIndex | None = self.model_data.itemByData(self._name_processing)
		if     index_group is not None: return

		item_group  = C20_StandardItem(self._name_processing)
		item_parent = self.model_data.invisibleRootItem()

		item_parent.appendRow(item_group)

	def LoadFinstructRecord(self):
		""" Загрузка счета """
		if not self._ido_processing: return

		record                                = C90_FinstructRecord(self._ido_processing)
		item_group  : C20_StandardItem | None = self.model_data.itemByData(record.Group(), Qt.ItemDataRole.DisplayRole)

		if     item_group is None  : return

		item_record : C20_StandardItem | None = self.model_data.itemByData(self._ido_processing, ROLE_IDO)

		if item_record is None:
			item_record = C20_StandardItem(record.Name(), self._ido_processing, ROLE_IDO)
			item_group.appendRow(item_record)

		item_record.setText(record.Name())

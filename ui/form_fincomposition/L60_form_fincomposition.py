# ФОРМА ФИНСОСТАВ: МЕХАНИКА ДАННЫХ

from PySide6.QtCore          import Qt

from L20_PySide6             import ROLE_IDO, C20_StandardItem
from L50_form_fincomposition import C50_FormFincomposition
from L90_fincomposition      import C90_FincompositionRecord


class C60_FormFincomposition(C50_FormFincomposition):
	""" Форма Финсостав: Механика данных """

	# Параметры
	def ReadProcessingIdoFromTreeData(self):
		""" Чтение IDO текущей записи """
		index_current = self.tree_data.currentIndex()
		self._processing_ido = index_current.data(ROLE_IDO)

	def ReadProcessingNameFromTreeData(self):
		""" Чтение наименование текущей записи """
		index_current = self.tree_data.currentIndex()
		self._processing_name = index_current.data(Qt.ItemDataRole.DisplayRole)

	def MemoryProcessingName(self):
		""" Запоминание наименования текущей записи """
		self._name_memory = self._processing_name

	# Модель данных
	def InitModelData(self):
		""" Инициализация модели данных """
		self.model_data.removeAll()

	def LoadRecordFincomposition(self):
		""" Загрузка записи финсостава """
		if not self._processing_ido: return

		record                                = C90_FincompositionRecord(self._processing_ido)

		item_record : C20_StandardItem | None = self.model_data.itemByData(self._processing_ido, ROLE_IDO)

		if item_record is None:
			item_record                           = C20_StandardItem(record.Name(), record.Ido().data)
			item_parent : C20_StandardItem | None = self.model_data.itemByData(record.ParentIdo(), ROLE_IDO)

			if item_parent is None: item_parent = self.model_data.invisibleRootItem()

			item_parent.appendRow(item_record)

		item_record.setText(record.Name())

		for self._processing_ido in record.SubIdos(): self.LoadRecordFincomposition()

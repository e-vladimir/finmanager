# ФОРМА ФИНСОСТАВ: МЕХАНИКА ДАННЫХ

from L20_PySide6             import ROLE_IDO, C20_StandardItem
from L50_form_fincomposition import C50_FormFincomposition
from L90_fincomposition      import C90_FincompositionRecord


class C60_FormFincomposition(C50_FormFincomposition):
	""" Форма Финсостав: Механика данных """

	# Параметры
	def ReadIdoProcessingFromTreeData(self):
		""" Чтение IDO текущей записи """
		index_current = self.tree_data.currentIndex()
		self._ido_processing = index_current.data(ROLE_IDO)

	# Модель данных
	def InitModelData(self):
		""" Инициализация модели данных """
		self.model_data.removeAll()

	def LoadRecordFincomposition(self):
		""" Загрузка записи финсостава """
		if not self._ido_processing: return

		record                                = C90_FincompositionRecord(self._ido_processing)

		item_record : C20_StandardItem | None = self.model_data.itemByData(self._ido_processing, ROLE_IDO)

		if item_record is None:
			item_record                           = C20_StandardItem(record.Name(), record.Ido().data)
			item_parent : C20_StandardItem | None = self.model_data.itemByData(record.ParentIdo(), ROLE_IDO)

			if item_parent is None: item_parent = self.model_data.invisibleRootItem()

			item_parent.appendRow(item_record)

		item_record.setText(record.Name())

		for self._ido_processing in record.SubIdos(): self.LoadRecordFincomposition()

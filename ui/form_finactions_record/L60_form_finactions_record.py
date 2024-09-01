# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: МЕХАНИКА ДАННЫХ

from PySide6.QtGui              import QStandardItem, Qt

from L20_PySide6                import ROLE_IDO, C20_StandardItem
from L50_form_finactions_record import C50_FormFinactionsRecord
from L90_finstruct              import C90_FinstructRecord


class C60_FormFinactionsRecord(C50_FormFinactionsRecord):
	""" Форма Запись финдействий: Механика данных """

	# Запись финдействий
	def ReadFinactionsRecordIdo(self):
		""" Чтение IDO из рабочего пространства """
		self.finactions_record.Ido(self.workspace.IdoFinactionsRecord())

	def SendFinactionsRecordIdo(self):
		""" Запись IDO в рабочее пространство """
		self.workspace.IdoFinactionsRecord(self.finactions_record.Ido().data)

	# Модель финструктуры
	def InitModelFinstruct(self):
		""" Инициализация модели финструктуры """
		self.model_finstruct.removeAll()

	def LoadFinstructGroup(self):
		""" Загрузка группы финструктуры """
		item_root  : QStandardItem           = self.model_finstruct.invisibleRootItem()
		item_group : C20_StandardItem | None = self.model_finstruct.itemByData(self._processing_name, Qt.ItemDataRole.DisplayRole)

		if item_group is not None: return

		item_group                           = C20_StandardItem(self._processing_name)
		item_root.appendRow(item_group)

	def LoadFinstructRecord(self):
		""" Загрузка записи финструктуры """
		record                                = C90_FinstructRecord(self._processing_ido)

		item_group  : C20_StandardItem | None = self.model_finstruct.itemByData(record.Group(), Qt.ItemDataRole.DisplayRole)
		if item_group  is     None: return

		item_record : C20_StandardItem | None = self.model_finstruct.itemByData(self._processing_ido, ROLE_IDO)
		if item_record is not None: return

		item_record                           = C20_StandardItem(record.Name(), self._processing_ido, ROLE_IDO)
		item_record.setCheckable(True)

		item_group.appendRow(item_record)

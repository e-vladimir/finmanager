# ФОРМА ФИНДЕЙСТВИЯ: МЕХАНИКА ДАННЫХ

from PySide6.QtCore      import Qt

from G11_convertor_data  import AmountToString

from L00_months          import MONTHS_SHORT
from L20_PySide6         import C20_StandardItem, ROLE_IDO
from L50_form_finactions import C50_FormFinactions
from L90_finactions      import C90_FinactionsRecord


class C60_FormFinactions(C50_FormFinactions):
	""" Форма Финдействия: Механика данных """

	# Модель данных
	def InitModel(self):
		""" Инициализация модели """
		self.model_data.removeAll()
		self.model_data.setHorizontalHeaderLabels(["Дата/Сумма", "Счёт", "Метки", "Примечание"])

	def LoadDd(self):
		""" Загрузка дня """
		if not self._dd_processing: return

		dm      : str                     = MONTHS_SHORT[self.workspace.Dm()]
		dd_name : str                     = f"{self._dd_processing:02d} {dm}"

		item_dd : C20_StandardItem | None = self.model_data.itemByData(dd_name, Qt.ItemDataRole.DisplayRole)

		if item_dd is not None: return

		item_dd                           = C20_StandardItem(dd_name)
		item_parent                       = self.model_data.invisibleRootItem()

		item_parent.appendRow([item_dd, C20_StandardItem(""), C20_StandardItem(""), C20_StandardItem("")])

	def LoadRecordFinactions(self):
		""" Загрузка записи финдействий """
		if not self._ido_processing: return

		record                                = C90_FinactionsRecord(self._ido_processing)

		dm          : str                     = MONTHS_SHORT[self.workspace.Dm()]
		dd_name     : str                     = f"{record.Dd():02d} {dm}"
		item_dd     : C20_StandardItem | None = self.model_data.itemByData(dd_name, Qt.ItemDataRole.DisplayRole)
		item_amount : C20_StandardItem | None = self.model_data.itemByData(self._ido_processing, ROLE_IDO)

		if     item_dd is None     : return

		if item_amount is None:
			item_amount     = C20_StandardItem(AmountToString(record.Amount(), flag_point=False, flag_sign=True), self._ido_processing, ROLE_IDO, flag_align_right=True)
			item_finstruct  = C20_StandardItem("")
			item_labels     = C20_StandardItem("")
			item_note       = C20_StandardItem("")

			item_dd.appendRow([item_amount, item_finstruct, item_labels, item_note])
		else:
			index_row : int = item_amount.row()
			item_finstruct  = item_dd.child(index_row, 1)
			item_labels     = item_dd.child(index_row, 2)
			item_note       = item_dd.child(index_row, 3)

		item_finstruct.setText('\n'.join(record.FinstructIdos()))
		item_labels.setText(' '.join(record.Labels()))
		item_note.setText(record.Note())

# ФОРМА ФИНДЕЙСТВИЯ: МЕХАНИКА ДАННЫХ

from PySide6.QtCore      import Qt, QModelIndex

from G11_convertor_data  import AmountToString

from L00_months          import MONTHS_SHORT
from L20_PySide6         import C20_StandardItem, ROLE_IDO
from L50_form_finactions import C50_FormFinactions
from L90_finactions      import C90_FinactionsRecord


class C60_FormFinactions(C50_FormFinactions):
	""" Форма Финдействия: Механика данных """

	# Параметры
	def ReadProcessingDd(self):
		""" Чтение дня месяца """
		self._processing_dd = 0

		current_index  : QModelIndex = self.tree_data.currentIndex()
		if not current_index.isValid(): return

		current_row    : int         = current_index.row()
		parent_index   : QModelIndex = current_index.parent()
		if not parent_index.isValid(): parent_index = QModelIndex()

		current_index                = self.model_data.index(current_row, 0, parent_index)
		parent_index                 = current_index.parent()

		parent_name    : str         = parent_index.data(Qt.ItemDataRole.DisplayRole)
		current_name   : str         = current_index.data(Qt.ItemDataRole.DisplayRole)

		dd_name        : str         = parent_name if parent_index.isValid() else current_name

		try   :
			items : list[str] = dd_name.split(' ')
			self._processing_dd = int(items[0])
		except: pass

	def ReadProcessingIdo(self):
		""" Чтение IDO из модели данных """
		current_index  : QModelIndex = self.tree_data.currentIndex()
		if not current_index.isValid(): return

		current_row    : int         = current_index.row()
		parent_index   : QModelIndex = current_index.parent()
		if not parent_index.isValid(): parent_index = QModelIndex()

		current_index                = self.model_data.index(current_row, 0, parent_index)

		self._processing_ido = current_index.data(ROLE_IDO)

	def ReadProcessingIdoFromWorkspace(self):
		""" Чтение IDO из рабочего пространства """
		self._processing_ido = self.workspace.IdoFinactionsRecord()

	# Модель данных
	def InitModel(self):
		""" Инициализация модели """
		self.model_data.removeAll()
		self.model_data.setHorizontalHeaderLabels(["Дата/Сумма", "Счёт", "Метки", "Примечание"])

	def LoadDd(self):
		""" Загрузка дня """
		if not self._processing_dd: return

		dm      : str                     = MONTHS_SHORT[self.workspace.Dm()]
		dd_name : str                     = f"{self._processing_dd:02d} {dm}"

		item_dd : C20_StandardItem | None = self.model_data.itemByData(dd_name, Qt.ItemDataRole.DisplayRole)

		if item_dd is not None: return

		item_dd                           = C20_StandardItem(dd_name)
		item_parent                       = self.model_data.invisibleRootItem()

		item_parent.appendRow([item_dd, C20_StandardItem(""), C20_StandardItem(""), C20_StandardItem("")])

	def LoadRecordFinactions(self):
		""" Загрузка записи финдействий """
		if not self._processing_ido: return

		record                                = C90_FinactionsRecord(self._processing_ido)

		dm          : str                     = MONTHS_SHORT[self.workspace.Dm()]
		dd_name     : str                     = f"{record.Dd():02d} {dm}"
		item_dd     : C20_StandardItem | None = self.model_data.itemByData(dd_name, Qt.ItemDataRole.DisplayRole)
		item_amount : C20_StandardItem | None = self.model_data.itemByData(self._processing_ido, ROLE_IDO)

		if     item_dd is None     : return

		if item_amount is None:
			item_amount     = C20_StandardItem(AmountToString(record.Amount(), flag_point=False, flag_sign=True), self._processing_ido, ROLE_IDO, flag_align_right=True)
			item_finstruct  = C20_StandardItem("")
			item_labels     = C20_StandardItem("")
			item_note       = C20_StandardItem("")

			item_dd.appendRow([item_amount, item_finstruct, item_labels, item_note])
		else:
			index_row : int = item_amount.row()
			item_finstruct  = item_dd.child(index_row, 1)
			item_labels     = item_dd.child(index_row, 2)
			item_note       = item_dd.child(index_row, 3)

		item_finstruct.setText('\n'.join(self.finstruct.IdosToNames(record.FinstructIdos())))
		item_labels.setText(', '.join(record.Labels()))
		item_note.setText(record.Note())

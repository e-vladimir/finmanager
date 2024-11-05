# ФОРМА СЧЕТА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore     import QModelIndex, Qt

from G11_convertor_data import AmountToString

from L20_PySide6        import ROLES, C20_StandardItem
from L50_form_accounts  import C50_FormAccounts
from L90_accounts       import C90_Account


class C60_FormAccounts(C50_FormAccounts):
	""" Форма Счета: Механика данных """

	# Параметры
	def ReadProcessingGroupFromAccount(self):
		""" Чтение названия группы счетов из счёта """
		account = C90_Account(self._processing_ido)

		self._processing_group = account.Group()

	def ReadProcessingIdoFromTreeData(self):
		""" Чтение IDO выбранного счёта """
		current_index  : QModelIndex = self.tree_data.currentIndex()
		current_parent : QModelIndex = current_index.parent()
		index_row      : int         = current_index.row()
		current_index                = self.model_data.index(index_row, 0, current_parent)

		self._processing_ido = current_index.data(ROLES.IDO)

	def ReadProcessingNameFromTreeData(self):
		""" Чтение название выбранного счёта """
		self._processing_name = ""

		current_index  : QModelIndex             = self.tree_data.currentIndex()
		current_parent : QModelIndex             = current_index.parent()
		index_row      : int                     = current_index.row()
		current_index                            = self.model_data.index(index_row, 0, current_parent)
		current_item   : C20_StandardItem | None = self.model_data.itemFromIndex(current_index)

		if current_item   is None: return

		current_parent : C20_StandardItem        = current_item.parent()
		if current_parent is None: return

		self._processing_name = current_item.data(ROLES.TEXT)

	def ReadProcessingGroupFromTreeData(self):
		""" Чтение названия выбранной группы счетов """
		self._processing_group = ""

		current_index : QModelIndex             = self.tree_data.currentIndex()
		current_item  : C20_StandardItem | None = self.model_data.itemFromIndex(current_index)

		if current_item   is None: return

		current_parent = current_item.parent()
		if current_parent is None: self._processing_group = current_item.data(ROLES.TEXT)
		else                     : self._processing_group = current_parent.data(ROLES.TEXT)

	# Модель данных
	def InitModelData(self):
		""" Инициализация модели данных """
		self.model_data.removeAll()
		self.model_data.setHorizontalHeaderLabels(["Группа счетов\nСчёт", "Баланс\nначальный"])

		self.model_data.horizontalHeaderItem(1).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

	def LoadAccountsGroup(self):
		""" Загрузка группы счетов в модель """
		if not self._processing_group : return

		index_group : QModelIndex | None = self.model_data.indexByData(self._processing_group, ROLES.TEXT)
		if     index_group is not None: return

		item_group = C20_StandardItem(self._processing_group)
		item_root  = self.model_data.invisibleRootItem()

		item_root.appendRow([item_group, C20_StandardItem("")])

	def LoadAccount(self):
		""" Загрузка счёта в модель """
		if not self._processing_ido: return

		account                            = C90_Account(self._processing_ido)

		index_group   : QModelIndex | None = self.model_data.indexByData(account.Group(), ROLES.TEXT)
		if index_group is None: return

		item_group    : C20_StandardItem   = self.model_data.itemFromIndex(index_group)

		if not self.model_data.checkIdo(self._processing_ido):
			item_account         = C20_StandardItem(account.Name(), self._processing_ido, ROLES.IDO)
			item_balance_initial = C20_StandardItem("0", flag_align_right=True)
			item_group.appendRow([item_account, item_balance_initial])

		indexes               : list[QModelIndex] = self.model_data.indexesInRowByIdo(self._processing_ido)
		index_account         : QModelIndex       = indexes[0]
		index_balance_initial : QModelIndex       = indexes[1]

		item_account          : C20_StandardItem  = self.model_data.itemFromIndex(index_account)
		item_account.setText(account.Name())

		item_balance_initial  : C20_StandardItem  = self.model_data.itemFromIndex(index_balance_initial)
		item_balance_initial.setText(AmountToString(account.BalanceInitial()))

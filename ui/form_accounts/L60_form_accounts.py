# ФОРМА СЧЕТА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore    import QModelIndex

from L20_PySide6       import ROLES, C20_StandardItem
from L50_form_accounts import C50_FormAccounts
from L90_accounts      import C90_Account


class C60_FormAccounts(C50_FormAccounts):
	""" Форма Счета: Механика данных """

	# Параметры
	def ReadProcessingGroupFromAccount(self):
		""" Чтение названия группы счетов из счёта """
		account = C90_Account(self._processing_ido)

		self._processing_group = account.Group()

	def ReadProcessingIdoFromTreeData(self):
		""" Чтение IDO выбранного счёта """
		current_index : QModelIndex = self.tree_data.currentIndex()

		self._processing_ido = current_index.data(ROLES.IDO)

	def ReadProcessingNameFromTreeData(self):
		""" Чтение название выбранного счёта """
		self._processing_name = ""

		current_index : QModelIndex             = self.tree_data.currentIndex()
		current_item  : C20_StandardItem | None = self.model_data.itemFromIndex(current_index)

		if current_item   is None: return

		current_parent = current_item.parent()
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
		self.model_data.setHorizontalHeaderLabels(["Группа счетов\nСчёт"])

	def LoadAccountsGroup(self):
		""" Загрузка группы счетов в модель """
		if not self._processing_group : return

		index_group : QModelIndex | None = self.model_data.indexByData(self._processing_group, ROLES.TEXT)
		if     index_group is not None: return

		item_group = C20_StandardItem(self._processing_group)
		item_root  = self.model_data.invisibleRootItem()

		item_root.appendRow(item_group)

	def LoadAccount(self):
		""" Загрузка счёта в модель """
		if not self._processing_ido: return

		account                            = C90_Account(self._processing_ido)

		index_group   : QModelIndex | None = self.model_data.indexByData(account.Group(), ROLES.TEXT)
		if index_group is None: return

		item_group    : C20_StandardItem   = self.model_data.itemFromIndex(index_group)

		if not self.model_data.checkIdo(self._processing_ido):
			item_account = C20_StandardItem(account.Name(), self._processing_ido, ROLES.IDO)
			item_group.appendRow(item_account)

			return

		indexes       : list[QModelIndex] = self.model_data.indexesInRowByIdo(self._processing_ido)
		index_account : QModelIndex       = indexes[0]

		item_account  : C20_StandardItem  = self.model_data.itemFromIndex(index_account)

		item_account.setText(account.Name())

# ФОРМА СЧЕТА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore    import QModelIndex

from L20_PySide6 import ROLES, C20_StandardItem
from L50_form_accounts import C50_FormAccounts
from L90_accounts      import C90_Account


class C60_FormAccounts(C50_FormAccounts):
	""" Форма Счета: Механика данных """

	# Параметры
	def ReadProcessingGroupFromAccount(self):
		""" Чтение названия группы счетов из счёта """
		account = C90_Account(self._processing_ido)
		self._processing_group = account.Group()

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

		index_group : QModelIndex | None = self.model_data.indexByData(self._processing_group, ROLES.TEXT)
		if     index_group is None : return

		item_group  : C20_StandardItem   = self.model_data.itemFromIndex(index_group)

		account                          = C90_Account(self._processing_ido)

		item_account                     = C20_StandardItem(account.Name(), self._processing_ido, ROLES.IDO)
		item_group.appendRow(item_account)

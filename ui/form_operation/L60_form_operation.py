# ФОРМА ФИНАНСОВАЯ ОПЕРАЦИЯ: МЕХАНИКА ДАННЫХ

from PySide6.QtCore     import QModelIndex

from G11_convertor_data import AmountToString

from L20_PySide6        import C20_StandardItem, ROLES
from L50_form_operation import C50_FormOperation


class C60_FormOperation(C50_FormOperation):
	""" Форма Финансовая операция: Механика данных """

	# Параметры
	def ReadOperationFromWorkspace(self):
		""" Загрузка операции """
		self.operation.Ido(self.workspace.IdoOperation())

	def ReadProcessingIdoFromTreeData(self):
		""" Чтение IDO из дерева данных """
		current_index  : QModelIndex = self.tree_data.currentIndex()
		current_parent : QModelIndex = current_index.parent()
		index_row      : int         = current_index.row()
		current_index                = self.model_data.index(index_row, 0, current_parent)

		self._processing_ido = current_index.data(ROLES.IDO)

	# Модель данных
	def InitModel(self):
		""" Инициализация модели данных """
		self.model_data.removeAll()

		idp_dd              = self.operation.f_dd.Idp().data
		idp_amount          = self.operation.f_amount.Idp().data
		idp_description     = self.operation.f_description.Idp().data
		idp_src_amount      = self.operation.f_src_amount.Idp().data
		idp_src_description = self.operation.f_src_description.Idp().data
		idp_accounts        = self.operation.f_accounts_idos.Idp().data
		idp_labels          = self.operation.f_labels.Idp().data

		item_group          = C20_StandardItem("ОПЕРАЦИЯ")
		item_date           = C20_StandardItem("Дата",     idp_dd,          ROLES.IDO)
		item_amount         = C20_StandardItem("Сумма",    idp_amount,      ROLES.IDO)
		item_description    = C20_StandardItem("Описание", idp_description, ROLES.IDO)

		self.model_data.appendRow([item_group, C20_StandardItem("")])
		item_group.appendRow([item_date,        C20_StandardItem("")])
		item_group.appendRow([item_amount,      C20_StandardItem("")])
		item_group.appendRow([item_description, C20_StandardItem("")])

		item_group       = C20_StandardItem("ИНФОРМАЦИЯ")
		item_amount      = C20_StandardItem("Исходная сумма",    idp_src_amount,      ROLES.IDO)
		item_description = C20_StandardItem("Исходное описание", idp_src_description, ROLES.IDO)

		self.model_data.appendRow([item_group, C20_StandardItem("")])
		item_group.appendRow([item_amount,      C20_StandardItem("")])
		item_group.appendRow([item_description, C20_StandardItem("")])

		item_group       = C20_StandardItem("УЧЁТ")
		item_accounts    = C20_StandardItem("Счета", idp_accounts, ROLES.IDO)

		self.model_data.appendRow([item_group, C20_StandardItem("")])
		item_group.appendRow([item_accounts, C20_StandardItem("")])

		item_group       = C20_StandardItem("АНАЛИТИКА")
		item_labels      = C20_StandardItem("Метки", idp_labels,   ROLES.IDO)

		self.model_data.appendRow([item_group, C20_StandardItem("")])
		item_group.appendRow([item_labels,   C20_StandardItem("")])

	def LoadOperation(self):
		""" Загрузка данных финансовой операции """
		idp_dd              = self.operation.f_dd.Idp().data
		idp_amount          = self.operation.f_amount.Idp().data
		idp_description     = self.operation.f_description.Idp().data
		idp_src_amount      = self.operation.f_src_amount.Idp().data
		idp_src_description = self.operation.f_src_description.Idp().data
		idp_accounts        = self.operation.f_accounts_idos.Idp().data
		idp_labels          = self.operation.f_labels.Idp().data

		row                 = self.model_data.indexesInRowByIdo(idp_dd)
		item                = self.model_data.itemFromIndex(row[1])
		item.setText(self.operation.DdDmDyToString())

		row                 = self.model_data.indexesInRowByIdo(idp_amount)
		item                = self.model_data.itemFromIndex(row[1])
		item.setText(AmountToString(self.operation.Amount(), flag_sign=True))

		row                 = self.model_data.indexesInRowByIdo(idp_description)
		item                = self.model_data.itemFromIndex(row[1])
		item.setText(self.operation.Description())

		row                 = self.model_data.indexesInRowByIdo(idp_src_amount)
		item                = self.model_data.itemFromIndex(row[1])
		item.setText(AmountToString(self.operation.SrcAmount(), flag_sign=True))

		row                 = self.model_data.indexesInRowByIdo(idp_src_description)
		item                = self.model_data.itemFromIndex(row[1])
		item.setText(self.operation.SrcDescription())

		row                 = self.model_data.indexesInRowByIdo(idp_accounts)
		item                = self.model_data.itemFromIndex(row[1])
		item.setText('\n'.join(self.accounts.IdosToNames(self.operation.AccountsIdos())))

		row                 = self.model_data.indexesInRowByIdo(idp_labels)
		item                = self.model_data.itemFromIndex(row[1])
		item.setText('\n'.join(self.operation.Labels()))

# ФОРМА ФИНАНСОВЫЕ ОПЕРАЦИИ: МЕХАНИКА ДАННЫХ
from PySide6.QtCore import Qt

from G11_convertor_data import AmountToString
from L20_PySide6         import ROLES, C20_StandardItem
from L50_form_operations import C50_FormOperations
from L90_operations import C90_Operation


class C60_FormOperations(C50_FormOperations):
	""" Форма Финансовые операции: Механика данных """

	# Модель данных
	def InitModel(self):
		""" Инициализация модели """
		self.model_data.removeAll()
		self.model_data.setHorizontalHeaderLabels(["Дата/Сумма", "Счёт учёта", "Метки", "Описание"])

	def LoadDd(self):
		""" Загрузка дня в модель """
		if self._processing_dd < 1                                     : return

		dd_name : str                    = f"{self._processing_dd:02d} {self.workspace.DmDyToString()}"

		if self.model_data.indexByData(dd_name, ROLES.TEXT) is not None: return

		row     : list[C20_StandardItem] = [C20_StandardItem("") for _ in range(self.model_data.columnCount())]

		item_dd_name                     = row[0]
		item_dd_name.setText(dd_name)

		parent_item                      = self.model_data.invisibleRootItem()
		parent_item.appendRow(row)

	def LoadOperation(self):
		""" Загрузка операции в модель """
		if not self._processing_ido : return

		operation                         = C90_Operation(self._processing_ido)
		dd                                = operation.Dd()
		dd_name : str                     = f"{dd:02d} {self.workspace.DmDyToString()}"

		item_dd : C20_StandardItem | None = self.model_data.itemByData(dd_name, ROLES.TEXT)
		if     item_dd is None      : return

		if not self.model_data.checkIdo(self._processing_ido):
			row: list[C20_StandardItem] = [C20_StandardItem("") for _ in range(self.model_data.columnCount())]

			item_amount                 = row[0]
			item_amount.setData(self._processing_ido, ROLES.IDO)
			item_amount.setText(AmountToString(operation.Amount(), flag_sign=True))

			item_dd.appendRow(row)

		indexes                           = self.model_data.indexesInRowByIdo(self._processing_ido)

		item_amount                       = self.model_data.itemFromIndex(indexes[0])
		item_amount.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

		item_accounts                     = self.model_data.itemFromIndex(indexes[1])
		item_accounts.setText('\n'.join(self.accounts.IdosToNames(operation.AccountsIdos())))

		item_labels                       = self.model_data.itemFromIndex(indexes[2])
		item_labels.setText(', '.join(operation.Labels()))

		item_description                  = self.model_data.itemFromIndex(indexes[3])
		item_description.setText(operation.Description())

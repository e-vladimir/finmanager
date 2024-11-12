# ФОРМА ФИНАНСОВЫЕ ОПЕРАЦИИ: МЕХАНИКА ДАННЫХ

from PySide6.QtCore      import Qt, QModelIndex
from PySide6.QtGui       import QColor

from G11_convertor_data  import AmountToString

from L00_colors          import COLORS
from L20_PySide6         import ROLES, C20_StandardItem
from L50_form_operations import C50_FormOperations
from L90_operations      import C90_Operation


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
		item_dd_name.setData(self._processing_dd, ROLES.GROUP)
		item_dd_name.setData(self._processing_dd, ROLES.SORT_INDEX)
		item_dd_name.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

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
			item_amount.setData(self._processing_dd,  ROLES.GROUP)
			item_amount.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

			item_dd.appendRow(row)

		indexes                           = self.model_data.indexesInRowByIdo(self._processing_ido)

		item_amount                       = self.model_data.itemFromIndex(indexes[0])
		item_amount.setText(AmountToString(operation.Amount(), flag_sign=True))
		item_amount.setData(operation.Amount(), ROLES.SORT_INDEX)

		item_accounts                     = self.model_data.itemFromIndex(indexes[1])
		item_accounts.setText(', '.join(self.accounts.IdosToNames(operation.AccountsIdos())))

		item_labels                       = self.model_data.itemFromIndex(indexes[2])
		item_labels.setText(', '.join(operation.Labels()))

		item_description                  = self.model_data.itemFromIndex(indexes[3])
		item_description.setText(operation.Description())

		text_color                        = QColor(0, 0, 0)

		match operation.Color():
			case COLORS.BLACK: text_color = QColor(  0,   0,   0)
			case COLORS.BLUE : text_color = QColor(  0,   0, 200)
			case COLORS.GRAY : text_color = QColor(120, 120, 120)
			case COLORS.GREEN: text_color = QColor(  0, 200,   0)
			case COLORS.RED  : text_color = QColor(200,   0,   0)

		self.model_data.setRowColor(item_dd, item_amount.row(), color_fg=text_color)

	def CleanOperation(self):
		""" Зачистка операции """
		if not self._processing_ido   : return

		index_operation : QModelIndex | None = self.model_data.indexByData(self._processing_ido, ROLES.IDO)
		if     index_operation is None: return

		index_dd        : QModelIndex        = index_operation.parent()
		operation                            = C90_Operation(self._processing_ido)
		if operation.Dd() == index_dd.data(ROLES.GROUP): return

		self.model_data.removeRow(index_operation.row(), index_dd)

	def CleanDd(self):
		""" Зачистка дня """
		index_dd     : QModelIndex | None = self.model_data.indexByData(self._processing_dd, ROLES.GROUP)
		if index_dd is None                  : return

		if self.model_data.rowCount(index_dd): return

		index_parent : QModelIndex        = index_dd.parent()

		self.model_data.removeRow(index_dd.row(), index_parent)

	# Параметры
	def ReadProcessingIdoFromTreeData(self):
		""" Чтение текущего IDO из дерева данных """
		current_index  : QModelIndex = self.tree_data.currentIndex()
		current_parent : QModelIndex = current_index.parent()
		index_row      : int         = current_index.row()
		current_index                = self.model_data.index(index_row, 0, current_parent)

		self._processing_ido = current_index.data(ROLES.IDO)

	def ReadProcessingDdFromTreeData(self):
		""" Чтение текущего дня из дерева данных """
		current_index  : QModelIndex = self.tree_data.currentIndex()
		current_parent : QModelIndex = current_index.parent()
		index_row      : int         = current_index.row()
		current_index                = self.model_data.index(index_row, 0, current_parent)

		self._processing_dd = current_index.data(ROLES.GROUP)
		if self._processing_dd is None: self._processing_dd = 1

	def ReadProcessingColumnFromTreeData(self):
		""" Чтение текущей колонки из дерева данных """
		current_index : QModelIndex = self.tree_data.currentIndex()
		self._processing_column = current_index.column()

# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МЕХАНИКА ДАННЫХ

from PySide6.QtCore    import QModelIndex, Qt
from PySide6.QtWidgets import QListWidgetItem

from L00_rules         import RULES
from L20_PySide6       import ROLES, C20_StandardItem
from L50_form_rules    import C50_FormRules
from L90_rules         import C90_ProcessingRulesRecord


class C60_FormRules(C50_FormRules):
	""" Форма Правила обработки данных: Механика данных """

	# Параметры
	def ReadProcessingType(self):
		""" Чтение типа правил """
		self._processing_type = None

		current_item : QListWidgetItem | None = self.list_types.currentItem()
		if current_item is None: return

		self._processing_type = RULES(current_item.text())

	def ReadProcessingIdo(self):
		""" Чтение IDO выбранной записи """
		self._processing_ido = ""

		current_index : QModelIndex = self.table_data.currentIndex()
		if not current_index.isValid(): return

		row           : int         = current_index.row()

		index_root                  = QModelIndex()
		index_item                  = self.model_data.index(row, 0, index_root)

		self._processing_ido = index_item.data(ROLES.ROLE_IDO)

	def ReadProcessingName(self):
		""" Чтение наименования выбранной записи """
		self._processing_name = ""

		current_index : QModelIndex = self.table_data.currentIndex()
		if not current_index.isValid(): return

		row           : int         = current_index.row()

		index_column  : int         = 0

		match self._processing_type:
			case RULES.REPLACE_TEXT : index_column = 1

		index_root                  = QModelIndex()
		index_item                  = self.model_data.index(row, index_column, index_root)

		self._processing_name = index_item.data(Qt.ItemDataRole.DisplayRole)
		self._processing_name = self._processing_name.replace('\n', ', ')
		self._processing_name = self._processing_name[:50]

	def ReadProcessingColumn(self):
		""" Чтение колонки """
		current_index : QModelIndex = self.table_data.currentIndex()

		self._processing_column = current_index.column()

	# Модель данных
	def InitModelData(self):
		""" Инициализация модели данных """
		self.model_data.removeAll()

		match self._processing_type:
			case RULES.REPLACE_TEXT: self.model_data.setHorizontalHeaderLabels(["Фрагмент поиска", "Фрагмент замены"])

	def LoadRulesRecord(self):
		""" Загрузка правила обработки данных """
		if not self._processing_ido: return

		record                               = C90_ProcessingRulesRecord(self._processing_ido)

		item_parent = self.model_data.invisibleRootItem()
		item_input : C20_StandardItem | None = self.model_data.itemByData(self._processing_ido, ROLES.ROLE_IDO)

		if item_input is None:
			item_input  = C20_StandardItem("", self._processing_ido, ROLES.ROLE_IDO)
			item_output = C20_StandardItem("")

			item_parent.appendRow([item_input, item_output])

		row        : int                     = item_input.row()
		item_output                          = item_parent.child(row, 1)

		item_input.setText('\n'.join(record.OptionsInputAsStrings()))
		item_output.setText('\n'.join(record.OptionsOutputAsStrings()))

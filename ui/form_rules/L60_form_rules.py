# ФОРМА ПРАВИЛ ОБРАБОТКИ: МЕХАНИКА ДАННЫХ

from PySide6.QtCore import QModelIndex, Qt
from PySide6.QtGui        import QStandardItem

from L00_roles            import *
from L00_rules_types      import *

from L20_PySide6          import C20_StandardItem
from L50_form_rules       import C50_FormRules
from L90_findescription   import C90_RecordFindescription
from L90_processing_rules import C90_RecordProcessingRules


class C60_FormRules(C50_FormRules):
	""" Форма правил обработки: Механика данных """

	# Параметры
	def ReadTypeProcessing(self):
		""" Чтение типа обработки """
		self._type_processing = self.cbbox_rules_types.currentText()

	def ReadIdoProcessing(self):
		""" Чтение OID записи правил """
		self._ido_processing = ""

		index_record : QModelIndex = self.tree_data.currentIndex()
		if not index_record.isValid(): return

		self._ido_processing = index_record.data(ROLE_OID_RULES)

	def ReadColumnProcessing(self):
		""" Чтение колонки """
		self._column_processing = -1

		index_record : QModelIndex = self.tree_data.currentIndex()
		if not index_record.isValid(): return

		self._column_processing = index_record.column()

	def ReadNameProcessing(self):
		""" Чтение наименования """
		self._name_processing = ""

		index_record : QModelIndex = self.tree_data.currentIndex()
		if not index_record.isValid(): return

		index_parent : QModelIndex = index_record.parent()

		index_row    : int         = index_record.row()
		index_name   : QModelIndex = self.model_data.index(index_row, 0, index_parent)

		self._name_processing = index_name.data(Qt.DisplayRole)

	# Модель данных
	def SetupModelData(self):
		""" Настройка модели данных """
		self.model_data.removeAll()

		if   self._type_processing == RULE_REPLACE_TEXT                 : self.model_data.setHorizontalHeaderLabels(["Фрагмент поиска", "Фрагмент замены"])
		elif self._type_processing == RULE_DETECT_FINDESCRIPTION_BY_TEXT: self.model_data.setHorizontalHeaderLabels(["Финсостав",       "Фрагмент поиска"])

	# Запись замены текстовых фрагментов
	def LoadRecordReplaceText(self):
		""" Загрузка записи правил замены текстовых фрагментов """
		if not self._ido_processing: return

		record_rule_processing       = C90_RecordProcessingRules(self._ido_processing)

		item_parent  : QStandardItem = self.model_data.invisibleRootItem()
		index_record : QModelIndex   = self.model_data.indexByData(self._ido_processing, ROLE_OID_RULES)

		index_row    : int           = self.model_data.rowCount() if index_record is None else index_record.row()

		labels : list[str] = [""] * 2
		labels[0]          = '\n'.join(record_rule_processing.OptionsInputAsStrings())
		labels[1]          = record_rule_processing.OptionsOutputAsString()

		for index_col, label in enumerate(labels):
			item_data = C20_StandardItem(label, self._ido_processing, ROLE_OID_RULES)

			item_parent.setChild(index_row, index_col, item_data)

	# Запись определения финсостава по текстовым фрагментам
	def LoadRecordDetectFindescriptionByText(self):
		""" Загрузка записи правил определения финсостава по текстовому фрагменту """
		if not self._ido_processing: return

		record_rule                       = C90_RecordProcessingRules(self._ido_processing)
		record_findescription             = C90_RecordFindescription(record_rule.OptionsOutputAsString())

		index_findescription : QModelIndex | None = self.model_data.indexByData(record_findescription.Ido().data, ROLE_OID_FINDESCRIPTION)
		if index_findescription is None: return

		index_parent : QModelIndex | None = index_findescription.parent()

		index_row    : int                = index_findescription.row()

		item_parent  : QStandardItem      = self.model_data.invisibleRootItem() if not index_parent.isValid() else self.model_data.itemFromIndex(index_parent)

		labels      : list[str]           = [""] * 2
		labels[0]                         = record_findescription.Name()
		labels[1]                         = ', '.join(record_rule.OptionsInputAsStrings())

		for index_col, label in enumerate(labels):
			if   index_col == 0:
				item_data : QStandardItem = item_parent.child(index_row, 0)
				item_data.setData(record_rule.Ido().data,            ROLE_OID_RULES)

			elif index_col == 1:
				item_data = C20_StandardItem(label)
				item_data.setData(record_findescription.Ido().data, ROLE_OID_FINDESCRIPTION)
				item_data.setData(record_rule.Ido().data,            ROLE_OID_RULES)
				item_parent.setChild(index_row, index_col, item_data)

	# Запись финструктуры
	def LoadRecordFindescription(self):
		""" Загрузка записи финсостава """
		if not self._ido_processing: return

		record_findescription             = C90_RecordFindescription(self._ido_processing)

		index_record : QModelIndex | None = self.model_data.indexByData(record_findescription.Ido().data, ROLE_OID_FINDESCRIPTION)
		index_parent : QModelIndex | None = self.model_data.indexByData(record_findescription.ParentIdo(), ROLE_OID_FINDESCRIPTION)

		item_parent : QStandardItem       = self.model_data.invisibleRootItem() if index_parent is None else self.model_data.itemFromIndex(index_parent)
		index_row   : int                 = item_parent.rowCount()              if index_record is None else index_record.row()

		labels      : list[str]           = [""] * 2
		labels[0]                         = record_findescription.Name()

		for index_col, label in enumerate(labels):
			item_data = C20_StandardItem(label)
			item_data.setData(record_findescription.Ido().data, ROLE_OID_FINDESCRIPTION)

			item_parent.setChild(index_row, index_col, item_data)

		for self._ido_processing in record_findescription.SubIdos(): self.LoadRecordFindescription()

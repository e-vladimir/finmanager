# ФОРМА ФИНСОСТАВА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore          import Qt, QModelIndex
from PySide6.QtGui           import QStandardItem
from PySide6.QtWidgets       import QListWidgetItem

from L00_containers          import CONTAINER_LOCAL
from L00_findescription      import FINDESCRIPTION_CATEGORIES

from L20_PySide6             import FindItemFromStandardModelByData, ItemsFromStandardModel, ROLE_OID
from L50_form_findescription import C50_FormFindescription
from L90_findescription      import C90_RecordFindescription


class C60_FormFindescription(C50_FormFindescription):
	""" Форма Финсостав: Механика данных """

	# Модель данных
	def SetupModel(self):
		""" Сброс модели """
		self.model_findescription.removeRows(0, self.model_findescription.rowCount())

	def ItemByOid(self, oid: str) -> QStandardItem | None:
		""" Поиск StandardItem по OID """
		return FindItemFromStandardModelByData(self.model_findescription, oid, ROLE_OID)

	def LoadRecordFindescription(self):
		""" Загрузка записи финсостава """
		if not self._oid_processing: return

		self._flag_loading = True

		record_findescription              = C90_RecordFindescription(self._oid_processing)
		record_item : QStandardItem | None = self.ItemByOid(self._oid_processing)

		if record_item is None:
			record_item                        = QStandardItem()

			parent_oid  : str                  = record_findescription.ParentOid()
			parent_item : QStandardItem | None = self.ItemByOid(parent_oid)

			if parent_item is None: parent_item = self.model_findescription.invisibleRootItem()

			parent_item.appendRow(record_item)

		record_item.setText(record_findescription.Name())
		record_item.setData(self._oid_processing, ROLE_OID)
		record_item.setCheckable(True)

		self._flag_loading = False

		for self._oid_processing in self.findescription.SubOids(self._oid_processing): self.LoadRecordFindescription()

	def SortModel(self):
		self.model_findescription.sort(0)

	def CleanModel(self):
		""" Зачистка модели от пустых записей """
		oids : list[str] = C90_RecordFindescription().Oids(CONTAINER_LOCAL).items

		for item in reversed(ItemsFromStandardModel(self.model_findescription)):
			if item.data(ROLE_OID) in oids: continue

			parent    : QStandardItem = item.parent()
			if parent is None                    : parent = self.model_findescription.invisibleRootItem()

			index_row : int           = item.row()
			parent.removeRow(index_row)

	def ProcessingIncludeRecordInCategory(self):
		""" Обработка вхождения записи в категорию финсостава """
		if not self._oid_processing: return

		record_findescription = C90_RecordFindescription(self._oid_processing)
		if self._flag_checked: record_findescription.IncludeInCategory(self._category_processing)
		else                 : record_findescription.ExcludeFromCategory(self._category_processing)

	# Дерево финсостава
	def ReadOidProcessingFromSelected(self):
		""" Считывание OID выделенной записи финсостава """
		self._item_processing = None

		index_selected : QModelIndex | None = self.tre_findescription.currentIndex()
		if index_selected is None: return

		self._item_processing = self.model_findescription.itemFromIndex(index_selected)

		self.ReadOidProcessingFromItem()

	def ReadOidProcessingFromItem(self):
		""" Считывание OID записи финсостава в обработке """
		self._oid_processing = ""

		if self._item_processing is None: return

		self._oid_processing = self._item_processing.data(ROLE_OID)

	def ReadFlagChecked(self):
		""" Чтение текущего состояния галочки элемента """
		self._flag_checked = False

		if not self._oid_processing: return

		item_record : QStandardItem | None = FindItemFromStandardModelByData(self.model_findescription, self._oid_processing, ROLE_OID)
		if     item_record is None : return

		self._flag_checked = item_record.checkState() == Qt.Checked

	def MemorySelectedOid(self):
		""" Запомнить OID записи финсостава """
		self._oid_memory = self._oid_processing

	def ShowItemsInCategory(self):
		""" Отображение значений в категории """
		self._flag_loading = True

		values : list[str] = self.findescription.Names(self._category_processing)

		for item in ItemsFromStandardModel(self.model_findescription):
			flag_in_category : bool = item.text() in values

			item.setCheckState(Qt.Checked if flag_in_category else Qt.Unchecked)

		self._flag_loading = False

	# Категории финсостава
	def FillCategories(self):
		""" Заполнение списка категорий финсостава """
		self.lst_categories.clear()

		self.lst_categories.addItems(FINDESCRIPTION_CATEGORIES)

	def ReadCategoryProcessing(self):
		""" Чтение текущей категории финсостава """
		self._category_processing = ""

		item_category : QListWidgetItem = self.lst_categories.currentItem()
		if item_category is None: return

		self._category_processing = item_category.text()

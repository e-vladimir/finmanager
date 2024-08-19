# ФОРМА ФИНСОСТАВА: ЛОГИКА УПРАВЛЕНИЯ

from PySide6.QtGui           import QStandardItem

from L80_form_findescription import C80_FormFindescription


class C90_FormFindescription(C80_FormFindescription):
	""" Форма Финсостав: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Модель финсостава
		self.model_findescription.itemChanged.connect(self.on_ItemChanged)

		# Дерево финсостава
		self.tre_findescription.customContextMenuRequested.connect(self.on_RequestMenuFindescription)
		self.tre_findescription.doubleClicked.connect(self.on_RequestRenameRecord)

		# Меню финсостава
		self.mnu_findescription_parent_create.triggered.connect(self.on_RequestCreateRecord)
		self.mnu_findescription_parent_paste.triggered.connect(self.on_RequestPasteRecord)

		self.mnu_findescription_record_create.triggered.connect(self.on_RequestCreateSubRecord)
		self.mnu_findescription_record_rename.triggered.connect(self.on_RequestRenameRecord)
		self.mnu_findescription_record_delete.triggered.connect(self.on_RequestDeleteRecord)
		self.mnu_findescription_record_paste.triggered.connect(self.on_RequestSubPasteRecord)

		self.mnu_findescription_move_memory.triggered.connect(self.on_RequestMemoryRecord)
		self.mnu_findescription_move_up.triggered.connect(self.on_RequestMoveUp)

		# Категория финсостава
		self.lst_categories.currentItemChanged.connect(self.on_CategorySwitched)

	def on_Open(self):
		""" Открытие формы """
		self.FillCategories()
		self.SelectCurrentCategory()

		self.SetupModel()
		self.LoadFindescription()

		self.on_CategorySwitched()

		self.ShowTitle()

	def on_RequestMenuFindescription(self):
		""" Запрос отображения меню финсостава """
		self.ReadIdoProcessingFromSelected()

		self.SetupMenuFindescription()
		self.EnabledMenuFindescription()
		self.ShowMenuFindescription()

	def on_RequestCreateRecord(self):
		""" Запрос на создание записи финсостава """
		self.ReadIdoProcessingFromSelected()

		self.CreateRecord()

	def on_RequestCreateSubRecord(self):
		""" Запрос на создание вложенной записи финсостава """
		self.ReadIdoProcessingFromSelected()

		self.CreateSubRecord()

	def on_RequestRenameRecord(self):
		""" Запрос на редактирование записи финсостава """
		self.ReadIdoProcessingFromSelected()

		self.EditNameRecord()

	def on_RequestDeleteRecord(self):
		""" Запрос на удаление записи финсостава """
		self.ReadIdoProcessingFromSelected()

		self.DeleteRecord()

	def on_RecordCreated(self):
		""" Создана запись финсостава """
		self.LoadFindescription()
		self.SortModel()

	def on_SubRecordCreated(self):
		""" Создана вложенная запись финсостава """
		self.LoadRecordFindescription()
		self.SortModel()

		self.ShowParents()

	def on_RecordRenamed(self):
		""" Изменено значение записи финсостава """
		self.LoadRecordFindescription()
		self.SortModel()

	def on_RecordDeleted(self):
		""" Удалена запись финсостава """
		self.CleanModel()

		if not self._ido_processing: self.LoadFindescription()
		else                       : self.LoadRecordFindescription()

		self.ShowParents()
		self.ShowItemsInCategory()

	def on_RequestMemoryRecord(self):
		""" Запрос на запоминание записи финсостава """
		self.MemorySelectedIdo()

	def on_RequestMoveUp(self):
		""" Запрос на перемещение записи уровнем выше """
		self.MoveUpRecord()

	def on_RecordMoved(self):
		""" Запись финсостава перемещена """
		self.SetupModel()
		self.LoadFindescription()

	def on_RequestPasteRecord(self):
		""" Перенос записи в тот же уровень """
		self.PasteRecord()

	def on_RequestSubPasteRecord(self):
		""" Перенос записи как дочерний элемент """
		self.SubPasteRecord()

	def on_CategorySwitched(self):
		""" Смена категории финсостава """
		self.ReadCategoryProcessing()

		self.ShowItemsInCategory()

		self.ShowTitle()

	def on_ItemChanged(self, item: QStandardItem | None):
		""" Изменение данных элемента """
		self._item_processing = item

		self.ProcessingItemChanged()

	def on_ItemCheckStateChanged(self):
		""" Изменилось состояние галочки """
		if self._flag_loading: return

		print("Change")

		self.ReadIdoProcessingFromItem()
		self.ReadFlagChecked()
		self.ReadCategoryProcessing()
		self.ProcessingIncludeRecordInCategory()

	def on_FindescriptionLoaded(self):
		""" Финсостав загружен """
		self._flag_loading = True

		self.SortModel()
		self.ExpandTreFindescription()
		self.ShowParents()

		self._flag_loading = True

# ФОРМА ФИНСТРУКТУРЫ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_finstruct import C80_FormFinstruct


class C90_FormFinstruct(C80_FormFinstruct):
	""" Форма Финструктуры: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево финструктуры
		self.tree_data.customContextMenuRequested.connect(self.on_RequestMenuFinstruct)
		self.tree_data.doubleClicked.connect(self.on_RequestEditRecord)

		# Меню финструктуры
		self.menu_finstruct_parent_create.triggered.connect(self.on_RequestCreateRecord)
		self.menu_finstruct_parent_paste.triggered.connect(self.on_RequestPasteRecord)

		self.menu_finstruct_record_create.triggered.connect(self.on_RequestCreateSubRecord)
		self.menu_finstruct_record_rename.triggered.connect(self.on_RequestRenameRecord)
		self.menu_finstruct_record_delete.triggered.connect(self.on_RequestDeleteRecord)
		self.menu_finstruct_record_set_priority.triggered.connect(self.on_RequestSetPriorityRecord)
		self.menu_finstruct_record_paste.triggered.connect(self.on_RequestSubPasteRecord)

		self.menu_finstruct_move_memory.triggered.connect(self.on_RequestMemoryRecord)
		self.menu_finstruct_move_move_up.triggered.connect(self.on_RequestMoveUp)

		self.menu_finstruct_finperiod_next.triggered.connect(self.on_RequestCopyRecordToNextDm)
		self.menu_finstruct_finperiod_prev.triggered.connect(self.on_RequestCopyRecordToPrevDm)

	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.SetupModel()

		self.LoadFinstruct()

	def on_RecordCreated(self):
		""" Создана запись финструктуры """
		self.LoadFinstruct()

	def on_SubRecordCreated(self):
		""" Создана вложенная запись финструктуры """
		self.LoadRecordFinstruct()

		self.AdjustTreeDataColor()

	def on_RecordRenamed(self):
		""" Изменено значение записи финструктуры """
		self.LoadRecordFinstruct()

	def on_RequestMenuFinstruct(self):
		""" Запрос меню финструктуры """
		self.ReadIdoProcessing()

		self.AdjustMenuFinstructText()
		self.AdjustMenuFinstructEnable()
		self.ShowMenuFinstruct()

	def on_RequestCreateRecord(self):
		""" Запрос на создание записи финструктуры """
		self.CreateRecord()

	def on_RequestCreateSubRecord(self):
		""" Запрос на создание записи финструктуры """
		self.CreateSubRecord()

	def on_RequestRenameRecord(self):
		""" Запрос на переименование записи финструктуры """
		self.ReadIdoProcessing()
		self.EditNameRecord()

	def on_RequestDeleteRecord(self):
		""" Запрос удаления записи финструктуры """
		self.DeleteRecord()

	def on_FinstructLoaded(self):
		""" Финструктура загружена """
		self.SetupModelSort()

		self.ShowPriorityRecord()

		self.AdjustTreeDataColor()
		self.AdjustTreeDataExpand()
		self.AdjustTreeDataSize()

	def on_RecordDeleted(self):
		""" Удалена запись финсостава """
		self.CleanModel()

		if not self._oid_processing: self.LoadFinstruct()
		else                       : self.LoadRecordFinstruct()

		self.AdjustTreeDataColor()
		self.AdjustTreeDataSize()

	def on_RequestMemoryRecord(self):
		""" Запрос на запоминание записи финсостава """
		self.ReadIdoMemory()

	def on_RequestMoveUp(self):
		""" Запрос на перемещение записи уровнем выше """
		self.MoveUpRecord()

	def on_RecordMoved(self):
		""" Запись финсостава перемещена """
		self.SetupModel()
		self.LoadFinstruct()

	def on_RequestPasteRecord(self):
		""" Перенос записи в тот же уровень """
		self.PasteRecord()

	def on_RequestSubPasteRecord(self):
		""" Перенос записи как дочерний элемент """
		self.SubPasteRecord()

	def on_RequestCopyRecordToNextDm(self):
		""" Запрос на перенос записи финструктуры в следующий месяц """
		self.CopyRecordToNextDm()

	def on_RequestCopyRecordToPrevDm(self):
		""" Запрос на перенос записи финструктуры в предыдущий месяц """
		self.CopyRecordToPrevDm()

	def on_RequestEditRecord(self):
		self.ReadIdoProcessing()
		self.ReadColProcessing()

		self.RequestEditRecord()

	def on_RequestEditRemainInitial(self):
		""" Запрос на редактирование остатка начального """
		self.RequestEditRemainInitial()

	def on_RecordChanged(self):
		""" Изменилась запись """
		self.LoadFinstruct()
		self.AdjustTreeDataSize()

	def on_RequestSetPriorityRecord(self):
		""" Запрос на установку записи по умолчанию """
		self.SetPriorityRecord()

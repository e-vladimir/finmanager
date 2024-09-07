# ФОРМА ФИНСТРУКТУРА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_finstruct import C80_FormFinstruct


class C90_FormFinstruct(C80_FormFinstruct):
	""" Форма Финструктура: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных
		self.tree_data.customContextMenuRequested.connect(self.on_RequestMenuFinstruct)
		self.tree_data.doubleClicked.connect(self.on_RequestProcessingTreeDataDbClick)

		# Меню финструктуры
		self.menu_finstruct_create.triggered.connect(self.on_RequestCreateFinstructRecord)

		self.menu_finstruct_group_create.triggered.connect(self.on_RequestCreateFinstructRecordInGroup)
		self.menu_finstruct_group_rename.triggered.connect(self.on_RequestRenameGroupFinstruct)

		self.menu_finstruct_record_rename.triggered.connect(self.on_RequestRenameFinstructRecord)
		self.menu_finstruct_record_delete.triggered.connect(self.on_RequestDeleteFinstructRecord)
		self.menu_finstruct_record_regroup.triggered.connect(self.on_RequestRegroupFinstructRecord)

		self.menu_finstruct_record_edit_balance_start.triggered.connect(self.on_RequestEditBalanceStartFinstructRecord)

		self.menu_finstruct_record_copy_prev_dm.triggered.connect(self.on_RequestCopyToPrevDmFinstructRecord)
		self.menu_finstruct_record_copy_next_dm.triggered.connect(self.on_RequestCopyToNextDmFinstructRecord)

	# Форма
	def on_Show(self):
		super().on_Show()

		self.ShowTitle()

		self.InitModel()
		self.LoadFinstruct()

		self.AdjustTreeDataSize()
		self.AdjustTreeDataAlign()
		self.AdjustTreeDataSort()
		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

		self.CleanModel()

	# Меню финструктуры
	def on_RequestMenuFinstruct(self):
		""" Запрос на отображение меню финструктуры """
		self.ReadProcessingRow()
		self.ReadProcessingColumn()
		self.ReadProcessingIdo()
		self.ReadProcessingName()
		self.ReadProcessingGroup()

		self.AdjustMenuFinstructEnable()
		self.AdjustMenuFinstructText()

		self.ShowMenuFinstruct()

	# Дерево финструктуры
	def on_RequestProcessingTreeDataDbClick(self):
		""" Реакция действия на двойной клик по дереву данных """
		self.ReadProcessingRow()
		self.ReadProcessingColumn()
		self.ReadProcessingIdo()
		self.ReadProcessingName()
		self.ReadProcessingGroup()

		self.ProcessingTreeDataDbClick()

	# Запись финструктуры
	def on_RequestCreateFinstructRecord(self):
		""" Запрос на создание записи финструктуры """
		self.CreateFinstructRecord()

		self.LoadFinstruct()

		self.AdjustTreeDataSort()
		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

	def on_RequestCreateFinstructRecordInGroup(self):
		""" Запрос на создание записи финструктуры в группе """
		self.CreateFinstructRecordInGroup()

		self.LoadFinstruct()

		self.AdjustTreeDataSort()
		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

	def on_RequestRenameFinstructRecord(self):
		""" Запрос на изменение наименования записи финструктуры """
		self.RenameFinstructRecord()

		self.LoadFinstruct()

		self.AdjustTreeDataSort()
		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

	def on_RequestDeleteFinstructRecord(self):
		""" Запрос на удаление записи финструктуры """
		self.DeleteFinstructRecord()

		self.CleanModel()

	def on_RequestRegroupFinstructRecord(self):
		""" Запрос на изменение группы счета """
		self.RegroupFinstructRecord()

		self.CleanModel()
		self.LoadFinstruct()

		self.AdjustTreeDataSort()
		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

	def on_RequestRenameGroupFinstruct(self):
		""" Запрос на изменение группы счетов """
		self.RenameGroupFinstruct()

		self.CleanModel()
		self.LoadFinstruct()

		self.AdjustTreeDataSort()
		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

	def on_RequestEditBalanceStartFinstructRecord(self):
		""" Запрос на установку баланса начального  """
		self.EditBalanceStartFinstructRecord()
		self.LoadFinstructRecord()

	def on_RequestCopyToPrevDmFinstructRecord(self):
		""" Запрос на перенос записи финструктуры в прошлый месяц """
		self.CopyToPrevDmFinstructRecord()

	def on_RequestCopyToNextDmFinstructRecord(self):
		""" Запрос на перенос записи финструктуры в следующий месяц """
		self.CopyToNextDmFinstructRecord()

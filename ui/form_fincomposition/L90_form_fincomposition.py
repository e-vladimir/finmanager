# ФОРМА ФИНСОСТАВ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_fincomposition import C80_FormFincomposition


class C90_FormFincomposition(C80_FormFincomposition):
	""" Форма Финсостав: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево финсостава
		self.tree_data.customContextMenuRequested.connect(self.on_RequestShowMenuFincomposition)
		self.tree_data.doubleClicked.connect(self.on_RequestRenameFincompositionRecord)

		# Меню финсостава
		self.menu_fincomposition_create.triggered.connect(self.on_RequestAppendFincompositionRecordToTop)

		self.menu_fincomposition_record_create.triggered.connect(self.on_RequestAppendFincompositionRecord)
		self.menu_fincomposition_record_rename.triggered.connect(self.on_RequestRenameFincompositionRecord)
		self.menu_fincomposition_record_delete.triggered.connect(self.on_RequestDeleteFincompositionRecord)
		self.menu_fincomposition_record_up.triggered.connect(self.on_RequestMoveUpFincompositionRecord)
		self.menu_fincomposition_record_copy.triggered.connect(self.on_RequestMemoryFincompositionRecord)
		self.menu_fincomposition_record_paste.triggered.connect(self.on_RequestPasteFincompositionRecord)

		self.menu_fincomposition_reset_all.triggered.connect(self.on_RequestResetFincomposition)

	# Форма
	def on_Show(self):
		""" Открытие """
		self.ShowTitle()

		self.InitModelData()
		self.LoadFincomposition()

		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

	# Меню финсостава
	def on_RequestShowMenuFincomposition(self):
		""" Запрос на отображение меню финсостава """
		self.ReadProcessingIdoFromTreeData()
		self.ReadProcessingNameFromTreeData()

		self.AdjustMenuFincompositionText()
		self.AdjustMenuFincompositionEnable()

		self.ShowMenuFincomposition()

	# Запись финсостава
	def on_RequestAppendFincompositionRecordToTop(self):
		""" Запрос на добавление записи финсостава верхнего уровня """
		self.AppendFincompositionRecordToTop()

		self.LoadFincomposition()

		self.AdjustTreeDataSort()
		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

	def on_RequestAppendFincompositionRecord(self):
		""" Запрос на добавление вложенной записи финсостава """
		self.AppendFincompositionRecord()

		self.LoadFincomposition()

		self.AdjustTreeDataSort()
		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

	def on_RequestRenameFincompositionRecord(self):
		""" Запрос на изменение наименования записи финсостава """
		self.ReadProcessingIdoFromTreeData()
		self.ReadProcessingNameFromTreeData()

		self.RenameFincompositionRecord()

		self.LoadFincomposition()

		self.AdjustTreeDataSort()
		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

	def on_RequestDeleteFincompositionRecord(self):
		""" Запрос на удаление записи финсостава """
		self.DeleteFincompositionRecord()

		self.InitModelData()
		self.LoadFincomposition()

		self.AdjustTreeDataSort()
		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

	def on_RequestMoveUpFincompositionRecord(self):
		""" Запрос на перемещение записи финсостава уровнем выше """
		self.MoveUpFincompositionRecord()

		self.InitModelData()
		self.LoadFincomposition()

		self.AdjustTreeDataSort()
		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

	def on_RequestMemoryFincompositionRecord(self):
		""" Запрос на запоминание записи финсостава """
		self.MemoryProcessingName()

	def on_RequestPasteFincompositionRecord(self):
		""" Вставка записи финсостава """
		self.PasteFincompositionRecord()

		self.InitModelData()
		self.LoadFincomposition()

		self.AdjustTreeDataSort()
		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

	def on_RequestResetFincomposition(self):
		""" Запрос сброса финсостава """
		self.ResetFincomposition()

		self.InitModelData()
		self.LoadFincomposition()

		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

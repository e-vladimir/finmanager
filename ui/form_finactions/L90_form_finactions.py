# ФОРМА ФИНДЕЙСТВИЯ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_finactions import C80_FormFinactions


class C90_FormFinactions(C80_FormFinactions):
	""" Форма Финдействия: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево финдействий
		self.tree_data.customContextMenuRequested.connect(self.on_RequestMenuFinactions)
		self.tree_data.doubleClicked.connect(self.on_RequestProcessingTreeDataDbClick)

		# Меню финдействий
		self.menu_finactions_create.triggered.connect(self.on_RequestCreateFinactionsRecord)
		self.menu_finactions_import.triggered.connect(self.on_RequestImportFinactions)

		self.menu_finactions_record_open.triggered.connect(self.on_RequestOpenFinactionsRecord)
		self.menu_finactions_record_delete.triggered.connect(self.on_RequestDeleteFinactionsRecord)
		self.menu_finactions_record_split.triggered.connect(self.on_RequestSplitFinactionsRecord)
		self.menu_finactions_record_edit_note.triggered.connect(self.on_RequestEditNoteFinactionsRecord)

	def on_Show(self):
		""" Отображение формы """
		self.ShowTitle()

		self.InitModel()
		self.LoadFinactions()

		self.AdjustTreeData_Size()
		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Color()

	# Данные
	def on_UpdateDataPartial(self):
		""" Частичное обновление данных """
		self.ReadProcessingIdoFromWorkspace()
		self.ReadProcessingDdFromRecordFinactions()

		self.CleanFinactionsRecord()

		self.LoadDd()
		self.LoadFinactionsRecord()

		self.AdjustTreeData_Size()
		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Color()

	# Меню финдействий
	def on_RequestMenuFinactions(self):
		""" Запрос отображению меню финдействий """
		self.ReadProcessingDd()
		self.ReadProcessingIdo()

		self.AdjustMenuFinactionsEnable()
		self.AdjustMenuFinactionsText()

		self.ShowMenuFinactions()

	# Финдействия
	def on_RequestCreateFinactionsRecord(self):
		""" Запрос на создание записи финдействий """
		self.CreateFinactionsRecord()

		self.LoadDd()
		self.LoadFinactionsRecord()

		self.AdjustTreeData_Size()
		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Color()

	def on_RequestImportFinactions(self):
		""" Запрос на импорт финдействий """
		self.application.form_import.Open()

	# Запись финдействий
	def on_RequestOpenFinactionsRecord(self):
		""" Запрос на открытие записи финдействий """
		self.OpenFinactionsRecord()

	def on_RequestDeleteFinactionsRecord(self):
		""" Запрос на удаление записи финдействий """
		self.DeleteFinactionsRecord()

		self.AdjustTreeData_Size()
		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Color()

	def on_RequestSplitFinactionsRecord(self):
		""" Запрос на разделение записи финдействий """
		self.SplitFinactionsRecord()

		self.AdjustTreeData_Size()
		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Color()

	# Дерево данных
	def on_RequestProcessingTreeDataDbClick(self):
		""" Запрос на обработку двойного клика по дереву данных """
		self.ReadProcessingColumn()
		self.ReadProcessingDd()
		self.ReadProcessingIdo()

		self.ProcessingTreeData_DbClick()

	def on_RequestEditNoteFinactionsRecord(self):
		""" Запрос на редактирование примечания записи финдействий """
		self.EditNoteFinactionsRecord()

		self.LoadFinactionsRecord()

		self.AdjustTreeData_Size()

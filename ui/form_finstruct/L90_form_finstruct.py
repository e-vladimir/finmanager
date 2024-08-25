# ФОРМА ФИНСТРУКТУРА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_finstruct import C80_FormFinstruct


class C90_FormFinstruct(C80_FormFinstruct):
	""" Форма Финструктура: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных
		self.tree_data.customContextMenuRequested.connect(self.on_RequestMenuFinstruct)

		# Меню финструктуры
		self.menu_finstruct_create.triggered.connect(self.on_RequestCreateFinstructRecord)

		self.menu_finstruct_group_create.triggered.connect(self.on_RequestCreateFinstructRecordInGroup)

		self.menu_finstruct_record_rename.triggered.connect(self.on_RequestRenameFinstructRecord)
		self.menu_finstruct_record_delete.triggered.connect(self.on_RequestDeleteFinstructRecord)
		self.menu_finstruct_record_regroup.triggered.connect(self.on_RequestRegroupFinstructRecord)

	# Форма
	def on_Show(self):
		super().on_Show()

		self.ShowTitle()

		self.InitModel()
		self.LoadFinstruct()

		self.AdjustTreeDataSort()
		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

		self.CleanModel()

	# Меню финструктуры
	def on_RequestMenuFinstruct(self):
		""" Запрос на отображение меню финструктуры """
		self.ReadIdoProcessing()
		self.ReadNameProcessing()
		self.ReadGroupProcessing()

		self.AdjustMenuFinstructEnable()
		self.AdjustMenuFinstructText()

		self.ShowMenuFinstruct()

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

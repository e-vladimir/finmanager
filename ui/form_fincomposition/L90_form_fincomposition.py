# ФОРМА ФИНСОСТАВ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_fincomposition import C80_FormFincomposition


class C90_FormFincomposition(C80_FormFincomposition):
	""" Форма Финсостав: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево финсостава
		self.tree_data.customContextMenuRequested.connect(self.on_RequestMenuFincomposition)

		# Меню финсостава
		self.menu_fincomposition_append.triggered.connect(self.on_RequestAppendFincompositionRecordToTop)

	# Форма
	def on_Show(self):
		""" Открытие """
		self.ShowTitle()

		self.InitModelData()
		self.LoadFincomposition()

		self.AdjustTreeDataExpand()

	# Меню финсостава
	def on_RequestMenuFincomposition(self):
		""" Запрос на отображение меню финсостава """
		self.ReadIdoProcessingFromTreeData()
		self.ReadNameProcessingFromTreeData()

		self.AdjustMenuFincompositionText()
		self.AdjustMenuFincompositionEnable()

		self.ShowMenuFincomposition()

	# Запись финсостава
	def on_RequestAppendFincompositionRecordToTop(self):
		""" Запрос на создание записи финсостава верхнего уровня """
		self.AppendRecordFincompositionToTop()

		self.LoadFincomposition()

		self.AdjustTreeDataSort()
		self.AdjustTreeDataExpand()

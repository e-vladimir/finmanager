# ФОРМА ФИНДЕЙСТВИЯ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_finactions import C80_FormFinactions


class C90_FormFinactions(C80_FormFinactions):
	""" Форма Финдействия: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево финдействий
		self.tree_data.customContextMenuRequested.connect(self.on_RequestMenuFinactions)

		# Меню финдействий
		self.menu_finactions_create.triggered.connect(self.on_RequestCreateFinactionsRecord)
		self.menu_finactions_record_open.triggered.connect(self.on_RequestOpenFinactionsRecord)

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

		self.LoadRecordFinactions()

	# Меню финдействий
	def on_RequestMenuFinactions(self):
		""" Запрос отображению меню финдействий """
		self.ReadProcessingDd()
		self.ReadProcessingIdo()

		self.AdjustMenuFinactionsEnable()
		self.AdjustMenuFinactionsText()

		self.ShowMenuFinactions()

	# Запись финдействий
	def on_RequestCreateFinactionsRecord(self):
		""" Запрос на создание записи финдействий """
		self.CreateRecordFinactions()

		self.LoadDd()
		self.LoadRecordFinactions()

	def on_RequestOpenFinactionsRecord(self):
		""" Запрос на открытие записи финдействий """
		self.OpenRecordFinactions()

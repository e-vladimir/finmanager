# ФОРМА ОПЕРАЦИИ: ЛОГИКА УПРАВЛЕНИЯ
# 11 мар 2025

from L80_form_operation import C80_FormOperation


class C90_FormOperation(C80_FormOperation):
	""" Форма Операции: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных
		self.TreeData.customContextMenuRequested.connect(self.on_RequestMenuOperation)

		# Меню Операции
		self.ActionCreateOperation.triggered.connect(self.on_RequestCreateOperation)

		# Меню Операция
		self.ActionDeleteOperation.triggered.connect(self.on_RequestDeleteOperation)

	# Форма
	def on_Opened(self):
		""" Форма открыта """
		self.ShowTitle()

		self.InitModelData()
		self.ShowOperations()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Sort()
		self.AdjustTreeData_Colors()

		self.CleanModelData()

	# Меню операций
	def on_RequestMenuOperation(self):
		""" Запрос меню операций """
		self.ReadProcessingIdoFromTreeData()
		self.ReadProcessingDdFromTreeData()

		self.AdjustMenuOperations()
		self.AdjustMenuOperation_Enable()
		self.AdjustMenuOperation_Text()

		self.ShowMenuOperation()

	# Операция
	def on_RequestCreateOperation(self):
		""" Запрос создания операции """
		self.CreateOperation()

	def on_RequestDeleteOperation(self):
		""" Запрос удаления операции """
		self.DeleteOperation()

	def on_OperationCreated(self):
		""" Операция создана """
		self.LoadDdInModelData()
		self.LoadOperationOnModelData()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Sort()
		self.AdjustTreeData_Colors()

	def on_OperationDeleted(self):
		""" Операция удалена """
		self.CleanModelData()

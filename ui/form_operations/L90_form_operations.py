# ФОРМА ФИНАНСОВЫЕ ОПЕРАЦИИ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_operations import C80_FormOperations


class C90_FormOperations(C80_FormOperations):
	""" Форма Финансовые операции: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных
		self.tree_data.customContextMenuRequested.connect(self.on_RequestShowMenuOperations)

		# Меню Финансовые операции
		self.action_operations_create_operation.triggered.connect(self.on_RequestCreateOperation)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.InitModel()

		self.ShowOperations()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

	# Меню операций по счетам
	def on_RequestShowMenuOperations(self):
		""" Запрос меню операций по счетам """
		self.AdjustMenuOperations_Text()
		self.AdjustMenuOperations_Enable()

		self.ShowMenuOperations()

	# Финансовые операции
	def on_RequestCreateOperation(self):
		""" Запрос на создание финансовой операции """
		self.CreateOperation()

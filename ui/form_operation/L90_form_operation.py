# ФОРМА ФИНАНСОВАЯ ОПЕРАЦИЯ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_operation import C80_FormOperation


class C90_FormOperation(C80_FormOperation):
	""" Форма Финансовая операция: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных
		self.tree_data.doubleClicked.connect(self.on_RequestProcessingTreeDataDbClick)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ReadOperationFromWorkspace()

		self.InitModel()
		self.LoadOperation()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Color()
		self.AdjustTreeData_Size()

		self.ShowTitle()

	def on_Close(self):
		""" Закрытие формы """
		self.application.form_operations.UpdateDataPartial()

	# Дерево данных
	def on_RequestProcessingTreeDataDbClick(self):
		""" Запрос на обработку двойного клика по дереву данных """
		self.ReadProcessingIdoFromTreeData()

		self.ProcessingTreeData_DbClick()

	# Финансовая операция
	def on_RequestSetDate(self):
		""" Запрос на изменение даты """
		self.SetDate()

		self.LoadOperation()

	def on_RequestSetAmount(self):
		""" Запрос на изменение суммы """
		self.SetAmount()

		self.LoadOperation()

	def on_RequestSetDescription(self):
		""" Запрос на изменение описания """
		self.SetDescription()

		self.LoadOperation()

	def on_RequestSetAccounts(self):
		""" Запрос на изменение счетов """
		self.SetAccounts()

		self.LoadOperation()

	def on_RequestSetLabels(self):
		""" Запрос на изменение меток """
		self.SetLabels()

		self.LoadOperation()

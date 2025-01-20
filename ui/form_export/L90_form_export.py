# ФОРМА ЭКСПОРТ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_export import C80_FormExport


class C90_FormExport(C80_FormExport):
	""" Форма Экспорт данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных Финансовые операции
		self.tree_data_operations.customContextMenuRequested.connect(self.on_RequestShowMenuOperations)
		self.tree_data_operations.doubleClicked.connect(self.on_RequestProcessingTreeDataOperationsDbClick)

		# Меню экспорта Финансовых операций
		self.action_operations_input_set_date.triggered.connect(self.on_RequestSetDateInOperations)
		self.action_operations_input_set_account.triggered.connect(self.on_RequestSetAccountInOperations)
		self.action_operations_output_set_path.triggered.connect(self.on_RequestSetPathInOperations)
		self.action_operations_exec_export.triggered.connect(self.on_RequestExportOperations)

	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.InitModelDataOperations()

		self.CalcOperationsOutputFiles()

		self.LoadModelDataOperations()

		self.AdjustTreeDataOperations_Expand()
		self.AdjustTreeDataOperations_Color()
		self.AdjustTreeDataOperations_Size()

	# Меню экспорта Финансовые операции
	def on_RequestShowMenuOperations(self):
		""" Запрос на отображение меню Финансовые операции """
		self.ReadProcessingIdFromTreeDataOperations()

		self.AdjustMenuOperations_Text()
		self.AdjustMenuOperations_Enable()

		self.ShowMenuOperations()

	# Экспорт Финансовых операций
	def on_RequestSetDateInOperations(self):
		""" Запрос на изменение периода выборки Финансовых операций """
		self.SetDataInOperations()

		self.CalcOperationsOutputFiles()

		self.LoadModelDataOperations()

	def on_RequestSetAccountInOperations(self):
		""" Запрос на изменение счёта Финансовых операций """
		self.SetAccountInOperations()

		self.CalcOperationsOutputFiles()

		self.LoadModelDataOperations()

	def on_RequestSetPathInOperations(self):
		""" Запрос на изменение директории Финансовых операций """
		self.SetPathInOperations()

		self.LoadModelDataOperations()

	def on_RequestExportOperations(self):
		""" Запрос на выполнение экспорта Финансовых операций """
		self.ExportOperations()

	# Дерево данных Финансовые операции
	def on_RequestProcessingTreeDataOperationsDbClick(self):
		""" Запрос на обработку двойного клика по дереву данных Финансовые операции """
		self.ReadProcessingIdFromTreeDataOperations()

		self.ProcessingTreeDataOperations_DbClick()

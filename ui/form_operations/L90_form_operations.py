# ФОРМА ФИНАНСОВЫЕ ОПЕРАЦИИ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_operations import C80_FormOperations


class C90_FormOperations(C80_FormOperations):
	""" Форма Финансовые операции: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных
		self.tree_data.customContextMenuRequested.connect(self.on_RequestShowMenuOperations)
		self.tree_data.doubleClicked.connect(self.on_RequestProcessingTreeDataDbClick)

		# Меню Финансовые операции
		self.action_operations_create_operation.triggered.connect(self.on_RequestCreateOperation)
		self.action_operations_replace_text.triggered.connect(self.on_RequestReplaceText)
		self.action_operations_reset.triggered.connect(self.on_RequestResetData)

		# Меню Финансовая операция
		self.action_operation_open_operation.triggered.connect(self.on_RequestOpenOperation)
		self.action_operation_delete_operation.triggered.connect(self.on_RequestDeleteOperation)

		self.action_operation_split.triggered.connect(self.on_RequestSplitOperation)
		self.action_operation_set_description.triggered.connect(self.on_RequestSetOperationDescription)
		self.action_operation_set_labels.triggered.connect(self.on_RequestSetOperationLabels)

		self.action_operation_colors_set_black.triggered.connect(self.on_RequestSetOperationColorBlack)
		self.action_operation_colors_set_gray.triggered.connect(self.on_RequestSetOperationColorGray)
		self.action_operation_colors_set_green.triggered.connect(self.on_RequestSetOperationColorGreen)
		self.action_operation_colors_set_blue.triggered.connect(self.on_RequestSetOperationColorBlue)
		self.action_operation_colors_set_red.triggered.connect(self.on_RequestSetOperationColorRed)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.InitModel()

		self.ShowOperations()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()
		self.AdjustTreeData_Sort()

	def on_UpdateDataPartial(self):
		""" Частичное обновление данных """
		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()
		self.AdjustTreeData_Sort()

	def on_Resize(self):
		""" Изменение размера окна """
		self.AdjustTreeData_Size()

	# Дерево данных
	def on_RequestProcessingTreeDataDbClick(self):
		""" Реакция на двойной клик по дереву данных """
		self.ReadProcessingIdoFromTreeData()
		self.ReadProcessingColumnFromTreeData()

		self.ProcessingTreeDataDbClick()

	# Меню операций по счетам
	def on_RequestShowMenuOperations(self):
		""" Запрос меню операций по счетам """
		self.ReadProcessingIdoFromTreeData()
		self.ReadProcessingDdFromTreeData()

		self.AdjustMenuOperations_Text()
		self.AdjustMenuOperations_Enable()

		self.ShowMenuOperations()

	# Финансовые операции
	def on_RequestCreateOperation(self):
		""" Запрос на создание финансовой операции """
		self.CreateOperation()

		self.LoadDd()
		self.LoadOperation()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()
		self.AdjustTreeData_Sort()

	def on_RequestReplaceText(self):
		""" Запрос на поиск и замену текстового фрагмента """
		self.ReplaceText()

	def on_RequestResetData(self):
		""" Запрос на сброс данных """
		self.ResetData()

		self.InitModel()

		self.ShowOperations()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()
		self.AdjustTreeData_Sort()

	# Финансовая операция
	def on_RequestOpenOperation(self):
		""" Запрос на открытие финансовой операции """
		self.OpenOperation()

	def on_RequestDeleteOperation(self):
		""" Запрос на удаление финансовой операции """
		self.DeleteOperation()

		self.CleanOperation()
		self.CleanDd()

		self.AdjustTreeData_Size()
		self.AdjustTreeData_Sort()

	def on_RequestSetOperationColorBlack(self):
		""" Запрос на установку цвета операции: Чёрный """
		self.SetProcessingColorBlack()
		self.SetOperationColor()

		self.LoadOperation()

	def on_RequestSetOperationColorGray(self):
		""" Запрос на установку цвета операции: Серый """
		self.SetProcessingColorGray()
		self.SetOperationColor()

		self.LoadOperation()

	def on_RequestSetOperationColorGreen(self):
		""" Запрос на установку цвета операции: Зелёный """
		self.SetProcessingColorGreen()
		self.SetOperationColor()

		self.LoadOperation()

	def on_RequestSetOperationColorBlue(self):
		""" Запрос на установку цвета операции: Синий """
		self.SetProcessingColorBlue()
		self.SetOperationColor()

		self.LoadOperation()

	def on_RequestSetOperationColorRed(self):
		""" Запрос на установку цвета операции: Красный """
		self.SetProcessingColorRed()
		self.SetOperationColor()

		self.LoadOperation()

	def on_RequestSetOperationDescription(self):
		""" Запрос на редактирование описания операции """
		self.SetOperationDescription()

		self.LoadOperation()

	def on_RequestSetOperationLabels(self):
		""" Запрос на редактирование меток """
		self.SetOperationLabels()

		self.LoadOperation()

	def on_RequestSplitOperation(self):
		""" Запрос на разделение операции """
		self.SplitOperation()

		self.LoadOperation()

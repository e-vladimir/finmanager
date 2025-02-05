# ФОРМА ОБРАБОТКА ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_processing import C80_FormProcessing


class C90_FormProcessing(C80_FormProcessing):
	""" Форма Обработка данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Модель данных Обработка операций
		self.model_operations.itemChecked.connect(self.on_OperationsChanged)
		self.model_operations.itemUnchecked.connect(self.on_OperationsChanged)

		# Дерево данных Обработка операций
		self.tree_data_operations.doubleClicked.connect(self.on_RequestProcessingTreeDataOperations_DbClick)
		self.tree_data_operations.customContextMenuRequested.connect(self.on_RequestShowMenuOperations)

		# Меню Обработка операций
		self.action_operations_edit_include.triggered.connect(self.on_RequestEditOperationsInclude)
		self.action_operations_edit_exclude.triggered.connect(self.on_RequestEditOperationsExclude)
		self.action_operations_edit_destination.triggered.connect(self.on_RequestEditOperationsDestination)
		self.action_operations_edit_detail.triggered.connect(self.on_RequestEditOperationsDetail)
		self.action_operations_edit_object_int.triggered.connect(self.on_RequestEditOperationsObjectInt)
		self.action_operations_edit_object_ext.triggered.connect(self.on_RequestEditOperationsObjectExt)
		self.action_operations_edit_color.triggered.connect(self.on_RequestEditOperationsColor)
		self.action_operations_edit_interval.triggered.connect(self.on_RequestEditOperationsInterval)
		self.action_operations_processing.triggered.connect(self.on_RequestProcessingOperations)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.InitModelOperations()
		self.LoadModelOperations()
		self.AdjustTreeDataOperations_Expand()
		self.AdjustTreeDataOperations_Color()
		self.AdjustTreeDataOperations_Size()

	# Параметры Обработка операций
	def on_OperationsChanged(self):
		""" Параметры Обработка операций изменились """
		self.AdjustTreeDataOperations_Color()

	def on_RequestEditOperationsInclude(self):
		""" Запрос редактирования параметра Обработка операций - Фрагмент поиска """
		self.EditOperationsInclude()

		self.LoadModelOperations()
		self.AdjustTreeDataOperations_Color()

	def on_RequestEditOperationsExclude(self):
		""" Запрос редактирования параметра Обработка операций - Фрагмент исключения """
		self.EditOperationsExclude()

		self.LoadModelOperations()
		self.AdjustTreeDataOperations_Color()

	def on_RequestEditOperationsDestination(self):
		""" Запрос редактирования параметра Обработка операций - Назначение """
		self.EditOperationsDestination()

		self.LoadModelOperations()
		self.AdjustTreeDataOperations_Color()

	def on_RequestEditOperationsDetail(self):
		""" Запрос редактирования параметра Обработка операций - Уточнение """
		self.EditOperationsDetail()

		self.LoadModelOperations()
		self.AdjustTreeDataOperations_Color()

	def on_RequestEditOperationsObjectInt(self):
		""" Запрос редактирования параметра Обработка операций - Объект внутренний """
		self.EditOperationsObjectInt()

		self.LoadModelOperations()
		self.AdjustTreeDataOperations_Color()

	def on_RequestEditOperationsObjectExt(self):
		""" Запрос редактирования параметра Обработка операций - Объект внешний """
		self.EditOperationsObjectExt()

		self.LoadModelOperations()
		self.AdjustTreeDataOperations_Color()

	def on_RequestEditOperationsColor(self):
		""" Запрос редактирования параметра Обработка операций - Цветовая метка """
		self.EditOperationsColor()

		self.LoadModelOperations()
		self.AdjustTreeDataOperations_Color()

	def on_RequestEditOperationsInterval(self):
		""" Запрос редактирования параметра Обработка операций - Интервал обработки """
		self.SwitchOperationsInterval()

		self.LoadModelOperations()
		self.AdjustTreeDataOperations_Color()

	def on_RequestProcessingOperations(self):
		""" Запрос обработки операций """
		self.ProcessingOperations()

	# Дерево данных параметров Обработка операций
	def on_RequestProcessingTreeDataOperations_DbClick(self):
		""" Запрос обработки двойного клика по дереву данных Обработка операций """
		self.ReadProcessingIdoFromTreeDataOperations()
		self.ProcessingTreeDataOperations_DbClick()

	# Меню Обработка операций
	def on_RequestShowMenuOperations(self):
		""" Запрос на отображение меню Обработка операций """
		self.ReadProcessingIdoFromTreeDataOperations()

		self.AdjustMenuOperations_Text()
		self.AdjustMenuOperations_Enable()

		self.ShowMenuOperations()

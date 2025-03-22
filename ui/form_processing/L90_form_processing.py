# ФОРМА ОБРАБОТКА ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 22 мар 2025

from L80_form_processing import C80_FormProcessing


class C90_FormProcessing(C80_FormProcessing):
	""" Форма Обработка данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных Обработка операций
		self.TreeDataOperations.doubleClicked.connect(self.on_TreeDataProcessingOperationsDoubleClicked)

	# Форма
	def on_Opened(self):
		""" Форма открыта """
		self.InitModelDataOperation()
		self.LoadModelDataOperations()

		self.AdjustTreeDataOperations_Expand()
		self.AdjustTreeDataOperations_Size()
		self.AdjustTreeDataOperations_Color()

	# Параметры Обработка операций
	def on_RequestSetOperationsFilterDescription(self):
		""" Запрос изменения параметра Описание содержит """
		self.SetOperationsFilterDescription()

	def on_RequestSetOperationsReplaceDescription(self):
		""" Запрос изменения параметра Замена фрагмента описания """
		self.SetOperationsReplaceDescription()

	def on_RequestSetOperationsSetDescription(self):
		""" Запрос изменения параметра Установка описания """
		self.SetOperationsProcessingSetDescription()

	def on_RequestSetOperationsSetColor(self):
		""" Запрос изменения параметра Установка цвета """
		self.SetOperationsProcessingSetColor()

	def on_ProcessingOperationsChanged(self):
		""" Параметры обработки операций изменились """
		self.LoadModelDataOperations()

	# Дерево данных Обработка операций
	def on_TreeDataProcessingOperationsDoubleClicked(self):
		""" Двойной клик по дереву данных Обработка операций """
		self.ReadProcessingFieldFromTreeDataOperations()

		self.ControlProcessingField()

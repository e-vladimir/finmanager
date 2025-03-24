# ФОРМА ОБРАБОТКА ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 22 мар 2025

from L80_form_processing import C80_FormProcessing


class C90_FormProcessing(C80_FormProcessing):
	""" Форма Обработка данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Вкладки режимов обработки
		self.TabsMain.currentChanged.connect(self.on_TabMainChanged)

		# Дерево данных ручной обработки данных
		self.TreeDataManual.customContextMenuRequested.connect(self.on_RequestShowMenuManual)

		# Меню ручной обработки данных
		self.ActionManualObjectsTypeOperations.triggered.connect(self.on_RequestSwitchProcessingObjectsTypeToOperations)
		self.ActionManualObjectsTypeLabels.triggered.connect(self.on_RequestSwitchProcessingObjectsTypeToLabels)

	# Форма
	def on_Opened(self):
		""" Открытие формы """
		self.ShowTitle()

	# Вкладки режимов обработки
	def on_TabMainChanged(self):
		""" Изменилась текущая вкладка режима обработки """
		self.ShowTitle()

	# Меню ручной обработки данных
	def on_RequestShowMenuManual(self):
		""" Запрос отображению меню ручной обработки данных """
		self.AdjustMenuManual()
		self.AdjustMenuManualText()
		self.AdjustMenuManualEnable()

		self.ShowMenuManual()

	# Параметры ручной обработки данных
	def on_RequestSwitchProcessingObjectsTypeToOperations(self):
		""" Запрос на переключение объекта ручной обработки данных на операции """
		self.SwitchProcessingObjectsTypeToOperations()

	def on_RequestSwitchProcessingObjectsTypeToLabels(self):
		""" Запрос на переключение объекта ручной обработки данных на метки """
		self.SwitchProcessingObjectsTypeToLabels()

	def on_ProcessingObjectsTypeChanged(self):
		""" Изменился тип объекта для ручной обработки данных """
		self.ShowTitle()

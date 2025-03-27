# ФОРМА ОБРАБОТКА ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 22 мар 2025

from L80_form_processing import C80_FormProcessing


class C90_FormProcessing(C80_FormProcessing):
	""" Форма Обработка данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных ручной обработки данных
		self.TreeDataManual.customContextMenuRequested.connect(self.on_RequestShowMenuManual)
		self.TreeDataManual.doubleClicked.connect(self.on_RequestEditOptionsManual)

		# Меню ручной обработки данных
		self.ActionManualObjectsTypeOperations.triggered.connect(self.on_RequestSwitchProcessingObjectsTypeToOperations)

		self.ActionManualProcessing.triggered.connect(self.on_RequestManualProcessing)

	# Форма
	def on_Opened(self):
		""" Открытие формы """
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

	def on_RequestEditOptionsManual(self):
		""" Запрос редактирования параметров ручной обработки данных """
		self.ReadProcessingFieldFromTreeDataManual()
		self.EditOptionsManual()

	def on_RequestManualProcessing(self):
		""" Запрос выполнения ручной обработки данных """
		self.ReadManualDescriptionInclude()
		self.ReadManualDescriptionReplace()
		self.ReadManualDescriptionSet()
		self.ReadManualLabelsAdd()
		self.ReadManualLabelsExclude()
		self.ReadManualLabelsInclude()
		self.ReadManualLabelsRemove()
		self.ReadManualLabelsReplace()

		self.ManualProcessing()

		self.Application.FormOperations.PartialUpdateData()

	def on_ProcessingObjectsTypeChanged(self):
		""" Изменился тип объектов в режиме ручной обработки """
		self.InitModelDataManual()
		self.LoadModelDataManual()

		self.AdjustTreeDataManualExpand()
		self.AdjustTreeDataManualColor()
		self.AdjustTreeDataManualSize()

		self.AdjustTabsMainText()

	def on_OptionsManualChanged(self):
		""" Изменились параметры ручной обработки данных """
		self.LoadModelDataManual()

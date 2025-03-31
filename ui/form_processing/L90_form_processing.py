# ФОРМА ОБРАБОТКА ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 22 мар 2025

from L00_rules           import RULES
from L80_form_processing import C80_FormProcessing


class C90_FormProcessing(C80_FormProcessing):
	""" Форма Обработка данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных ручной обработки
		self.TreeDataManual.customContextMenuRequested.connect(self.on_RequestShowMenuManual)
		self.TreeDataManual.doubleClicked.connect(self.on_RequestEditOptionsManual)

		# Таблица данных автоматической обработки
		self.TableDataAuto.customContextMenuRequested.connect(self.on_RequestShowMenuAuto)

		# Меню ручной обработки
		self.ActionManualObjectsTypeOperations.triggered.connect(self.on_RequestSwitchProcessingObjectsTypeToOperations)
		self.ActionManualProcessing.triggered.connect(self.on_RequestManualProcessing)

		# Меню автоматической обработки
		self.ActionAutoRulesTypeReplaceDescription.triggered.connect(self.on_RequestSwitchProcessingRulesTypeToReplaceDescription)

		self.ActionAutoCreateRule.triggered.connect(self.on_RequestCreateRule)
		self.ActionAutoDeleteRule.triggered.connect(self.on_RequestDeleteRule)

	# Форма
	def on_Opened(self):
		""" Открытие формы """
		self.ShowTitle()

		self.SwitchTabsMainToManual()
		self.SwitchProcessingObjectsTypeToOperations()

	# Меню ручной обработки
	def on_RequestShowMenuManual(self):
		""" Запрос отображению меню ручной обработки """
		self.AdjustMenuManual()
		self.AdjustMenuManualText()
		self.AdjustMenuManualEnable()

		self.ShowMenuManual()

	# Меню автоматической обработки
	def on_RequestShowMenuAuto(self):
		""" Запрос отображению меню автоматической обработки """
		self.ReadProcessingIdoFromTableDataAuto()

		self.AdjustMenuAuto()
		self.AdjustMenuAutoText()
		self.AdjustMenuAutoEnable()

		self.ShowMenuAuto()

	# Параметры ручной обработки
	def on_RequestSwitchProcessingObjectsTypeToOperations(self):
		""" Запрос на переключение объекта ручной обработки на операции """
		self.SwitchProcessingObjectsTypeToOperations()

	def on_RequestEditOptionsManual(self):
		""" Запрос редактирования параметров ручной обработки """
		self.ReadProcessingFieldFromTreeDataManual()
		self.EditOptionsManual()

	def on_RequestManualProcessing(self):
		""" Запрос выполнения ручной обработки """
		self.ReadManualDescriptionAdd()
		self.ReadManualDescriptionExclude()
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
		""" Изменились параметры ручной обработки """
		self.LoadModelDataManual()

	# Параметры автоматической обработки
	def on_RequestSwitchProcessingRulesTypeToReplaceDescription(self):
		""" Запрос на изменение типа правил на замену описания """
		self.SwitchProcessingRulesTypeToReplaceDescription()

	def on_ProcessingRulesTypeChanged(self):
		""" Изменился тип правил в режиме автоматической обработки """
		self.InitModelDataAuto()
		self.LoadRules()

		self.AdjustTabsMainText()
		self.AdjustTableDataAutoSort()
		self.AdjustTableDataAutoSize()

	# Правило автоматической обработки
	def on_RequestCreateRule(self):
		""" Запрос создания правила автоматической обработки """
		self.CreateRule()

	def on_RequestDeleteRule(self):
		""" Запрос удаления правила автоматической обработки """
		self.DeleteRule()

	def on_RuleCreated(self):
		""" Создано правило автоматической обработки """
		match self.processing_rules_type:
			case RULES.REPLACE_DESCRIPTION: self.LoadRuleReplaceDescriptionInModel()

	def on_RuleDeleted(self):
		""" Удалено правила автоматической обработки """
		self.InitModelDataAuto()
		self.LoadRules()

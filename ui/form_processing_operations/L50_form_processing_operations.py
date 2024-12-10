# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: МОДЕЛЬ СОБЫТИЙ

from L42_form_processing_operations import C42_FormProcessingOperations


class C50_FormProcessingOperations(C42_FormProcessingOperations):
	""" Форма Обработка операций: Модель событий """

	# Меню правил обработки
	def on_RequestShowMenuRules(self): pass

	# Меню инструментов обработки
	def on_RequestShowMenuTools(self): pass

	# Тип правил обработки
	def on_RequestSwitchRulesToDescription(self): pass
	def on_RequestSwitchRulesToDestination(self): pass
	def on_RequestSwitchRulesToLabels(self): pass

	# Правила обработки
	def on_RequestCreateRule(self): pass
	def on_RequestApplyRules(self): pass

	# Правило обработки
	def on_RequestOpenRule(self): pass
	def on_RequestDeleteRule(self): pass

	# Дерево инструментов обработки
	def on_RequestProcessingTreeTools_DbClick(self): pass

	# Инструменты обработки описания
	def on_RequestEditToolsDescriptionInclude(self): pass
	def on_RequestSelectToolsDescriptionInclude(self): pass
	def on_RequestEditToolsDescriptionApplies(self): pass
	def on_RequestDescriptionProcessing(self): pass

	# Инструменты обработки назначения
	def on_RequestEditToolsDestinationInclude(self): pass
	def on_RequestSelectToolsDestinationInclude(self): pass
	def on_RequestEditToolsDestinationApplies(self): pass
	def on_RequestDestinationProcessing(self): pass

	# Инструменты обработки меток
	def on_RequestSwitchToolsLabelsModeToReplace(self): pass
	def on_RequestSwitchToolsLabelsModeToAppend(self): pass
	def on_RequestSwitchToolsLabelsModeToExpand(self): pass
	def on_RequestEditToolsLabelsInclude(self): pass
	def on_RequestSelectToolsLabelsInclude(self): pass
	def on_RequestEditToolsLabelsApplies(self): pass
	def on_RequestSelectToolsLabelsApplies(self): pass
	def on_RequestLabelsProcessing(self): pass

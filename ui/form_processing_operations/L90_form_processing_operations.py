# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_processing_operations import C80_FormProcessingOperations


class C90_FormProcessingOperations(C80_FormProcessingOperations):
	""" Форма Обработка операций: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица правил обработки
		self.table_rules.customContextMenuRequested.connect(self.on_RequestShowMenuRules)
		self.table_rules.doubleClicked.connect(self.on_RequestOpenRule)

		# Дерево инструментов обработки
		self.tree_tools.customContextMenuRequested.connect(self.on_RequestShowMenuTools)
		self.tree_tools.doubleClicked.connect(self.on_RequestProcessingTreeTools_DbClick)

		# Меню Типы правил
		self.action_rules_types_description.triggered.connect(self.on_RequestSwitchRulesToDescription)
		self.action_rules_types_destination.triggered.connect(self.on_RequestSwitchRulesToDestination)
		self.action_rules_types_labels.triggered.connect(self.on_RequestSwitchRulesToLabels)

		# Меню Правила обработки
		self.action_rules_rules_create.triggered.connect(self.on_RequestCreateRule)
		self.action_rules_rules_apply.triggered.connect(self.on_RequestApplyRules)

		# Меню Правило обработки
		self.action_rules_rule_open.triggered.connect(self.on_RequestOpenRule)
		self.action_rules_rule_delete.triggered.connect(self.on_RequestDeleteRule)

		# Меню Инструменты обработки
		self.action_tools_description_include_edit.triggered.connect(self.on_RequestEditToolsDescriptionInclude)
		self.action_tools_description_include_select.triggered.connect(self.on_RequestSelectToolsDescriptionInclude)
		self.action_tools_description_applies_edit.triggered.connect(self.on_RequestEditToolsDescriptionApplies)
		self.action_tools_description_processing.triggered.connect(self.on_RequestDescriptionProcessing)

		self.action_tools_destination_include_edit.triggered.connect(self.on_RequestEditToolsDestinationInclude)
		self.action_tools_destination_include_select.triggered.connect(self.on_RequestSelectToolsDestinationInclude)
		self.action_tools_destination_applies_edit.triggered.connect(self.on_RequestEditToolsDestinationApplies)
		self.action_tools_destination_processing.triggered.connect(self.on_RequestDestinationProcessing)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.InitTabsMain()

		self.ShowTitle()

		self.InitModelRules()
		self.ShowRules()
		self.AdjustTableRules_Size()

		self.InitModelTools()
		self.LoadToolsDescriptionToModel()
		self.LoadToolsDestinationToModel()
		self.LoadToolsLabelsToModel()
		self.AdjustTreeTools_Expand()
		self.AdjustTreeTools_Color()
		self.AdjustTreeTools_Size()

	def on_Show(self):
		""" Отображение формы """
		self.AdjustTableRules_Size()

	# Тип правил
	def on_RequestSwitchRulesToDescription(self):
		""" Переключение на тип правил обработки: Описание """
		self.SwitchRuleTypesToDescription()

		self.InitModelRules()
		self.ShowRules()
		self.AdjustTableRules_Size()

	def on_RequestSwitchRulesToDestination(self):
		""" Переключение на тип правил обработки: Назначение """
		self.SwitchRuleTypesToDestination()

		self.InitModelRules()
		self.ShowRules()
		self.AdjustTableRules_Size()

	def on_RequestSwitchRulesToLabels(self):
		""" Переключение на тип правил обработки: Метки """
		self.SwitchRuleTypesToLabels()

		self.InitModelRules()
		self.ShowRules()
		self.AdjustTableRules_Size()

	# Меню правил обработки
	def on_RequestShowMenuRules(self):
		""" Запрос отображения меню правил обработки """
		self.ReadProcessingIdoFromTableRules()

		self.AdjustMenuRules_Text()
		self.AdjustMenuRules_Enable()

		self.ShowMenuRules()

	# Меню инструментов обработки
	def on_RequestShowMenuTools(self):
		""" Запрос на отображение меню инструментов обработки """
		self.AdjustMenuTools_Text()
		self.AdjustMenuTools_Enable()

		self.ShowMenuTools()

	# Правила обработки
	def on_RequestCreateRule(self):
		""" Запрос создания правила """
		self.CreateRule()

		self.application.form_processing_rule.Open()

	def on_RequestApplyRules(self):
		""" Запрос на применение правил обработки """
		self.ApplyRules()

		self.application.form_operations.UpdateData()

	# Правило обработки
	def on_RequestOpenRule(self):
		""" Запрос открытия правила """
		self.ReadProcessingIdoFromTableRules()
		self.WriteProcessingRuleToWorkspace()

		self.application.form_processing_rule.Open()

	def on_RequestDeleteRule(self):
		""" Запрос на удаление правила обработки """
		self.DeleteRule()
		self.InitModelRules()
		self.ShowRules()

	# Обработка описания
	def on_RequestEditToolsDescriptionInclude(self):
		""" Запрос на редактирование Содержит обработки описания """
		self.EditToolsDescriptionInclude()
		
		self.LoadToolsDescriptionToModel()

	def on_RequestSelectToolsDescriptionInclude(self):
		""" Запрос на выбор Содержит обработки описания """
		self.SelectToolsDescriptionInclude()

		self.LoadToolsDescriptionToModel()

	def on_RequestEditToolsDescriptionApplies(self):
		""" Запрос на редактирование Применяется обработки описания """
		self.EditToolsDescriptionApplies()

		self.LoadToolsDescriptionToModel()

	def on_RequestDescriptionProcessing(self):
		""" Запрос на обработку описания """
		self.ProcessingDescription()

		self.application.form_operations.UpdateData()

	# Обработка назначения
	def on_RequestEditToolsDestinationInclude(self):
		""" Запрос на редактирование Содержит обработки назначения """
		self.EditToolsDestinationInclude()

		self.LoadToolsDestinationToModel()

	def on_RequestSelectToolsDestinationInclude(self):
		""" Запрос на выбор Содержит обработки назначения """
		self.SelectToolsDestinationInclude()

		self.LoadToolsDestinationToModel()

	def on_RequestEditToolsDestinationApplies(self):
		""" Запрос на редактирование Применяется обработки назначения """
		self.EditToolsDestinationApplies()

		self.LoadToolsDestinationToModel()

	def on_RequestDestinationProcessing(self):
		""" Запрос на обработку назначения """
		self.ProcessingDestination()

		self.application.form_operations.UpdateData()

	# Дерево инструментов обработки
	def on_RequestProcessingTreeTools_DbClick(self):
		""" Запрос на обработку двойного клика по дереву инструментов """
		self.ReadProcessingToolFromTreeTools()

		self.ProcessingTreeTools_DbClick()

# ФОРМА УПРАВЛЕНИЕ НАЗНАЧЕНИЕМ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_control_destination import C80_FormControlDestination


class C90_FormControlDestination(C80_FormControlDestination):
	""" Форма Управление назначением: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица правил сопоставления назначения
		self.table_rules.customContextMenuRequested.connect(self.on_RequestShowMenuRules)
		self.table_rules.doubleClicked.connect(self.on_RequestProcessingTableRules_DbClick)

		# Меню правил сопоставления назначения
		self.action_rules_rules_create_rule.triggered.connect(self.on_RequestCreateRule)
		self.action_rules_rules_apply.triggered.connect(self.on_RequestApplyRules)

		# Меню правила сопоставления назначения
		self.action_rules_rule_delete_rule.triggered.connect(self.on_RequestDeleteRule)
		self.action_rules_rule_edit_input.triggered.connect(self.on_RequestEditInput)
		self.action_rules_rule_edit_output.triggered.connect(self.on_RequestEditOutput)

		# Список доступных фрагментов поиска
		self.list_control_replace_available.doubleClicked.connect(self.on_RequestListControlReplaceAvailable_DbClick)

		# Кнопка Поиск и замена
		self.btn_control_replace.clicked.connect(self.on_RequestExecReplace)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.SwitchTabsMainToFirst()

		self.ShowTitle()

		self.InitModelRules()
		self.ShowRules()
		self.AdjustTableRules_Sizes()
		self.AdjustTableRules_Sort()

		self.FillListControlReplaceAvailable()

	# Меню сопоставления назначения
	def on_RequestShowMenuRules(self):
		""" Запрос на вызов меню сопоставления назначения """
		self.ReadProcessingIdoFromTableRules()

		self.AdjustMenuRules_Text()
		self.AdjustMenuRules_Enable()

		self.ShowMenuRules()

	# Таблица правил
	def on_RequestProcessingTableRules_DbClick(self):
		""" Запрос на обработку двойного клика по таблице правил """
		self.ReadProcessingIdoFromTableRules()
		self.ReadProcessingColumnFromTableRule()

		self.ProcessingTableRules_DbClick()

	# Правила сопоставления назначения
	def on_RequestApplyRules(self):
		""" Запрос применения правил сопоставления назначения """
		self.ApplyRules()

		self.application.form_operations.ShowOperations()

	# Правило сопоставления назначения
	def on_RequestCreateRule(self):
		""" Создание правила сопоставления назначения """
		self.CreateRule()

		self.LoadRuleInModel()
		self.AdjustTableRules_Sort()

	def on_RequestDeleteRule(self):
		""" Запрос на удаление правила сопоставления назначения """
		self.DeleteRule()

		self.InitModelRules()
		self.ShowRules()
		self.AdjustTableRules_Sizes()
		self.AdjustTableRules_Sort()

	def on_RequestEditInput(self):
		""" Запрос редактирования входа правила """
		self.EditRuleInput()

		self.LoadRuleInModel()

		self.AdjustTableRules_Sizes()
		self.AdjustTableRules_Sort()

	def on_RequestEditOutput(self):
		""" Запрос редактирования выхода правила """
		self.EditRuleOutput()

		self.LoadRuleInModel()

		self.AdjustTableRules_Sizes()
		self.AdjustTableRules_Sort()

	# Список доступных фрагментов поиска
	def on_RequestListControlReplaceAvailable_DbClick(self):
		""" Обработка двойного клика по списку доступных фрагментов поиска """
		self.ExtendEditControlReplaceInputFromAvailable()

	# Вкладка Поиск и замена
	def on_RequestExecReplace(self):
		""" Запрос на выполнение поиска и замены """
		self.ExecReplace()
		self.FillListControlReplaceAvailable()

		self.application.form_operations.ShowOperations()

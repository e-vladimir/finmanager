# ФОРМА УПРАВЛЕНИЕ ОПИСАНИЕМ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_control_description import C80_FormControlDescription


class C90_FormControlDescription(C80_FormControlDescription):
	""" Форма Управление описанием: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица правил автозамены описания
		self.table_rules.customContextMenuRequested.connect(self.on_RequestShowMenuRules)
		self.table_rules.doubleClicked.connect(self.on_RequestProcessingTableRules_DbClick)

		# Меню правил автозамены описания
		self.action_rules_rules_create_rule.triggered.connect(self.on_RequestCreateRule)
		self.action_rules_rules_apply.triggered.connect(self.on_RequestApplyRules)

		# Меню правила автозамены описания
		self.action_rules_rule_delete_rule.triggered.connect(self.on_RequestDeleteRule)
		self.action_rules_rule_edit_input.triggered.connect(self.on_RequestEditInput)
		self.action_rules_rule_edit_output.triggered.connect(self.on_RequestEditOutput)
		self.action_rules_rule_apply.triggered.connect(self.on_RequestApplyRule)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.SwitchTabsMainToFirst()

		self.ShowTitle()

		self.InitModelRules()
		self.ShowRules()
		self.AdjustTableRules_Sizes()
		self.AdjustTableRules_Sort()

		self.InitModelControl()

	# Меню автозамены описания
	def on_RequestShowMenuRules(self):
		""" Запрос на вызов меню автозамены описания """
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

	# Правила автозамены описания
	def on_RequestApplyRules(self):
		""" Запрос применения правил автозамены описания """
		self.ApplyRules()

		self.application.form_operations.ShowOperations()

	# Правило автозамены описания
	def on_RequestCreateRule(self):
		""" Создание правила автозамены описания """
		self.CreateRule()

		self.LoadRuleInModel()
		self.AdjustTableRules_Sort()

	def on_RequestDeleteRule(self):
		""" Запрос на удаление правила автозамены описания """
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

	def on_RequestApplyRule(self):
		""" Запрос на применение правила """
		self.ApplyRule()

		self.application.form_operations.ShowOperations()

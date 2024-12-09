# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_processing_operations import C80_FormProcessingOperations


class C90_FormProcessingOperations(C80_FormProcessingOperations):
	""" Форма Обработка операций: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список субъектов обработки
		self.cbbox_subject.activated.connect(self.on_SubjectChanged)

		# Таблица правил обработки
		self.table_rules.customContextMenuRequested.connect(self.on_RequestShowMenuRules)
		self.table_rules.doubleClicked.connect(self.on_RequestOpenRule)

		# Таблица инструментов
		self.table_tools.customContextMenuRequested.connect(self.on_RequestShowMenuTools)

		# Меню Правила обработки
		self.action_rules_rules_create.triggered.connect(self.on_RequestCreateRule)
		self.action_rules_rules_apply.triggered.connect(self.on_RequestApplyRules)

		# Меню Правило обработки
		self.action_rules_rule_open.triggered.connect(self.on_RequestOpenRule)
		self.action_rules_rule_delete.triggered.connect(self.on_RequestDeleteRule)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.FillCbboxSubject()
		self.ReadProcessingSubjectFromCbboxSubject()

		self.InitModelRules()
		self.ShowRules()
		self.AdjustTableRules_Size()

	def on_Show(self):
		""" Отображение формы """
		self.AdjustTableRules_Size()

	# Субъект обработки
	def on_SubjectChanged(self):
		""" Изменился субъект обработки """
		self.ReadProcessingSubjectFromCbboxSubject()

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

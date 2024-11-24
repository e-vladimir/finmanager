# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_rules import C80_FormRules


class C90_FormRules(C80_FormRules):
	""" Форма Правила обработки данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список типов обработки данных
		self.cbbox_types.activated.connect(self.on_RulesTypeChanged)

		# Таблица данных
		self.table_data.customContextMenuRequested.connect(self.on_RequestShowMenuRules)
		self.table_data.doubleClicked.connect(self.on_RequestOpenRule)

		# Тип правил обработки данных
		self.action_rules_type_create_rule.triggered.connect(self.on_RequestCreateRule)
		self.action_rules_type_reset.triggered.connect(self.on_RequestResetData)

		# Правило обработки данных
		self.action_rules_rule_open_rule.triggered.connect(self.on_RequestOpenRule)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.FillCbboxTypes()
		self.ShowCbboxTypes()

		self.ReadProcessingTypeFromCbboxTypes()

		self.InitModelData()

		self.ShowRules()

		self.AdjustTableData_Size()
		self.AdjustTableData_Order()
		self.AdjustTableData_Color()

	# Список типов правил обработки данных
	def on_RulesTypeChanged(self):
		""" Тип правил обработки данных изменился """
		self.ReadProcessingTypeFromCbboxTypes()

		self.InitModelData()

		self.ShowRules()

		self.AdjustTableData_Size()
		self.AdjustTableData_Order()
		self.AdjustTableData_Color()

	# Меню правил обработки данных
	def on_RequestShowMenuRules(self):
		""" Запрос на отображение правил обработки данных """
		self.AdjustMenuRules_Text()
		self.AdjustMenuRules_Enable()

		self.ShowMenuRules()

	# Тип правил обработки данных
	def on_RequestCreateRule(self):
		""" Запрос создания правила обработки данных """
		self.CreateRule()

		self.InitModelData()

		self.ShowRules()

		self.AdjustTableData_Size()
		self.AdjustTableData_Order()
		self.AdjustTableData_Color()

	def on_RequestResetData(self):
		""" Запрос на сброс данных """
		self.ResetData()

		self.InitModelData()

		self.ShowRules()

		self.AdjustTableData_Size()
		self.AdjustTableData_Order()
		self.AdjustTableData_Color()

	# Правило обработки данных
	def on_RequestOpenRule(self):
		""" Запрос на открытие правила обработки данных """
		self.ReadProcessingIdoFromTableData()

		self.OpenRule()

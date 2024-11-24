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

		# Правила обработки данных
		self.action_rules_type_create_rule.triggered.connect(self.on_RequestCreateRule)

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

	# Правило обработки данных
	def on_RequestCreateRule(self):
		""" Запрос создания правила обработки данных """
		self.CreateRule()

		self.InitModelData()

		self.ShowRules()

		self.AdjustTableData_Size()
		self.AdjustTableData_Order()
		self.AdjustTableData_Color()

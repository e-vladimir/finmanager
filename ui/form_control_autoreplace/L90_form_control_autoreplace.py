# ФОРМА УПРАВЛЕНИЕ АВТОЗАМЕНОЙ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_control_autoreplace import C80_FormControlAutoreplace


class C90_FormControlAutoreplace(C80_FormControlAutoreplace):
	""" Форма Управление автозаменой: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Меню правил автозамены
		self.action_rules_create_rule.triggered.connect(self.on_RequestCreateRule)

		# Таблица данных
		self.table_data.customContextMenuRequested.connect(self.on_RequestShowMenuRules)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.InitModelData()

		self.ShowRules()

		self.AdjustTableData_Size()
		self.AdjustTableData_Sort()

	def on_Show(self):
		""" Отображение формы """
		self.AdjustTableData_Size()

	# Меню Правил автозамены
	def on_RequestShowMenuRules(self):
		""" Запрос отображения меню Правил автозамены """
		self.ReadProcessingIdoFromTableData()
		self.ReadProcessingOutputFromTableData()

		self.AdjustMenuRules_Enable()
		self.AdjustMenuRules_Text()

		self.ShowMenuRules()

	# Правило автозамены
	def on_RequestCreateRule(self):
		""" Запрос на создание правила автозамены """
		self.CreateRule()

		self.LoadRuleAutoreplace()

		self.AdjustTableData_Size()
		self.AdjustTableData_Sort()

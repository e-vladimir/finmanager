# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_rules import C80_FormRules


class C90_FormRules(C80_FormRules):
	""" Форма Правила обработки данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список типов обработки данных
		self.cbbox_types.activated.connect(self.on_RulesTypeChanged)

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

	# Список типов правил обработки данных
	def on_RulesTypeChanged(self):
		""" Тип правил обработки данных изменился """
		self.ReadProcessingTypeFromCbboxTypes()

		self.InitModelData()

		self.ShowRules()

		self.AdjustTableData_Size()
		self.AdjustTableData_Order()

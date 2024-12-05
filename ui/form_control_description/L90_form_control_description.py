# ФОРМА УПРАВЛЕНИЕ ОПИСАНИЕМ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_control_description import C80_FormControlDescription


class C90_FormControlDescription(C80_FormControlDescription):
	""" Форма Управление описанием: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица правил автозамены описания
		self.table_rules.customContextMenuRequested.connect(self.on_RequestShowMenuRules)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.SwitchTabsMainToFirst()

		self.ShowTitle()

		self.InitModelRules()
		self.LoadRuleInModel()
		self.AdjustTableRules_Sizes()
		self.AdjustTableRules_Sort()

		self.InitModelControl()

	# Меню автозамены описания
	def on_RequestShowMenuRules(self):
		""" Запрос на вызов меню автозамены описания """
		self.AdjustMenuRules_Text()
		self.AdjustMenuRules_Enable()

		self.ShowMenuRules()

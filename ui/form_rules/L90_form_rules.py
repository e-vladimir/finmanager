# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
from L00_rules import RULES
from L80_form_rules import C80_FormRules


class C90_FormRules(C80_FormRules):
	""" Форма Правила обработки данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список типов правил
		self.list_types.clicked.connect(self.on_SwitchRulesType)

		# Таблица данных
		self.table_data.customContextMenuRequested.connect(self.on_RequestMenuRules)

		# Меню правил обработки данных
		self.menu_rules_create.triggered.connect(self.on_RequestCreateRule)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.FillListTypes()

		self.ReadProcessingType()

		self.ShowTitle()

	# Тип правил
	def on_SwitchRulesType(self):
		""" Изменился тип правил """
		self.ReadProcessingType()

		self.InitModelData()
		self.LoadRules()

		self.AdjustTableDataSort()
		self.AdjustTableDataSize()

		self.ShowTitle()

	# Меню правил обработки данных
	def on_RequestMenuRules(self):
		"""  """
		self.AdjustMenuRulesText()
		self.AdjustMenuRulesEnable()

		self.ShowMenuRules()

	# Правило обработки данных
	def on_RequestCreateRule(self):
		""" Запрос создания правила обработки данных """
		match self._processing_type:
			case RULES.REPLACE_TEXT: self.CreateRuleReplaceText()
			case RULES.DETECT_LABEL: self.CreateRuleDetectLabel()
			case _                 : return

		self.LoadRules()

		self.AdjustTableDataSort()
		self.AdjustTableDataSize()

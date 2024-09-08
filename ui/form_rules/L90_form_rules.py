# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L00_rules      import RULES
from L80_form_rules import C80_FormRules


class C90_FormRules(C80_FormRules):
	""" Форма Правила обработки данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список типов правил
		self.list_types.clicked.connect(self.on_SwitchRulesType)

		# Таблица данных
		self.table_data.customContextMenuRequested.connect(self.on_RequestMenuRules)
		self.table_data.doubleClicked.connect(self.on_RequestProcessingDbClickTableData)

		# Меню правил обработки данных
		self.menu_rules_create.triggered.connect(self.on_RequestCreateRule)
		self.menu_rule_edit_input.triggered.connect(self.on_RequestEditInputRule)
		self.menu_rule_edit_output.triggered.connect(self.on_RequestEditOutputRule)
		self.menu_rule_delete.triggered.connect(self.on_RequestDeleteRule)

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
		""" Запрос вызова меню """
		self.ReadProcessingIdo()
		self.ReadProcessingName()

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

	def on_RequestEditInputRule(self):
		""" Запрос на редактирование входа """
		match self._processing_type:
			case RULES.REPLACE_TEXT: self.EditInputRuleReplaceText()
			case RULES.DETECT_LABEL: self.EditInputRuleDetectLabel()
			case _                 : return

		self.LoadRulesRecord()

		self.AdjustTableDataSort()
		self.AdjustTableDataSize()

	def on_RequestEditOutputRule(self):
		""" Запрос на редактирование выхода """
		match self._processing_type:
			case RULES.REPLACE_TEXT: self.EditOutputRuleReplaceText()
			case RULES.DETECT_LABEL: self.EditOutputRuleDetectLabel()
			case _                 : return

		self.LoadRulesRecord()

		self.AdjustTableDataSort()
		self.AdjustTableDataSize()

	def on_RequestDeleteRule(self):
		""" Запрос на удаление  """
		match self._processing_type:
			case RULES.REPLACE_TEXT: self.DeleteRuleReplaceText()
			case RULES.DETECT_LABEL: self.DeleteRuleDetectLabel()
			case _                 : return

		self.InitModelData()
		self.LoadRules()

		self.AdjustTableDataSort()
		self.AdjustTableDataSize()

	# Таблица данных
	def on_RequestProcessingDbClickTableData(self):
		""" Запрос реакции на двойной клик по таблице """
		self.ReadProcessingIdo()
		self.ReadProcessingColumn()

		match self._processing_column:
			case 0: self.on_RequestEditInputRule()
			case 1: self.on_RequestEditOutputRule()

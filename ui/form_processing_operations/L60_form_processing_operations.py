# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: МЕХАНИКА ДАННЫХ

from L00_form_processing_operations import MODES, TOOLS
from L00_rules                      import RULES

from L20_PySide6                    import C20_StandardItem, ROLES
from L50_form_processing_operations import C50_FormProcessingOperations
from L90_rules                      import C90_ProcessingRule


class C60_FormProcessingOperations(C50_FormProcessingOperations):
	""" Форма Обработка операций: Механика данных """

	# Модель правил
	def InitModelRules(self):
		""" Инициализация модели правил """
		self.model_rules.removeAll()

		match self._processing_rule_types:
			case RULES.REPLACE_DESCRIPTION: self.model_rules.setHorizontalHeaderLabels(["Фрагменты поиска", "Фрагмент замены"])
			case RULES.MATCH_DESTINATION  : self.model_rules.setHorizontalHeaderLabels(["Фрагменты поиска", "Фрагмент сопоставления"])
			case RULES.DETECT_LABEL       : self.model_rules.setHorizontalHeaderLabels(["Фрагменты поиска", "Применяемые метки"])

	def LoadRuleToModel(self):
		""" Загрузка правила в модель """
		if not self.model_rules.checkIdo(self._processing_ido):
			item_input  = C20_StandardItem("")
			item_input.setData(self._processing_ido, ROLES.IDO)

			item_output = C20_StandardItem("")
			item_output.setData(self._processing_ido, ROLES.IDO)

			self.model_rules.invisibleRootItem().appendRow([item_input, item_output])

		rule        = C90_ProcessingRule(self._processing_ido)

		indexes     = self.model_rules.indexesInRowByIdo(self._processing_ido)
		item_input  = self.model_rules.itemFromIndex(indexes[0])
		item_input.setText('\n'.join(rule.InputAsStrings()))

		item_output = self.model_rules.itemFromIndex(indexes[1])
		item_output.setText('\n'.join(rule.OutputAsStrings()))

	# Модель инструментов
	def InitModelTools(self):
		""" Инициализация модели инструментов """
		self.model_tools.removeAll()
		self.model_tools.setHorizontalHeaderLabels(["", ""])

	def LoadToolsDescriptionToModel(self):
		""" Загрузка инструментов описания в модель """
		if not self.model_tools.checkIdo(TOOLS.GROUP_DESCRIPTION):
			item_group = C20_StandardItem("ОБРАБОТКА ОПИСАНИЯ")
			item_group.setData(TOOLS.GROUP_DESCRIPTION, ROLES.IDO)
			item_group.setData(TOOLS.GROUP_DESCRIPTION, ROLES.GROUP)

			item_space = C20_StandardItem("")
			item_space.setData(TOOLS.GROUP_DESCRIPTION, ROLES.IDO)
			item_space.setData(TOOLS.GROUP_DESCRIPTION, ROLES.GROUP)

			self.model_tools.invisibleRootItem().appendRow([item_group, C20_StandardItem("")])

		item_group                          = self.model_tools.itemByData(TOOLS.GROUP_DESCRIPTION, ROLES.IDO)

		if not self.model_tools.checkIdo(TOOLS.DESCRIPTION_INCLUDE):
			item_field = C20_StandardItem("Описание содержит")
			item_field.setData(TOOLS.DESCRIPTION_INCLUDE, ROLES.IDO)
			item_field.setData(TOOLS.GROUP_DESCRIPTION,   ROLES.GROUP)

			item_space = C20_StandardItem("")
			item_space.setData(TOOLS.DESCRIPTION_INCLUDE, ROLES.IDO)
			item_space.setData(TOOLS.GROUP_DESCRIPTION,   ROLES.GROUP)

			item_group.appendRow([item_field, item_space])

		if not self.model_tools.checkIdo(TOOLS.DESCRIPTION_APPLIES):
			item_field = C20_StandardItem("Применяется замена")
			item_field.setData(TOOLS.DESCRIPTION_APPLIES, ROLES.IDO)
			item_field.setData(TOOLS.GROUP_DESCRIPTION,       ROLES.GROUP)

			item_space = C20_StandardItem("")
			item_space.setData(TOOLS.DESCRIPTION_APPLIES, ROLES.IDO)
			item_space.setData(TOOLS.GROUP_DESCRIPTION,       ROLES.GROUP)

			item_group.appendRow([item_field, item_space])

			self.model_tools.fastAppendRow(["", ""])

		indexes                             = self.model_tools.indexesInRowByIdo(TOOLS.DESCRIPTION_INCLUDE)
		item_value : C20_StandardItem       = self.model_tools.itemFromIndex(indexes[1])
		item_value.setText(self._tools_description_include)

		indexes                             = self.model_tools.indexesInRowByIdo(TOOLS.DESCRIPTION_APPLIES)
		item_value : C20_StandardItem       = self.model_tools.itemFromIndex(indexes[1])
		item_value.setText(self._tools_description_applies)

	def LoadToolsDestinationToModel(self):
		""" Загрузка инструментов назначения в модель """
		if not self.model_tools.checkIdo(TOOLS.GROUP_DESTINATION):
			item_group = C20_StandardItem("ОБРАБОТКА НАЗНАЧЕНИЯ")
			item_group.setData(TOOLS.GROUP_DESTINATION, ROLES.IDO)
			item_group.setData(TOOLS.GROUP_DESTINATION, ROLES.GROUP)

			item_space = C20_StandardItem("")
			item_space.setData(TOOLS.GROUP_DESTINATION, ROLES.IDO)
			item_space.setData(TOOLS.GROUP_DESTINATION, ROLES.GROUP)

			self.model_tools.invisibleRootItem().appendRow([item_group, C20_StandardItem("")])

		item_group                          = self.model_tools.itemByData(TOOLS.GROUP_DESTINATION, ROLES.IDO)

		if not self.model_tools.checkIdo(TOOLS.DESTINATION_INCLUDE):
			item_field = C20_StandardItem("Назначение содержит")
			item_field.setData(TOOLS.DESTINATION_INCLUDE, ROLES.IDO)
			item_field.setData(TOOLS.GROUP_DESTINATION,   ROLES.GROUP)

			item_space = C20_StandardItem("")
			item_space.setData(TOOLS.DESTINATION_INCLUDE, ROLES.IDO)
			item_space.setData(TOOLS.GROUP_DESTINATION,   ROLES.GROUP)

			item_group.appendRow([item_field, item_space])

		if not self.model_tools.checkIdo(TOOLS.DESTINATION_APPLIES):
			item_field = C20_StandardItem("Применяется замена")
			item_field.setData(TOOLS.DESTINATION_APPLIES, ROLES.IDO)
			item_field.setData(TOOLS.GROUP_DESTINATION,       ROLES.GROUP)

			item_space = C20_StandardItem("")
			item_space.setData(TOOLS.DESTINATION_APPLIES, ROLES.IDO)
			item_space.setData(TOOLS.GROUP_DESTINATION,       ROLES.GROUP)

			item_group.appendRow([item_field, item_space])

			self.model_tools.fastAppendRow(["", ""])

		indexes                             = self.model_tools.indexesInRowByIdo(TOOLS.DESTINATION_INCLUDE)
		item_value : C20_StandardItem       = self.model_tools.itemFromIndex(indexes[1])
		item_value.setText(self._tools_destination_include)

		indexes                             = self.model_tools.indexesInRowByIdo(TOOLS.DESTINATION_APPLIES)
		item_value : C20_StandardItem       = self.model_tools.itemFromIndex(indexes[1])
		item_value.setText(self._tools_destination_applies)

	def LoadToolsLabelsToModel(self):
		""" Загрузка инструментов меток в модель """
		if not self.model_tools.checkIdo(TOOLS.GROUP_LABELS):
			item_group = C20_StandardItem("ОБРАБОТКА МЕТОК")
			item_group.setData(TOOLS.GROUP_LABELS, ROLES.IDO)
			item_group.setData(TOOLS.GROUP_LABELS, ROLES.GROUP)

			item_space = C20_StandardItem("")
			item_space.setData(TOOLS.GROUP_LABELS, ROLES.IDO)
			item_space.setData(TOOLS.GROUP_LABELS, ROLES.GROUP)

			self.model_tools.invisibleRootItem().appendRow([item_group, C20_StandardItem("")])

		item_group                          = self.model_tools.itemByData(TOOLS.GROUP_LABELS, ROLES.IDO)

		if not self.model_tools.checkIdo(TOOLS.LABELS_MODE):
			item_field = C20_StandardItem("Режим обработки")
			item_field.setData(TOOLS.LABELS_MODE, ROLES.IDO)
			item_field.setData(TOOLS.GROUP_LABELS,   ROLES.GROUP)

			item_space = C20_StandardItem("")
			item_space.setData(TOOLS.LABELS_MODE, ROLES.IDO)
			item_space.setData(TOOLS.GROUP_LABELS,   ROLES.GROUP)

			item_group.appendRow([item_field, item_space])

		if not self.model_tools.checkIdo(TOOLS.LABELS_INCLUDE):
			item_field = C20_StandardItem("Назначение содержит")
			item_field.setData(TOOLS.LABELS_INCLUDE, ROLES.IDO)
			item_field.setData(TOOLS.GROUP_LABELS,   ROLES.GROUP)

			item_space = C20_StandardItem("")
			item_space.setData(TOOLS.LABELS_INCLUDE, ROLES.IDO)
			item_space.setData(TOOLS.GROUP_LABELS,   ROLES.GROUP)

			item_group.appendRow([item_field, item_space])

		if not self.model_tools.checkIdo(TOOLS.LABELS_APPLIES):
			item_field = C20_StandardItem("Применяются метки")
			item_field.setData(TOOLS.LABELS_APPLIES, ROLES.IDO)
			item_field.setData(TOOLS.GROUP_LABELS,   ROLES.GROUP)

			item_space = C20_StandardItem("")
			item_space.setData(TOOLS.LABELS_APPLIES, ROLES.IDO)
			item_space.setData(TOOLS.GROUP_LABELS,   ROLES.GROUP)

			item_group.appendRow([item_field, item_space])

		indexes                             = self.model_tools.indexesInRowByIdo(TOOLS.LABELS_MODE)
		item_value : C20_StandardItem       = self.model_tools.itemFromIndex(indexes[1])
		item_value.setText(f"{self._tools_labels_mode.value}")

		indexes                             = self.model_tools.indexesInRowByIdo(TOOLS.LABELS_INCLUDE)
		item_title : C20_StandardItem       = self.model_tools.itemFromIndex(indexes[0])

		match self._tools_labels_mode:
			case MODES.REPLACE:	item_title.setText("Метки содержат")
			case MODES.APPEND :	item_title.setText("Назначение содержит")
			case MODES.EXPAND :	item_title.setText("Метки содержат")

		item_value : C20_StandardItem       = self.model_tools.itemFromIndex(indexes[1])
		item_value.setText('\n'.join(self._tools_labels_include))

		indexes                             = self.model_tools.indexesInRowByIdo(TOOLS.LABELS_APPLIES)
		item_value : C20_StandardItem       = self.model_tools.itemFromIndex(indexes[1])
		item_value.setText('\n'.join(self._tools_labels_applies))

	# Параметры
	def SwitchRuleTypesToDescription(self):
		""" Смена типа правил на Описание """
		self._processing_rule_types = RULES.REPLACE_DESCRIPTION

	def SwitchRuleTypesToDestination(self):
		""" Смена типа правил на Назначение """
		self._processing_rule_types = RULES.MATCH_DESTINATION

	def SwitchRuleTypesToLabels(self):
		""" Смена типа правил на Метки """
		self._processing_rule_types = RULES.DETECT_LABEL

	def ReadProcessingIdoFromTableRules(self):
		""" Чтение текущего IDO из таблицы правил """
		current_index = self.table_rules.currentIndex()
		self._processing_ido = current_index.data(ROLES.IDO)

	def ReadProcessingIdoFromWorkspace(self):
		""" Чтение текущего IDO из рабочего пространства """
		self._processing_ido = self.workspace.IdoRule()

	def WriteProcessingRuleToWorkspace(self):
		""" Запись правила обработки к рабочее пространство """
		self.workspace.IdoRule(self._processing_ido)

	def ReadProcessingToolFromTreeTools(self):
		""" Чтение текущего инструмента из дерева инструментов """
		current_index = self.tree_tools.currentIndex()
		self._processing_tool = current_index.data(ROLES.IDO)

	def SwitchProcessingLabelsModeToReplace(self):
		""" Переключение режима обработки меток на Замена """
		self._tools_labels_mode = MODES.REPLACE

	def SwitchProcessingLabelsModeToAppend(self):
		""" Переключение режима обработки меток на Добавление """
		self._tools_labels_mode = MODES.APPEND

	def SwitchProcessingLabelsModeToExpand(self):
		""" Переключение режима обработки меток на Расширение """
		self._tools_labels_mode = MODES.EXPAND

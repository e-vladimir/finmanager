# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui                  import QCursor
from PySide6.QtWidgets              import QHeaderView

from L00_form_processing_operations import TOOLS
from L60_form_processing_operations import C60_FormProcessingOperations
from L90_rules                      import C90_ProcessingRule


class C70_FormProcessingOperations(C60_FormProcessingOperations):
	""" Форма Обработка операций: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Обработка операций - {self.workspace.DmDyToString()}")

	# Вкладки
	def InitTabsMain(self):
		""" Настройка вкладок """
		self.tabs_main.setCurrentIndex(0)

	# Таблица правил
	def AdjustTableRules_Size(self):
		""" Таблица правил: Настройка размера """
		self.table_rules.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.table_rules.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

		self.table_rules.resizeRowsToContents()

	# Дерево инструментов
	def AdjustTreeTools_Size(self):
		""" Дерево инструментов: Настройка размера """
		self.tree_tools.resizeColumnToContents(0)

	def AdjustTreeTools_Expand(self):
		""" Дерево инструментов: Настройка раскрытия """
		self.tree_tools.expandAll()

	def AdjustTreeTools_Color(self):
		""" Дерево инструментов: Настройка цвета """
		self.model_tools.adjustGroupView(True, True, True)

	def ProcessingTreeTools_DbClick(self):
		""" Обработка двойного клика по дереву инструментов """
		match self._processing_tool:
			case TOOLS.DESCRIPTION_INCLUDE: self.on_RequestEditToolsDescriptionInclude()
			case TOOLS.DESCRIPTION_APPLIES: self.on_RequestEditToolsDescriptionApplies()

			case TOOLS.DESTINATION_INCLUDE: self.on_RequestEditToolsDestinationInclude()
			case TOOLS.DESTINATION_APPLIES: self.on_RequestEditToolsDestinationApplies()

	# Меню правила обработки
	def AdjustMenuRules_Enable(self):
		""" Меню правил обработки: Настройка доступности """
		flag_selected : bool = bool(self._processing_ido)

		self.action_rules_rule_open.setEnabled(flag_selected)
		self.action_rules_rule_delete.setEnabled(flag_selected)

	def AdjustMenuRules_Text(self):
		""" Меню правил обработки: Настройка текстов """
		self.submenu_rules_rules.setTitle(f"{self._processing_rule_types.value}")

		self.submenu_rules_rule.setTitle("Правило обработки")

		if self._processing_ido:
			rule         = C90_ProcessingRule(self._processing_ido)
			output : str = ', '.join(rule.OutputAsStrings())
			suffix : str = '...' if len(output) > 30 else ''
			self.submenu_rules_rule.setTitle(f"{output[:30]}{suffix}")

	def ShowMenuRules(self):
		""" Отображение меню правил обработки """
		self.menu_rules.exec_(QCursor().pos())

	# Меню инструменты
	def AdjustMenuTools_Enable(self):
		""" Меню инструментов обработки: Настройка доступности """
		flag_description : bool = bool(self._tools_description_include)
		self.action_tools_description_processing.setEnabled(flag_description)

		flag_destination : bool = bool(self._tools_destination_include)
		self.action_tools_destination_processing.setEnabled(flag_destination)

		flag_labels      : bool = bool(self._tools_labels_include)
		self.action_tools_labels_processing.setEnabled(flag_labels)

	def AdjustMenuTools_Text(self):
		""" Меню инструментов обработки: Настройка текстов """
		pass

	def ShowMenuTools(self):
		""" Отображение меню инструментов обработки """
		self.menu_tools.exec_(QCursor().pos())

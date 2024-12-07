# ФОРМА УПРАВЛЕНИЕ ОПИСАНИЕМ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui                import QCursor, Qt
from PySide6.QtWidgets            import QHeaderView, QListWidgetItem

from G30_cactus_datafilters       import C30_FilterLinear1D

from L00_containers               import CONTAINERS
from L60_form_control_description import C60_FormControlDescription
from L90_operations               import C90_Operation
from L90_rules                    import C90_ProcessingRule


class C70_FormControlDescription(C60_FormControlDescription):
	""" Форма Управление описанием: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Управление описанием операций - {self.workspace.DmDyToString()}")

	# Вкладки
	def SwitchTabsMainToFirst(self):
		""" Переключение вкладки на первую """
		self.tabs_main.setCurrentIndex(0)

	# Таблица правил
	def AdjustTableRules_Sizes(self):
		""" Таблица правил: Настройка размера """
		self.table_rules.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.table_rules.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

		self.table_rules.resizeRowsToContents()

	def AdjustTableRules_Sort(self):
		""" Таблица правил: Настройка сортировки """
		self.table_rules.sortByColumn(0, Qt.SortOrder.AscendingOrder)

	def ProcessingTableRules_DbClick(self):
		""" Обработка двойного клика по таблице правил """
		match self._processing_column:
			case 0: self.on_RequestEditInput()
			case 1: self.on_RequestEditOutput()

	# Меню правил автозамены описания
	def AdjustMenuRules_Enable(self):
		""" Меню автозамены описания: Настройка доступности """
		flag_selected : bool = bool(self._processing_ido)

		self.action_rules_rule_edit_input.setEnabled(flag_selected)
		self.action_rules_rule_edit_output.setEnabled(flag_selected)
		self.action_rules_rule_delete_rule.setEnabled(flag_selected)
		self.action_rules_rule_apply.setEnabled(flag_selected)

	def AdjustMenuRules_Text(self):
		""" Меню автозамены описания: Настройка текста """
		self.submenu_rules_rule.setTitle("Правило автозамены описания")

		if self._processing_ido:
			rule = C90_ProcessingRule(self._processing_ido)
			self.submenu_rules_rule.setTitle(rule.OutputAsString())

	def ShowMenuRules(self):
		""" Отображение меню правил автозамены описания """
		self.menu_rules.exec_(QCursor().pos())

	# Список доступных фрагментов
	def FillListControlReplaceAvailable(self):
		""" Загрузка списка доступных фрагментов """
		self.list_control_replace_available.clear()

		dy, dm                      = self.workspace.DyDm()

		operation                   = C90_Operation()
		idc             : str       = operation.Idc().data
		idp_dy          : str       = operation.f_dy.Idp().data
		idp_dm          : str       = operation.f_dm.Idp().data
		idp_description : str       = operation.f_description.Idp().data

		filter_operations           = C30_FilterLinear1D(idc)
		filter_operations.FilterIdpVlpByEqual(idp_dy, dy)
		filter_operations.FilterIdpVlpByEqual(idp_dm, dm)
		filter_operations.Capture(CONTAINERS.DISK)

		descriptions    : list[str] = filter_operations.ToStrings(idp_description, True, True).data

		subdescriptions : set[str]  = set()

		for description in descriptions:
			subdescriptions = subdescriptions.union(set(description.split(' ')))

		self.list_control_replace_available.addItems(descriptions)
		self.list_control_replace_available.addItems(sorted(list(subdescriptions)))

	# Список фрагментов поиска
	def ExtendEditControlReplaceInputFromAvailable(self):
		""" Расширение списка фрагментов поиска из доступных фрагментов """
		current_item : QListWidgetItem = self.list_control_replace_available.currentItem()
		self.edit_control_replace_input.appendPlainText(current_item.text())

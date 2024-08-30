# ФОРМА ФИНСТРУКТУРА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore     import Qt
from PySide6.QtGui      import QCursor

from L60_form_finstruct import C60_FormFinstruct


class C70_FormFinstruct(C60_FormFinstruct):
	""" Форма Финструктура: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Финструктура - {self.workspace.DmDyToString()}")

	# Дерево финструктуры
	def AdjustTreeDataSort(self):
		""" Настройка сортировки данных в дереве финструктуры """
		self.tree_data.sortByColumn(0, Qt.SortOrder.AscendingOrder)

	def AdjustTreeDataExpand(self):
		""" Настройка раскрытия данных в дереве финструктуры """
		self.tree_data.expandAll()

	def AdjustTreeDataColors(self):
		""" Настройка цветовой схемы дерева финструктуры """
		self.model_data.setGroupsView(True, True)

	def ProcessingTreeDataDbClick(self):
		""" Обработка двойного клика по дереву данных """
		if   self._name_processing : self.on_RequestRenameFinstructRecord()
		elif self._group_processing: self.on_RequestRenameGroupFinstruct()

	# Меню финструктуры
	def AdjustMenuFinstructEnable(self):
		""" Меню финсостава: Настройка доступности """
		flag_selected_group  : bool = bool(self._group_processing)
		self.menu_finstruct_group_create.setEnabled(flag_selected_group)
		self.menu_finstruct_group_rename.setEnabled(flag_selected_group)

		flag_selected_record : bool = bool(self._ido_processing)
		self.menu_finstruct_record_rename.setEnabled(flag_selected_record)
		self.menu_finstruct_record_regroup.setEnabled(flag_selected_record)
		self.menu_finstruct_record_delete.setEnabled(flag_selected_record)

	def AdjustMenuFinstructText(self):
		""" Меню финсостава: Настройка наименования """
		self.menu_finstruct_group_header.setTitle("Группа счетов" if not self._group_processing else self._group_processing)
		self.menu_finstruct_record_header.setTitle("Счёт" if not self._name_processing else self._name_processing)

	def ShowMenuFinstruct(self):
		""" Меню финсостава: Отображение """
		self.menu_finstruct.exec_(QCursor().pos())

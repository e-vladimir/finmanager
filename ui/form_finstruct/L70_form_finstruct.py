# ФОРМА ФИНСТРУКТУРА: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore     import Qt
from PySide6.QtGui      import QCursor
from PySide6.QtWidgets  import QHeaderView

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

	def AdjustTreeDataSize(self):
		""" Дерево данных: Настройка размера """
		self.tree_data.header().setStretchLastSection(False)
		self.tree_data.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

		for index_col in range(1, self.tree_data.header().count()): self.tree_data.setColumnWidth(index_col, 100)

	def AdjustTreeDataAlign(self):
		""" Дерево данных: Настройка выравнивания """
		for index_col in range(1, self.tree_data.header().count()):
			self.model_data.horizontalHeaderItem(index_col).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

	def ProcessingTreeDataDbClick(self):
		""" Обработка двойного клика по дереву данных """
		if self._processing_name :
			if self._processing_column == 1: self.on_RequestEditBalanceStartFinstructRecord()
			else                           : self.on_RequestRenameFinstructRecord()

		elif self._processing_group:
			self.on_RequestRenameGroupFinstruct()

	# Меню финструктуры
	def AdjustMenuFinstructEnable(self):
		""" Меню финсостава: Настройка доступности """
		flag_selected_group  : bool = bool(self._processing_group)
		self.menu_finstruct_group_create.setEnabled(flag_selected_group)
		self.menu_finstruct_group_rename.setEnabled(flag_selected_group)

		self.menu_finstruct_group_copy_next_dm.setEnabled(flag_selected_group)
		self.menu_finstruct_group_copy_prev_dm.setEnabled(flag_selected_group)

		flag_selected_record : bool = bool(self._processing_ido)
		self.menu_finstruct_record_rename.setEnabled(flag_selected_record)
		self.menu_finstruct_record_regroup.setEnabled(flag_selected_record)
		self.menu_finstruct_record_delete.setEnabled(flag_selected_record)

		self.menu_finstruct_record_edit_balance_start.setEnabled(flag_selected_record)

		self.menu_finstruct_record_copy_prev_dm.setEnabled(flag_selected_record)
		self.menu_finstruct_record_copy_next_dm.setEnabled(flag_selected_record)

	def AdjustMenuFinstructText(self):
		""" Меню финсостава: Настройка наименования """
		self.menu_finstruct_group_header.setTitle("Группа счетов" if not self._processing_group else self._processing_group)
		self.menu_finstruct_record_header.setTitle("Счёт" if not self._processing_name else self._processing_name)
		self.menu_finstruct_reset_by_dm.setText(f"Сброс финструктуры за {self.workspace.DmDyToString()}")

	def ShowMenuFinstruct(self):
		""" Меню финсостава: Отображение """
		self.menu_finstruct.exec_(QCursor().pos())

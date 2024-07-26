# ФОРМА ФИНСТРУКТУРЫ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore     import QModelIndex
from PySide6.QtGui      import QCursor, QStandardItem, QColor
from PySide6.QtWidgets  import QHeaderView

from L20_PySide6        import ROLE_OID
from L60_form_finstruct import C60_FormFinstruct
from L90_finstruct      import C90_RecordFinstruct


class C70_FormFinstruct(C60_FormFinstruct):
	""" Форма Финструктуры: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Финструктура  -  {self.workspace.DmDyToString()}")

	# Меню финструктуры
	def ShowMenuFinstruct(self):
		""" Отображение меню финструктуры """
		self.menu_finstruct.exec_(QCursor().pos())

	def AdjustMenuFinstructText(self):
		""" Настройка пунктов меню финструктуры """
		record_finstruct = C90_RecordFinstruct(self._ido_processing)

		self.menu_finstruct_record_header.setText(record_finstruct.Name())
		self.menu_finstruct_move_move_up.setText(f"Перенести {record_finstruct.Name()} выше")
		self.menu_finstruct_move_memory.setText(f"Запомнить {record_finstruct.Name()}")

		parent_name = ""
		if record_finstruct.ParentIdo():
			record_finstruct.Ido(record_finstruct.ParentIdo())
			parent_name = record_finstruct.Name()
		self.menu_finstruct_parent_header.setText(parent_name if parent_name else "Корневой уровень")

		record_finstruct = C90_RecordFinstruct(self._ido_memory)
		self.menu_finstruct_parent_paste.setText(f"Перенести {record_finstruct.Name()}")
		self.menu_finstruct_record_paste.setText(f"Перенести {record_finstruct.Name()}")

	def AdjustMenuFinstructEnable(self):
		""" Установка доступности меню финструктуры """
		record_finstruct          = C90_RecordFinstruct(self._ido_processing)

		flag_selected      : bool = bool(self._ido_processing)
		flag_exist_root    : bool = bool(record_finstruct.ParentIdo())
		flag_memory        : bool = bool(self._ido_memory)
		flag_memory_self   : bool = self._ido_memory == self._ido_processing
		flag_memory_parent : bool = self._ido_memory == record_finstruct.ParentIdo()

		self.menu_finstruct_parent_paste.setEnabled((flag_exist_root and flag_memory) and not flag_memory_parent)

		self.menu_finstruct_record_create.setEnabled(flag_selected)
		self.menu_finstruct_record_rename.setEnabled(flag_selected)
		self.menu_finstruct_record_delete.setEnabled(flag_selected)
		self.menu_finstruct_record_set_priority.setEnabled(flag_selected)

		self.menu_finstruct_move_move_up.setEnabled(flag_exist_root)
		self.menu_finstruct_move_memory.setEnabled(flag_selected)
		self.menu_finstruct_record_paste.setEnabled(flag_selected and flag_memory and not flag_memory_self)

		self.menu_finstruct_finperiod_prev.setEnabled(flag_selected)
		self.menu_finstruct_finperiod_next.setEnabled(flag_selected)

	# Дерево финструктуры
	def ShowPriorityRecord(self):
		""" Отображение приоритетной записи финструктуры """
		dy : int = self.workspace.Dy()
		dm : int = self.workspace.Dm()

		for ido in self.finstruct.IdosInDyDm(dy, dm):
			record_finstruct = C90_RecordFinstruct(ido)

			if not record_finstruct.Priority(): continue

			item_record : QStandardItem | None = self.model_data.itemByData(ido, ROLE_OID)
			item_record.setText(f"{record_finstruct.Name()} ★")

	def AdjustTreeDataExpand(self):
		""" Раскрытие дерева финструктуры """
		self.tree_data.expandAll()

	def AdjustTreeDataSize(self):
		""" Настройка размеров дерева финструктуры """
		self.tree_data.header().setSectionResizeMode(0, QHeaderView.Stretch)

		optimal_sizes : list[int] = [300] + [100] * 5

		for index_col, optimal_size in enumerate(optimal_sizes):
			if index_col == 0: continue

			self.tree_data.resizeColumnToContents(index_col)

			col_size : int = self.tree_data.columnWidth(index_col)
			col_size       = max(optimal_size, col_size)

			self.tree_data.setColumnWidth(index_col, col_size)

	def AdjustTreeDataColor(self):
		""" Раскраска дерева финструктуры """
		self.model_data.setGroupsView(False, True, False)

		color_red   = QColor(200,  60,  60)
		color_black = QColor(  0,   0,   0)

		for index_record in self.model_data.indexes():
			index_row            : int           = index_record.row()
			index_parent         : QModelIndex   = index_record.parent()
			item_parent          : QStandardItem = self.model_data.invisibleRootItem() if not index_parent.isValid() else self.model_data.itemFromIndex(index_parent)

			item_remains_initial : QStandardItem = item_parent.child(index_row, 1)
			item_remains_final   : QStandardItem = item_parent.child(index_row, 2)
			item_remains_delta   : QStandardItem = item_parent.child(index_row, 3)

			item_remains_initial.setForeground(color_red if '-' in item_remains_initial.data() else color_black)
			item_remains_final.setForeground(color_red if '-' in item_remains_final.data() else color_black)
			item_remains_delta.setForeground(color_red if '-' in item_remains_delta.data() else color_black)

	def RequestEditRecord(self):
		""" Запрос на редактирование записи финструктуры """
		if   self._col_processing == 0: self.on_RequestRenameRecord()
		elif self._col_processing == 1: self.on_RequestEditRemainInitial()

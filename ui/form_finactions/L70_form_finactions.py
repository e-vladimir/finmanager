# ФОРМА ФИНДЕЙСТВИЯ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui       import QCursor

from G10_math_linear     import CalcBetween
from G11_convertor_data  import AmountToString

from L00_months          import MONTHS_SHORT
from L60_form_finactions import C60_FormFinactions
from L90_finactions      import C90_FinactionsRecord


class C70_FormFinactions(C60_FormFinactions):
	""" Форма Финдействия: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Финдействия - {self.workspace.DmDyToString()}")

	# Меню финдействий
	def AdjustMenuFinactionsEnable(self):
		""" Меню финдействий: Настройка доступности """
		flag_selected_single   : bool = bool(self._processing_ido)
		flag_selected_multiple : bool = len(self._processing_idos) > 0

		self.menu_finactions_record_open.setEnabled(flag_selected_single)
		self.menu_finactions_record_delete.setEnabled(flag_selected_single)
		self.menu_finactions_record_edit_note.setEnabled(flag_selected_single)
		self.menu_finactions_record_split.setEnabled(flag_selected_single)

		self.menu_finactions_colors_black.setEnabled(flag_selected_single or flag_selected_multiple)
		self.menu_finactions_colors_gray.setEnabled(flag_selected_single or flag_selected_multiple)
		self.menu_finactions_colors_blue.setEnabled(flag_selected_single or flag_selected_multiple)
		self.menu_finactions_colors_green.setEnabled(flag_selected_single or flag_selected_multiple)
		self.menu_finactions_colors_red.setEnabled(flag_selected_single or flag_selected_multiple)

		self.menu_finactions_pack_reset.setEnabled(flag_selected_multiple)

		self.menu_finactions_rules_apply.setEnabled(flag_selected_single or flag_selected_multiple)

	def AdjustMenuFinactionsText(self):
		""" Меню финдействий: Настройка наименования """
		self.menu_finactions_record_header.setTitle("Запись финдействий")

		if self._processing_ido:
			record       = C90_FinactionsRecord(self._processing_ido)
			dm     : str = MONTHS_SHORT[self.workspace.Dm()]
			dd_name: str = f"{record.Dd():02d} {dm}"

			self.menu_finactions_record_header.setTitle(f"{AmountToString(record.Amount(), False, True)} от {dd_name}")

		self.menu_finactions_pack_header.setTitle("Пакетный режим")
		if self._processing_idos:
			self.menu_finactions_pack_header.setTitle(f"Пакетный режим ({len(self._processing_idos)})")

		self.menu_finactions_reset_by_dm.setText(f"Сброс финдействий за {self.workspace.DmDyToString()}")

	def ShowMenuFinactions(self):
		""" Меню финдействий: Отображение """
		self.menu_finactions.exec_(QCursor().pos())

	# Дерево данных
	def AdjustTreeData_Size(self):
		""" Дерево данных: Настройка размера """
		sizes_min : list[int] = [100, 200, 300]
		sizes_max : list[int] = [150, 200, 500]

		for index_col in range(self.model_data.columnCount() - 1):
			self.tree_data.resizeColumnToContents(index_col)

			col_size : int = self.tree_data.columnWidth(index_col)
			col_size       = CalcBetween(sizes_min[index_col], col_size, sizes_max[index_col])

			self.tree_data.setColumnWidth(index_col, col_size)

	def AdjustTreeData_Expand(self):
		""" Дерево данных: Настройка раскрытия """
		self.tree_data.expandAll()

	def AdjustTreeData_Color(self):
		""" Дерево данных: Настройка цветовой палитры """
		self.model_data.setGroupsView(True, True, True)

	def ProcessingTreeData_DbClick(self):
		""" Обработка двойного клика по дереву данных """
		match self._processing_column:
			case 0: self.on_RequestOpenFinactionsRecord()
			case 1: self.on_RequestOpenFinactionsRecord()
			case 2: self.on_RequestEditNoteFinactionsRecord()
			case 3: self.on_RequestOpenFinactionsRecord()

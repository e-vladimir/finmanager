# ФОРМА ФИНАНСОВЫЕ ОПЕРАЦИИ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui       import QCursor, Qt
from PySide6.QtWidgets   import QHeaderView

from G10_math_linear     import CalcBetween
from G11_convertor_data  import AmountToString

from L20_PySide6         import ROLES
from L60_form_operations import C60_FormOperations
from L90_operations      import C90_Operation


class C70_FormOperations(C60_FormOperations):
	""" Форма Финансовые операции: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Финансовые операции - {self.workspace.DmDyToString()}")

	# Дерево данных
	def ProcessingTreeDataDbClick(self):
		""" Обработка двойного нажатия на дереве данных """
		if not self._processing_ido: return

		match self._processing_column:
			case 0: self.on_RequestOpenOperation()
			case 2: self.on_RequestSetOperationObjectExt()
			case 3: self.on_RequestSetOperationObjectInt()
			case 4: self.on_RequestSetOperationDestination()

	def AdjustTreeData_Size(self):
		""" Настройка дерева данных: Размеры """
		sizes_min : list[int] = [ 75,
		                          200,
		                          100,
		                          100]

		sizes_max : list[int] = [    150,
		                         max(200, self.width() // 5),
		                         max(200, self.width() // 5),
		                         max(200, self.width() // 5)]

		for index_col in range(self.model_data.columnCount() - 1):
			self.tree_data.resizeColumnToContents(index_col)

			column_size : int = self.tree_data.columnWidth(index_col)
			column_size       = CalcBetween(sizes_min[index_col], column_size, sizes_max[index_col])

			self.tree_data.setColumnWidth(index_col, column_size)

		self.tree_data.header().setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

	def AdjustTreeData_Color(self):
		""" Настройка дерева данных: Цвета """
		self.model_data.adjustGroupView(True, True, True)

	def AdjustTreeData_Expand(self):
		""" Настройка дерева данных: Раскрытие """
		self.tree_data.expandAll()

	def AdjustTreeData_Sort(self):
		""" Настройка дерева данных: Сортировка """
		self.model_data.setSortRole(ROLES.SORT_INDEX)
		self.model_data.sort(0, Qt.SortOrder.AscendingOrder)

	# Меню Финансовые операции
	def AdjustMenuOperations_Text(self):
		""" Меню операций по счетам: Настройка текста """
		self.submenu_operation.setTitle("Операция")
		self.submenu_operations_pack.setTitle("Пакет операций")

		if self._processing_ido:
			operation = C90_Operation(self._processing_ido)
			self.submenu_operation.setTitle(f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}")

		if self._processing_idos:
			self.submenu_operations_pack.setTitle(f"Пакет операций: {len(self._processing_idos)}")

	def AdjustMenuOperations_Enable(self):
		""" Меню операций по счетам: Настройка доступности """
		flag_selected_operation : bool = bool(self._processing_ido)
		flag_selected_pack      : bool = len(self._processing_idos) > 0

		self.action_operation_open_operation.setEnabled(flag_selected_operation)
		self.action_operation_delete_operation.setEnabled(flag_selected_operation)

		self.action_operations_pack_clear_selection.setEnabled(flag_selected_pack)
		self.action_operations_pack_collapse_selection.setEnabled(flag_selected_pack)
		self.action_operations_pack_delete_pack.setEnabled(flag_selected_pack)

		self.action_operation_split.setEnabled(flag_selected_operation)
		self.action_operation_set_description.setEnabled(flag_selected_operation)
		self.action_operation_set_destination.setEnabled(flag_selected_operation)
		self.action_operation_set_object_int.setEnabled(flag_selected_operation)
		self.action_operation_set_object_ext.setEnabled(flag_selected_operation)

		self.submenu_operation_colors.setEnabled(flag_selected_operation)

	def ShowMenuOperations(self):
		""" Меню операций по счетам: Отображение """
		self.menu_operations.exec_(QCursor().pos())

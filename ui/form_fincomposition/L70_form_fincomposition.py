# ФОРМА ФИНСОСТАВ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore          import Qt
from PySide6.QtGui           import QCursor

from L60_form_fincomposition import C60_FormFincomposition
from L90_fincomposition      import C90_FincompositionRecord


class C70_FormFincomposition(C60_FormFincomposition):
	""" Форма Финсостав: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Форма: Отображение заголовка окна """
		self.setWindowTitle("Финсостав")

	# Меню финсостава
	def AdjustMenuFincompositionEnable(self):
		""" Меню финсостава: Настройка доступности """
		flag_selected : bool = bool(self._ido_processing)

		self.menu_fincomposition_record_create.setEnabled(flag_selected)
		self.menu_fincomposition_record_rename.setEnabled(flag_selected)
		self.menu_fincomposition_record_delete.setEnabled(flag_selected)

	def AdjustMenuFincompositionText(self):
		""" Меню финсостава: Настройка наименования """
		self.menu_fincomposition_record_header.setText("ЗАПИСЬ ФИНСОСТАВА")

		if not self._ido_processing: return
		record_fincomposition = C90_FincompositionRecord(self._ido_processing)
		self.menu_fincomposition_record_header.setText(record_fincomposition.Name().upper())

	def ShowMenuFincomposition(self):
		""" Меню финсостава: Отображение """
		self.menu_fincomposition.exec_(QCursor().pos())

	# Дерево финсостава
	def AdjustTreeDataSort(self):
		""" Настройка сортировки данных в дереве финсостава """
		self.tree_data.sortByColumn(0, Qt.SortOrder.AscendingOrder)

	def AdjustTreeDataExpand(self):
		""" Настройка раскрытия данных в дереве финсостава """
		self.tree_data.expandAll()

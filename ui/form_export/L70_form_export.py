# ФОРМА ЭКСПОРТ ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui     import QCursor

from L00_struct_export import EXPORT_ID
from L60_form_export   import C60_FormExport


class C70_FormExport(C60_FormExport):
	""" Форма Экспорт данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Экспорт данных - {self.workspace.DmDyToString()}")

	# Дерево данных
	def AdjustTreeDataOperations_Color(self):
		""" Дерево операций: Настройка цвета """
		self.model_operations.adjustGroupView(True, True, True)

	def AdjustTreeDataOperations_Expand(self):
		""" Дерево операций: Настройка раскрытия """
		self.tree_data_operations.expandAll()

	def AdjustTreeDataOperations_Size(self):
		""" Дерево операций: Настройка размера """
		self.tree_data_operations.resizeColumnToContents(0)

	def ProcessingTreeDataOperations_DbClick(self):
		""" Обработка двойного клика по дереву данных Финансовых операций """
		match self._processing_ido:
			case EXPORT_ID.MODE_DATE: self.on_RequestSetDateInOperations()
			case EXPORT_ID.ACCOUNT  : self.on_RequestSetAccountInOperations()
			case EXPORT_ID.DIRECTORY: self.on_RequestSetPathInOperations()

	# Меню экспорта финансовых операций
	def AdjustMenuOperations_Enable(self):
		""" Меню экспорта финансовых операций: Настройка доступности """
		flag_exist : bool = bool(self._operations_output_files)

		self.action_operations_exec_export.setEnabled(flag_exist)

	def AdjustMenuOperations_Text(self):
		""" Меню экспорта финансовых операций: Настройка текста """
		pass

	def ShowMenuOperations(self):
		""" Отображение меню импорта финансовых операций """
		self.menu_operations.exec_(QCursor().pos())

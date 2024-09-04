# ФОРМА ИМПОРТ ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui   import QCursor, Qt

from L60_form_import import C60_FormImport


class C70_FormImport(C60_FormImport):
	""" Форма Импорт данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle("Импорт данных")

	# Вкладка Финдействия
	def AdjustPageFinactions_Text(self):
		""" Вкладка Импорт финдействий: Настройка текста """
		filename : str = ""
		if self._import_finactions_filepath.is_file(): filename += f"({self._import_finactions_filepath.name})"

		self.tabs_main.setTabText(0, f"Финдействия {filename}")

	# Меню импорта финдействий
	def AdjustMenuImportFinactions_Enable(self):
		""" Меню импорта финдействий: Настройка доступности """
		flag_selected : bool = self._processing_column >= 0
		self.menu_import_finactions_column_set_field.setEnabled(flag_selected)
		self.menu_import_finactions_column_reset_field.setEnabled(flag_selected)

		flag_data     : bool = len(self._import_finactions_data) > 0
		self.menu_import_finactions_exec_import.setEnabled(flag_data)

	def AdjustMenuImportFinactions_Text(self):
		""" Меню импорта финдействий: Настройка наименований """
		self.menu_import_finactions_column_header.setTitle("Колонка данных")

		if not self._processing_name: return

		self.menu_import_finactions_column_header.setTitle(self._processing_name)

	def ShowMenuImportFinactions(self):
		""" Меню импорта финдействий: Отображение"""
		self.menu_import_finactions.exec_(QCursor().pos())

	# Таблица данных импорта финдействий
	def AdjustTableImportFinactionsData_Size(self):
		""" Таблица данных импорта финдействий: Настройка размеров """
		self.table_import_finactions_data.resizeColumnsToContents()

		for index_row in range(self.model_import_finactions_data.rowCount()):
			self.table_import_finactions_data.setRowHeight(index_row, 22)

	def AdjustTableImportFinactionsData_Color(self):
		""" Таблица данных импорта финдействий: Настройка цветов """
		item_root = self.model_import_finactions_data.invisibleRootItem()

		for index_row in range(self.model_import_finactions_data.rowCount()):
			self.model_import_finactions_data.setRowColor(item_root, index_row, Qt.GlobalColor.white, Qt.GlobalColor.gray)

		for index_col in self._import_finactions_header.keys():
			self.model_import_finactions_data.setColColor(item_root, index_col, Qt.GlobalColor.white, Qt.GlobalColor.black)

# ФОРМА ИМПОРТ ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui   import QCursor

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
		pass

	def AdjustMenuImportFinactions_Text(self):
		""" Меню импорта финдействий: Настройка наименований """
		pass

	def ShowMenuImportFinactions(self):
		""" Меню импорта финдействий: Отображение"""
		self.menu_import_finactions.exec_(QCursor().pos())

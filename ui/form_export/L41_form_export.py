# ФОРМА ЭКСПОРТ ДАННЫХ: МОДЕЛЬ UI

from PySide6.QtGui     import QIcon, QAction
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_export   import Ui_form_export


class C41_FormExport(C20_PySideForm, Ui_form_export):
	""" Форма Экспорт данных: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuExportFinactions()

	def InitMenuExportFinactions(self):
		""" Инициализацию меню финсостава """
		icon_open      = QIcon("./ui/icons/open.svg")
		icon_list      = QIcon("./ui/icons/list.svg")
		icon_upload    = QIcon("./ui/icons/upload.svg")
		icon_grid_33   = QIcon("./ui/icons/grid_3_3.svg")
		icon_grid_22   = QIcon("./ui/icons/grid_2_2.svg")
		icon_grid_13   = QIcon("./ui/icons/grid_1_3.svg")

		self.menu_export_finactions                          = QMenu()
		self.menu_export_finactions_period_mode    : QAction = self.menu_export_finactions.addAction(icon_grid_13, "Режим выборки периода экспорта")
		self.menu_export_finactions_period_dy      : QAction = self.menu_export_finactions.addAction(icon_grid_22, "Год экспорта")
		self.menu_export_finactions_period_dm      : QAction = self.menu_export_finactions.addAction(icon_grid_33, "Месяц экспорта")
		self.menu_export_finactions.addSeparator()

		self.menu_export_finactions_finstruct_mode : QAction = self.menu_export_finactions.addAction(icon_grid_13, "Режим выборки счетов")
		self.menu_export_finactions_finstruct_name : QAction = self.menu_export_finactions.addAction(icon_list,    "Счёт экспорта")
		self.menu_export_finactions.addSeparator()

		self.menu_export_finactions_folder         : QAction = self.menu_export_finactions.addAction(icon_open,    "Директория экспорта")
		self.menu_export_finactions.addSeparator()

		self.menu_export_finactions_exec_export    : QAction = self.menu_export_finactions.addAction(icon_upload,  "Выполнить экспорт")

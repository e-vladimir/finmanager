# ФОРМА ЭКСПОРТ ДАННЫХ: МОДЕЛЬ UI

from PySide6.QtGui     import QIcon, QAction
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_export   import Ui_frm_export


class C41_FormExport(C20_PySideForm, Ui_frm_export):
	""" Форма Экспорт данных: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuOperations()

	def InitMenuOperations(self):
		""" Инициализация меню Финансовые операции """
		icon_arrow_up                                      = QIcon("./L0/icons/arrow_up.svg")
		icon_edit                                          = QIcon("./L0/icons/edit.svg")
		icon_upload                                        = QIcon("./L0/icons/upload.svg")

		self.menu_operations                               = QMenu("Финансовые операции")

		self.submenu_operations_input                      = self.menu_operations.addMenu(icon_arrow_up, "Параметры выборки данных")
		self.action_operations_input_set_date    : QAction = self.submenu_operations_input.addAction(icon_edit,  "Указать период")
		self.action_operations_input_set_account : QAction = self.submenu_operations_input.addAction(icon_edit,  "Указать счет")

		self.submenu_operations_output                     = self.menu_operations.addMenu(icon_arrow_up, "Параметры экспорта данных")
		self.action_operations_output_set_path   : QAction = self.submenu_operations_output.addAction(icon_edit, "Указать директорию")

		self.menu_operations.addSeparator()
		self.action_operations_exec_export       : QAction = self.menu_operations.addAction(icon_upload, "Выполнить экспорт данных")

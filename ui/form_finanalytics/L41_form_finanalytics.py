# ФОРМА ФИНАНАЛИЗ: МОДЕЛЬ UI

from PySide6.QtGui         import QIcon, QAction
from PySide6.QtWidgets     import QMenu

from L20_PySide6           import C20_PySideForm
from L40_form_finanalytics import Ui_form_finanalytics


class C41_FormFinanalytics(C20_PySideForm, Ui_form_finanalytics):
	""" Форма Финанализ: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuFindescription()

	def InitMenuFindescription(self):
		""" Меню финсостава """
		icon_delete = QIcon("./ui/icons/item_delete.svg")
		icon_plus   = QIcon("./ui/icons/item_plus.svg")

		self.menu_findescription_dynamic                         = QMenu(self.table_findescription_dynamic)

		self.menu_findescription_dynamic_header        : QAction = self.menu_findescription_dynamic.addSection("Финсостав")
		self.menu_findescription_dynamic_inc           : QAction = self.menu_findescription_dynamic.addAction(icon_plus, "Расширить анализ финсостава")

		self.menu_findescription_dynamic_record_header : QAction = self.menu_findescription_dynamic.addSection("Запись финсостава")
		self.menu_findescription_dynamic_record_dec    : QAction = self.menu_findescription_dynamic.addAction(icon_delete, "Убрать из анализа")

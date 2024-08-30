# ФОРМА ФИНСОСТАВ: МОДЕЛЬ UI

from PySide6.QtGui           import QAction, QIcon
from PySide6.QtWidgets       import QMenu

from L20_PySide6             import C20_PySideForm
from L40_form_fincomposition import Ui_frm_fincomposition


class C41_FormFincomposition(C20_PySideForm, Ui_frm_fincomposition):
	""" Форма Финсостав: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuFincomposition()

	def InitMenuFincomposition(self):
		""" Инициализацию меню финсостава """
		icon_plus   = QIcon("./ui/icons/item_plus.svg")
		icon_edit   = QIcon("./ui/icons/edit.svg")
		icon_delete = QIcon("./ui/icons/item_delete.svg")
		icon_up     = QIcon("./ui/icons/arrow_up.svg")
		icon_copy   = QIcon("./ui/icons/copy.svg")
		icon_paste  = QIcon("./ui/icons/paste.svg")

		self.menu_fincomposition = QMenu()
		self.menu_fincomposition_header        : QAction = self.menu_fincomposition.addSection("ФИНСОСТАВ")
		self.menu_fincomposition_create        : QAction = self.menu_fincomposition.addAction(icon_plus,   "Создать")

		self.menu_fincomposition_record_header : QAction = self.menu_fincomposition.addSection("ЗАПИСЬ ФИНСОСТАВА")
		self.menu_fincomposition_record_create : QAction = self.menu_fincomposition.addAction(icon_plus,   "Создать внутри")
		self.menu_fincomposition_record_rename : QAction = self.menu_fincomposition.addAction(icon_edit,   "Переименовать")
		self.menu_fincomposition_record_delete : QAction = self.menu_fincomposition.addAction(icon_delete, "Удалить")
		self.menu_fincomposition_record_up     : QAction = self.menu_fincomposition.addAction(icon_up,     "Перенести уровнем выше")
		self.menu_fincomposition_record_copy   : QAction = self.menu_fincomposition.addAction(icon_copy,   "Копировать")
		self.menu_fincomposition_record_paste  : QAction = self.menu_fincomposition.addAction(icon_paste,  "Вставить")

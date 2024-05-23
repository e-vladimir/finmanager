# ФОРМА ФИНСОСТАВА: МОДЕЛЬ UI

from PySide6.QtGui           import QIcon, QAction
from PySide6.QtWidgets       import QMenu

from L20_PySide6             import C20_PySideForm
from L40_form_findescription import Ui_frm_findescription


class C41_FormFindescription(C20_PySideForm, Ui_frm_findescription):
	""" Форма Финсостав: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuFindescription()

	def InitMenuFindescription(self):
		""" Меню финсостава """
		icon_copy   = QIcon("./ui/icons/copy.svg")
		icon_delete = QIcon("./ui/icons/item_delete.svg")
		icon_edit   = QIcon("./ui/icons/edit.svg")
		icon_paste  = QIcon("./ui/icons/paste.svg")
		icon_plus   = QIcon("./ui/icons/item_plus.svg")
		icon_up     = QIcon("./ui/icons/arrow_up.svg")

		self.mnu_findescription                         = QMenu(self.tre_findescription)

		self.mnu_findescription_parent_header : QAction = self.mnu_findescription.addSection("Корневой уровень")
		self.mnu_findescription_parent_create : QAction = self.mnu_findescription.addAction(icon_plus, "Создать запись финсостава")
		self.mnu_findescription_parent_paste  : QAction = self.mnu_findescription.addAction(icon_paste, "Перенести")

		self.mnu_findescription_record_header : QAction = self.mnu_findescription.addSection("Запись финсостава")
		self.mnu_findescription_record_create : QAction = self.mnu_findescription.addAction(icon_plus,   "Создать запись финсостава")
		self.mnu_findescription_record_rename : QAction = self.mnu_findescription.addAction(icon_edit,   "Редактировать")
		self.mnu_findescription_record_delete : QAction = self.mnu_findescription.addAction(icon_delete, "Удалить")
		self.mnu_findescription_record_paste  : QAction = self.mnu_findescription.addAction(icon_paste,  "Перенести")

		self.mnu_findescription_move_header   : QAction = self.mnu_findescription.addSection("Управление структурой")
		self.mnu_findescription_move_up       : QAction = self.mnu_findescription.addAction(icon_up,   "Перенести выше")
		self.mnu_findescription_move_memory   : QAction = self.mnu_findescription.addAction(icon_copy, "Запомнить")

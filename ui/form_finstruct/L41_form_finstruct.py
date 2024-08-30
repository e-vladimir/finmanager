# ФОРМА ФИНСТРУКТУРА: МОДЕЛЬ UI

from PySide6.QtGui      import QIcon, QAction
from PySide6.QtWidgets  import QMenu

from L20_PySide6        import C20_PySideForm
from L40_form_finstruct import Ui_frm_finstruct


class C41_FormFinstruct(C20_PySideForm, Ui_frm_finstruct):
	""" Форма Финструктура: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuFinstruct()

	def InitMenuFinstruct(self):
		""" Инициализацию меню финсостава """
		icon_plus   = QIcon("./ui/icons/item_plus.svg")
		icon_edit   = QIcon("./ui/icons/edit.svg")
		icon_delete = QIcon("./ui/icons/item_delete.svg")

		self.menu_finstruct                          = QMenu()
		self.menu_finstruct_header         : QAction = self.menu_finstruct.addSection("ФИНСТРУКТУРА")
		self.menu_finstruct_create         : QAction = self.menu_finstruct.addAction(icon_plus,   "Создать счёт")

		self.menu_finstruct_group_header   : QAction = self.menu_finstruct.addSection("ГРУППА СЧЕТОВ")
		self.menu_finstruct_group_create   : QAction = self.menu_finstruct.addAction(icon_plus,   "Создать подсчёт")
		self.menu_finstruct_group_rename   : QAction = self.menu_finstruct.addAction(icon_edit,   "Переименовать")

		self.menu_finstruct_record_header  : QAction = self.menu_finstruct.addSection("СЧЕТ")
		self.menu_finstruct_record_rename  : QAction = self.menu_finstruct.addAction(icon_edit,   "Переименовать")
		self.menu_finstruct_record_regroup : QAction = self.menu_finstruct.addAction(icon_edit,   "Изменить группу")
		self.menu_finstruct_record_delete  : QAction = self.menu_finstruct.addAction(icon_delete, "Удалить счёт")

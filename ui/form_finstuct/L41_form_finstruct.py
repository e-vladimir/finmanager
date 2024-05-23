# ФОРМА ФИНСТРУКТУРЫ: МОДЕЛЬ UI

from PySide6.QtGui      import QIcon, QAction
from PySide6.QtWidgets  import QMenu

from L20_PySide6        import C20_PySideForm
from L40_form_finstruct import Ui_form_finstruct


class C41_FormFinstruct(C20_PySideForm, Ui_form_finstruct):
	""" Форма Финструктуры: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuFinstruct()

	def InitMenuFinstruct(self):
		""" Меню финструктуры """

		icon_copy   = QIcon("./ui/icons/copy.svg")
		icon_plus   = QIcon("./ui/icons/item_plus.svg")
		icon_remove = QIcon("./ui/icons/item_delete.svg")
		icon_edit   = QIcon("./ui/icons/edit.svg")
		icon_paste  = QIcon("./ui/icons/paste.svg")
		icon_up     = QIcon("./ui/icons/arrow_up.svg")
		icon_left   = QIcon("./ui/icons/arrow_left_2.svg")
		icon_right  = QIcon("./ui/icons/arrow_right_2.svg")
		icon_star   = QIcon("./ui/icons/star.svg")

		self.menu_finstruct                               = QMenu(None)
		self.menu_finstruct_parent_header       : QAction = self.menu_finstruct.addSection("Корневой уровень")
		self.menu_finstruct_parent_create       : QAction = self.menu_finstruct.addAction(icon_plus,  "Создать запись финструктуры")
		self.menu_finstruct_parent_paste        : QAction = self.menu_finstruct.addAction(icon_paste, "Переместить запись")

		self.menu_finstruct_record_header       : QAction = self.menu_finstruct.addSection("Запись финструктуры")
		self.menu_finstruct_record_create       : QAction = self.menu_finstruct.addAction(icon_plus,  "Создать запись финструктуры")
		self.menu_finstruct_record_rename       : QAction = self.menu_finstruct.addAction(icon_edit,  "Переименовать")
		self.menu_finstruct_record_delete       : QAction = self.menu_finstruct.addAction(icon_remove, "Удалить")
		self.menu_finstruct_record_set_priority : QAction = self.menu_finstruct.addAction(icon_star,  "Установить по-умолчанию")
		self.menu_finstruct_record_paste        : QAction = self.menu_finstruct.addAction(icon_paste, "Переместить запись")

		self.menu_finstruct_move_header         : QAction = self.menu_finstruct.addSection("Управление структурой")
		self.menu_finstruct_move_move_up        : QAction = self.menu_finstruct.addAction(icon_up,    "Переместить запись выше")
		self.menu_finstruct_move_memory         : QAction = self.menu_finstruct.addAction(icon_copy,  "Запомнить запись")

		self.menu_finstruct_finperiod_header    : QAction = self.menu_finstruct.addSection("Перемещение в финпериоде")
		self.menu_finstruct_finperiod_prev      : QAction = self.menu_finstruct.addAction(icon_left,  "Переместить в предыдущий период")
		self.menu_finstruct_finperiod_next      : QAction = self.menu_finstruct.addAction(icon_right, "Переместить в следующий период")

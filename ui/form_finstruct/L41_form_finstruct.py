# ФОРМА ФИНСТРУКТУРА: МОДЕЛЬ UI

from PySide6.QtGui      import QIcon, QAction
from PySide6.QtWidgets  import QMenu

from L20_PySide6        import C20_PySideForm
from L40_form_finstruct import Ui_form_finstruct


class C41_FormFinstruct(C20_PySideForm, Ui_form_finstruct):
	""" Форма Финструктура: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuFinstruct()

	def InitMenuFinstruct(self):
		""" Инициализацию меню финсостава """
		icon_plus      = QIcon("./ui/icons/item_plus.svg")
		icon_edit      = QIcon("./ui/icons/edit.svg")
		icon_delete    = QIcon("./ui/icons/item_delete.svg")
		icon_blocks    = QIcon("./ui/icons/blocks.svg")
		icon_grid_22   = QIcon("./ui/icons/grid_2_2.svg")
		icon_grid_33   = QIcon("./ui/icons/grid_3_3.svg")
		icon_arrow_l_1 = QIcon("./ui/icons/arrow_left.svg")
		icon_arrow_r_1 = QIcon("./ui/icons/arrow_right.svg")

		self.menu_finstruct                                     = QMenu()
		self.menu_finstruct_header                    : QMenu   = self.menu_finstruct.addMenu(icon_grid_22, "Финструктура")
		self.menu_finstruct_create                    : QAction = self.menu_finstruct_header.addAction(icon_plus,   "Создать счёт")

		self.menu_finstruct_group_header              : QMenu   = self.menu_finstruct.addMenu(icon_blocks, "Группа счетов")
		self.menu_finstruct_group_create              : QAction = self.menu_finstruct_group_header.addAction(icon_plus,   "Создать счёт")
		self.menu_finstruct_group_rename              : QAction = self.menu_finstruct_group_header.addAction(icon_edit,   "Переименовать")

		self.menu_finstruct_record_header             : QMenu   = self.menu_finstruct.addMenu(icon_grid_33, "Счёт")
		self.menu_finstruct_record_rename             : QAction = self.menu_finstruct_record_header.addAction(icon_edit,   "Переименовать")
		self.menu_finstruct_record_regroup            : QAction = self.menu_finstruct_record_header.addAction(icon_blocks, "Изменить группу")
		self.menu_finstruct_record_delete             : QAction = self.menu_finstruct_record_header.addAction(icon_delete, "Удалить")
		self.menu_finstruct_record_header.addSeparator()
		self.menu_finstruct_record_edit_balance_start : QAction = self.menu_finstruct_record_header.addAction(icon_edit,   "Установить баланс начальный")
		self.menu_finstruct_record_header.addSeparator()
		self.menu_finstruct_record_copy_prev_dm       : QAction = self.menu_finstruct_record_header.addAction(icon_arrow_l_1, "Перенести в предыдущий месяц")
		self.menu_finstruct_record_copy_next_dm       : QAction = self.menu_finstruct_record_header.addAction(icon_arrow_r_1, "Перенести в следующий месяц")

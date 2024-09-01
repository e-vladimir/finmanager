# ФОРМА ФИНДЕЙСТВИЯ: МОДЕЛЬ UI

from PySide6.QtGui       import QIcon, QAction
from PySide6.QtWidgets   import QMenu

from L20_PySide6         import C20_PySideForm
from L40_form_finactions import Ui_frm_finactions


class C41_FormFinactions(C20_PySideForm, Ui_frm_finactions):
	""" Форма Финдействия: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuFinstruct()

	def InitMenuFinstruct(self):
		""" Инициализацию меню финсостава """
		icon_plus      = QIcon("./ui/icons/item_plus.svg")
		icon_open      = QIcon("./ui/icons/open.svg")
		icon_edit      = QIcon("./ui/icons/edit.svg")
		icon_delete    = QIcon("./ui/icons/item_delete.svg")
		icon_grid_22   = QIcon("./ui/icons/grid_2_2.svg")
		icon_grid_33   = QIcon("./ui/icons/grid_3_3.svg")
		icon_arrow_l_r = QIcon("./ui/icons/arrow_left_right.svg")

		self.menu_finactions                            = QMenu()
		self.menu_finactions_header           : QMenu   = self.menu_finactions.addMenu(icon_grid_22, "Финдействия")
		self.menu_finactions_create           : QAction = self.menu_finactions_header.addAction(icon_plus, "Создать запись")

		self.menu_finactions_record_header    : QMenu   = self.menu_finactions.addMenu(icon_grid_33, "Запись финдействий")
		self.menu_finactions_record_open      : QAction = self.menu_finactions_record_header.addAction(icon_open,      "Открыть запись")
		self.menu_finactions_record_edit_note : QAction = self.menu_finactions_record_header.addAction(icon_edit,      "Редактировать примечание")
		self.menu_finactions_record_delete    : QAction = self.menu_finactions_record_header.addAction(icon_delete,    "Удалить запись")
		self.menu_finactions_record_header.addSeparator()
		self.menu_finactions_record_split     : QAction = self.menu_finactions_record_header.addAction(icon_arrow_l_r, "Разделить запись")

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
		icon_download  = QIcon("./ui/icons/download.svg")
		icon_delete    = QIcon("./ui/icons/item_delete.svg")
		icon_grid_22   = QIcon("./ui/icons/grid_2_2.svg")
		icon_grid_33   = QIcon("./ui/icons/grid_3_3.svg")
		icon_arrow_l_r = QIcon("./ui/icons/arrow_left_right.svg")
		icon_replace   = QIcon("./ui/icons/replace.svg")
		icon_black     = QIcon("./ui/icons/square_black.svg")
		icon_gray      = QIcon("./ui/icons/square_gray.svg")
		icon_blue      = QIcon("./ui/icons/square_blue.svg")
		icon_green     = QIcon("./ui/icons/square_green.svg")
		icon_red       = QIcon("./ui/icons/square_red.svg")
		icon_unchecked = QIcon("./ui/icons/checked_uncheck.svg")
		icon_checked   = QIcon("./ui/icons/checked_check.svg")

		self.menu_finactions                                = QMenu()
		self.menu_finactions_header               : QMenu   = self.menu_finactions.addMenu(icon_grid_22, "Финдействия")
		self.menu_finactions_create               : QAction = self.menu_finactions_header.addAction(icon_plus,     "Создать запись")
		self.menu_finactions_header.addSeparator()
		self.menu_finactions_import               : QAction = self.menu_finactions_header.addAction(icon_download, "Импорт финдействий")

		self.menu_finactions_record_header        : QMenu   = self.menu_finactions.addMenu(icon_grid_33, "Запись финдействий")
		self.menu_finactions_record_open          : QAction = self.menu_finactions_record_header.addAction(icon_open,      "Открыть запись")
		self.menu_finactions_record_edit_note     : QAction = self.menu_finactions_record_header.addAction(icon_edit,      "Редактировать примечание")
		self.menu_finactions_record_delete        : QAction = self.menu_finactions_record_header.addAction(icon_delete,    "Удалить запись")
		self.menu_finactions_record_header.addSeparator()
		self.menu_finactions_record_split         : QAction = self.menu_finactions_record_header.addAction(icon_arrow_l_r, "Разделить запись")

		self.menu_finactions_colors_header        : QMenu   = self.menu_finactions.addMenu(icon_gray, "Цветовая метка")
		self.menu_finactions_colors_black         : QAction = self.menu_finactions_colors_header.addAction(icon_black, "Чёрный")
		self.menu_finactions_colors_gray          : QAction = self.menu_finactions_colors_header.addAction(icon_gray,  "Серый")
		self.menu_finactions_colors_blue          : QAction = self.menu_finactions_colors_header.addAction(icon_blue,  "Синий")
		self.menu_finactions_colors_green         : QAction = self.menu_finactions_colors_header.addAction(icon_green, "Зелёный")
		self.menu_finactions_colors_red           : QAction = self.menu_finactions_colors_header.addAction(icon_red,   "Красный")

		self.menu_finactions_pack_header          : QMenu   = self.menu_finactions.addMenu(icon_checked, "Пакетный режим")
		self.menu_finactions_pack_reset           : QAction = self.menu_finactions_pack_header.addAction(icon_unchecked, "Снять выбор")

		self.menu_finactions_tools_replace_header : QMenu   = self.menu_finactions.addMenu(icon_replace, "Поиск и замена")
		self.menu_finactions_tools_replace_text   : QAction = self.menu_finactions_tools_replace_header.addAction(icon_replace, "Замена текстового фрагмента")

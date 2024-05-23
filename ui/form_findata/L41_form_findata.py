# ФОРМА ФИНДАННЫЕ: МОДЕЛЬ UI

from PySide6.QtGui     import QIcon, QAction
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_findata  import Ui_form_findata


class C41_FormFindata(C20_PySideForm, Ui_form_findata):
	""" Форма Финданные: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuData()

	def InitMenuData(self):
		""" Меню финструктуры """

		icon_arrow_up_down = QIcon("./ui/icons/arrow_up_down.svg")
		icon_blocks        = QIcon("./ui/icons/blocks.svg")
		icon_checked       = QIcon("./ui/icons/checked_check.svg")
		icon_delete        = QIcon("./ui/icons/item_delete.svg")
		icon_download      = QIcon("./ui/icons/download.svg")
		icon_gear          = QIcon("./ui/icons/gear.svg")
		icon_grid_2_2      = QIcon("./ui/icons/grid_2_2.svg")
		icon_grid_3_3      = QIcon("./ui/icons/grid_3_3.svg")
		icon_open          = QIcon("./ui/icons/open.svg")
		icon_plus          = QIcon("./ui/icons/item_plus.svg")
		icon_processing    = QIcon("./ui/icons/processing.svg")
		icon_replace       = QIcon("./ui/icons/replace.svg")
		icon_right         = QIcon("./ui/icons/arrow_right.svg")
		icon_right_2       = QIcon("./ui/icons/arrow_right_2.svg")
		icon_unchecked     = QIcon("./ui/icons/checked_uncheck.svg")
		icon_upload        = QIcon("./ui/icons/upload.svg")

		self.menu_data                                                     = QMenu(None)
		self.menu_data_findata_header                            : QMenu   = self.menu_data.addMenu(icon_blocks, "Финданные")
		self.menu_data_findata_create                            : QAction = self.menu_data_findata_header.addAction(icon_plus,    "Создать запись финданных")
		self.menu_data_findata_header.addSection("Пакетная обработка")
		self.menu_data_findata_create_finactions_quick           : QAction = self.menu_data_findata_header.addAction(icon_right_2, "Быстрое создание записей финдействий")

		self.menu_data_findata_record_header                     : QMenu   = self.menu_data.addMenu(icon_grid_2_2, "Запись финданных")
		self.menu_data_findata_record_open                       : QAction = self.menu_data_findata_record_header.addAction(icon_open, "Открыть")
		self.menu_data_findata_record_delete                     : QAction = self.menu_data_findata_record_header.addAction(icon_delete, "Удалить")
		self.menu_data_findata_record_header.addSection("Преобразование в финдействия")
		self.menu_data_findata_record_create_finactions          : QAction = self.menu_data_findata_record_header.addAction(icon_right, "Создать запись финдействий")
		self.menu_data_findata_record_create_finactions_quick    : QAction = self.menu_data_findata_record_header.addAction(icon_right_2, "Быстрое создание записи финдействий")

		self.menu_data_finactions_record_header                  : QMenu   = self.menu_data.addMenu(icon_grid_3_3, "Запись финдействия")
		self.menu_data_finactions_record_open                    : QAction = self.menu_data_finactions_record_header.addAction(icon_open, "Открыть")
		self.menu_data_finactions_record_delete                  : QAction = self.menu_data_finactions_record_header.addAction(icon_delete, "Удалить")

		self.menu_data_selection_header                          : QMenu   = self.menu_data.addMenu(icon_checked, "Выбор данных")
		self.menu_data_selection_clean                           : QAction = self.menu_data_selection_header.addAction(icon_unchecked, "Сброс выбора")
		self.menu_data_selection_header.addSection("Расширение выбора")
		self.menu_data_selection_expand_by_text                  : QAction = self.menu_data_selection_header.addAction(icon_checked, "По текстовому фрагменту")
		self.menu_data_selection_expand_by_findescription        : QAction = self.menu_data_selection_header.addAction(icon_checked, "По финсоставу")
		self.menu_data_selection_header.addSection("Сокращение выбора")
		self.menu_data_selection_collapse_by_text                : QAction = self.menu_data_selection_header.addAction(icon_unchecked, "По текстовому фрагменту")
		self.menu_data_selection_collapse_by_findescription      : QAction = self.menu_data_selection_header.addAction(icon_unchecked, "По финсоставу")

		self.menu_data_rules_header                              : QMenu   = self.menu_data.addMenu(icon_processing, "Правила обработки данных")
		self.menu_data_rules_header.addSection("Обычная\Пакетная обработка")
		self.menu_data_rules_replace_text                        : QAction = self.menu_data_rules_header.addAction(icon_processing, "Замена текстовых фрагментов")
		self.menu_data_rules_detect_findescription               : QAction = self.menu_data_rules_header.addAction(icon_processing, "Определение финсостава")
		self.menu_data_rules_header.addSection("Массовая обработка")
		self.menu_data_rules_replace_text_for_all                : QAction = self.menu_data_rules_header.addAction(icon_processing, "Замена текстовых фрагментов")
		self.menu_data_rules_detect_findescription_for_all       : QAction = self.menu_data_rules_header.addAction(icon_processing, "Определение финсостава")

		self.menu_data_tools_header                              : QMenu   = self.menu_data.addMenu(icon_gear, "Утилиты")
		self.menu_data_tools_replace                             : QAction = self.menu_data_tools_header.addAction(icon_replace, "Поиск и замена")

		self.menu_data_exchange_header                           : QMenu   = self.menu_data.addMenu(icon_arrow_up_down, "Обмен данными")
		self.menu_data_exchange_import                           : QAction = self.menu_data_exchange_header.addAction(icon_download, "Импорт данных")
		self.menu_data_exchange_export                           : QAction = self.menu_data_exchange_header.addAction(icon_upload,   "Экспорт данных")

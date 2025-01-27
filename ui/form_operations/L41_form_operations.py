# ФОРМА ФИНАНСОВЫЕ ОПЕРАЦИИ: МОДЕЛЬ UI

from PySide6.QtGui       import QIcon, QAction
from PySide6.QtWidgets   import QMenu

from L20_PySide6         import C20_PySideForm
from L40_form_operations import Ui_frm_operations


class C41_FormOperations(C20_PySideForm, Ui_frm_operations):
	""" Форма Финансовые операции: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		super().InitMenus()

		self.Init_MenuOperations()

	def Init_MenuOperations(self):
		""" Инициализация меню Финансовые операции """
		icon_arrows_l_r = QIcon("./L0/icons/arrow_left_right.svg")
		icon_black      = QIcon("./L0/icons/square_black.svg")
		icon_blocks     = QIcon("./L0/icons/blocks.svg")
		icon_blue       = QIcon("./L0/icons/square_blue.svg")
		icon_delete     = QIcon("./L0/icons/item_delete.svg")
		icon_edit       = QIcon("./L0/icons/edit.svg")
		icon_gray       = QIcon("./L0/icons/square_gray.svg")
		icon_green      = QIcon("./L0/icons/square_green.svg")
		icon_grid_3_3   = QIcon("./L0/icons/grid_3_3.svg")
		icon_import     = QIcon("./L0/icons/download.svg")
		icon_item_plus  = QIcon("./L0/icons/item_plus.svg")
		icon_layers     = QIcon("./L0/icons/layers.svg")
		icon_red        = QIcon("./L0/icons/square_red.svg")
		icon_reload     = QIcon("./L0/icons/reload.svg")
		icon_upload     = QIcon("./L0/icons/upload.svg")

		self.action_operations_create_operation        = QAction(icon_item_plus,  "Создать операцию")
		self.action_operations_import                  = QAction(icon_import,     "Импорт операций")
		self.action_operations_export                  = QAction(icon_upload,     "Экспорт операций")
		self.action_operations_open_processing         = QAction(icon_layers,     "Обработка операций")
		self.action_operations_reset                   = QAction(icon_reload,     "Сброс данных")
		self.action_operation_delete_operation         = QAction(icon_delete,     "Удалить операцию")
		self.action_operation_split                    = QAction(icon_arrows_l_r, "Разделить операцию")
		self.action_operation_clone                    = QAction(icon_arrows_l_r, "Клонировать операцию")
		self.action_operation_set_amount               = QAction(icon_edit,       "Сумма")
		self.action_operation_set_accounts             = QAction(icon_edit,       "Счет")
		self.action_operation_set_destination          = QAction(icon_edit,       "Назначение")
		self.action_operation_set_detail               = QAction(icon_edit,       "Уточнение")
		self.action_operation_set_object_int           = QAction(icon_edit,       "Объект внутренний")
		self.action_operation_set_object_ext           = QAction(icon_edit,       "Объект внешний")
		self.action_operation_colors_set_black         = QAction(icon_black,      "Чёрный")
		self.action_operation_colors_set_gray          = QAction(icon_gray,       "Серый")
		self.action_operation_colors_set_red           = QAction(icon_red,        "Красный")
		self.action_operation_colors_set_blue          = QAction(icon_blue,       "Синий")
		self.action_operation_colors_set_green         = QAction(icon_green,      "Зелёный")

		self.menu_operations                           = QMenu("Операции")

		self.submenu_operations                        = self.menu_operations.addMenu(icon_blocks, "Операции")
		self.submenu_operations.addAction(self.action_operations_create_operation)
		self.submenu_operations.addSeparator()
		self.submenu_operations.addAction(self.action_operations_import)
		self.submenu_operations.addAction(self.action_operations_export)
		self.submenu_operations.addSeparator()
		self.submenu_operations.addAction(self.action_operations_reset)

		self.submenu_operation                         = self.menu_operations.addMenu(icon_grid_3_3, "Операция")
		self.submenu_operation.addSection("Редактирование")
		self.submenu_operation.addAction(self.action_operation_set_amount)
		self.submenu_operation.addAction(self.action_operation_set_accounts)
		self.submenu_operation.addAction(self.action_operation_set_destination)
		self.submenu_operation.addAction(self.action_operation_set_detail)
		self.submenu_operation.addAction(self.action_operation_set_object_int)
		self.submenu_operation.addAction(self.action_operation_set_object_ext)
		self.submenu_operation.addSeparator()
		self.submenu_operation.addAction(self.action_operation_delete_operation)
		self.submenu_operation.addSeparator()
		self.submenu_operation.addAction(self.action_operation_split)
		self.submenu_operation.addAction(self.action_operation_clone)
		self.submenu_operation.addSeparator()
		self.submenu_operation_colors                  = self.submenu_operation.addMenu(icon_gray, "Цветовая метка")
		self.submenu_operation_colors.addAction(self.action_operation_colors_set_black)
		self.submenu_operation_colors.addAction(self.action_operation_colors_set_gray)
		self.submenu_operation_colors.addSeparator()
		self.submenu_operation_colors.addAction(self.action_operation_colors_set_red)
		self.submenu_operation_colors.addAction(self.action_operation_colors_set_blue)
		self.submenu_operation_colors.addAction(self.action_operation_colors_set_green)

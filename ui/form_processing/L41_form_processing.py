# ФОРМА ОБРАБОТКА ДАННЫХ: МОДЕЛЬ UI

from PySide6.QtGui       import QAction, QIcon
from PySide6.QtWidgets   import QMenu

from L20_PySide6         import C20_PySideForm
from L40_form_processing import Ui_form_processing


class C41_FormProcessing(C20_PySideForm, Ui_form_processing):
	""" Форма Обработка данных: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		super().InitMenus()

		self.InitMenuArchives()

	def InitMenuArchives(self):
		""" Инициализация меню архива данных """
		icon_edit       = QIcon("./L0/icons/edit.svg")
		icon_processing = QIcon("./L0/icons/processing.svg")

		self.action_operations_edit_include     = QAction(icon_edit,       "Редактировать фрагмент поиска")
		self.action_operations_edit_exclude     = QAction(icon_edit,       "Редактировать фрагмент исключения")
		self.action_operations_edit_destination = QAction(icon_edit,       "Редактировать назначение")
		self.action_operations_edit_detail      = QAction(icon_edit,       "Редактировать уточнение")
		self.action_operations_edit_object_int  = QAction(icon_edit,       "Редактировать объект внутренний")
		self.action_operations_edit_object_ext  = QAction(icon_edit,       "Редактировать объект внешний")
		self.action_operations_edit_color       = QAction(icon_edit,       "Редактировать цветовую метку")
		self.action_operations_edit_interval    = QAction(icon_edit,       "Редактировать интервал обработки")
		self.action_operations_processing       = QAction(icon_processing, "Выполнить обработку операций")

		self.menu_operations                    = QMenu()
		self.menu_operations.addAction(self.action_operations_edit_include)
		self.menu_operations.addAction(self.action_operations_edit_exclude)
		self.menu_operations.addSeparator()

		self.menu_operations.addAction(self.action_operations_edit_destination)
		self.menu_operations.addAction(self.action_operations_edit_detail)
		self.menu_operations.addAction(self.action_operations_edit_object_int)
		self.menu_operations.addAction(self.action_operations_edit_object_ext)
		self.menu_operations.addAction(self.action_operations_edit_color)
		self.menu_operations.addSeparator()

		self.menu_operations.addAction(self.action_operations_edit_interval)
		self.menu_operations.addSeparator()

		self.menu_operations.addAction(self.action_operations_processing)

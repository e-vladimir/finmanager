# ФОРМА ПРАВИЛ ОБРАБОТКИ: МОДЕЛЬ UI

from PySide6.QtGui     import QIcon, QAction
from PySide6.QtWidgets import QMenu

from L20_PySide6       import C20_PySideForm
from L40_form_rules    import Ui_form_rules


class C41_FormRules(C20_PySideForm, Ui_form_rules):
	""" Форма правил обработки: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		"""  """
		self.InitMenuReplaceText()
		self.InitMenuDetectFindescription()

	def InitMenuReplaceText(self):
		""" Инициализацию меню правил замены фрагментов """
		icon_delete = QIcon("./ui/icons/item_delete.svg")
		icon_edit   = QIcon("./ui/icons/edit.svg")
		icon_plus   = QIcon("./ui/icons/item_plus.svg")

		self.menu_replace_text                              = QMenu(None)
		self.menu_replace_text_header             : QAction = self.menu_replace_text.addSection("Правила замены текстовых фрагментов")
		self.menu_replace_text_create             : QAction = self.menu_replace_text.addAction(icon_plus,  "Создать запись")

		self.menu_replace_text_record_header      : QAction = self.menu_replace_text.addSection("Запись правил замены текстовых фрагментов")
		self.menu_replace_text_record_edit_input  : QAction = self.menu_replace_text.addAction(icon_edit,   "Редактировать фрагменты поиска")
		self.menu_replace_text_record_edit_output : QAction = self.menu_replace_text.addAction(icon_edit,   "Редактировать фрагмент замены")
		self.menu_replace_text_record_delete      : QAction = self.menu_replace_text.addAction(icon_delete, "Удалить запись")

	def InitMenuDetectFindescription(self):
		""" Инициализацию меню правил определения финсостава """
		icon_delete = QIcon("./ui/icons/item_delete.svg")
		icon_edit   = QIcon("./ui/icons/edit.svg")
		icon_layers = QIcon("./ui/icons/layers.svg")

		self.menu_detect_findescription                             = QMenu(None)
		self.menu_detect_findescription_record_header     : QAction = self.menu_detect_findescription.addSection("Запись правила определения финсостава")
		self.menu_detect_findescription_record_edit_input : QAction = self.menu_detect_findescription.addAction(icon_edit,  "Редактировать фрагменты поиска")
		self.menu_detect_findescription_record_delete     : QAction = self.menu_detect_findescription.addAction(icon_delete, "Удалить запись")
		self.menu_detect_findescription.addSeparator()

		self.menu_detect_findescription_record_wrap       : QAction = self.menu_detect_findescription.addAction(icon_layers, "Свернуть фрагменты поиска")

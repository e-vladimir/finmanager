# ФОРМА ОСНОВНАЯ: МОДЕЛЬ UI

from PySide6.QtGui import QIcon

from L20_PySide6   import C20_PySideForm
from L40_form_main import Ui_form_main


class C41_FormMain(C20_PySideForm, Ui_form_main):
	""" Форма Основная: Модель UI """

	def InitUi(self):
		self.setupUi(self)
		self.InitButtons()

	def InitButtons(self):
		""" Инициализация кнопок """
		icon_l = QIcon("./L0/icons/arrow_left.svg")
		icon_r = QIcon("./L0/icons/arrow_right.svg")

		self.btn_dm_prev.setIcon(icon_l)
		self.btn_dm_next.setIcon(icon_r)

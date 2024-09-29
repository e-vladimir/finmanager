# ФОРМА ОСНОВНАЯ: МОДЕЛЬ UI

from PySide6.QtGui import QIcon

from L20_PySide6   import C20_PySideForm
from L40_form_main import Ui_form_main


class C41_FormMain(C20_PySideForm, Ui_form_main):
	""" Форма основная: Модель UI """

	def InitUi(self):
		self.setupUi(self)

		self.AdjustBtns()

	def AdjustBtns(self):
		""" Настройка кнопок """
		icon_prev = QIcon(f"./L0/icons/arrow_left.svg")
		icon_next = QIcon(f"./L0/icons/arrow_right.svg")

		self.btn_dm_prev.setIcon(icon_prev)
		self.btn_dm_next.setIcon(icon_next)

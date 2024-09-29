# ФОРМА ФИНАНАЛИТИКА: МОДЕЛЬ UI

from PySide6.QtGui         import QAction, QIcon
from PySide6.QtWidgets     import QMenu

from L20_PySide6           import C20_PySideForm
from L40_form_finanalitics import Ui_form_finanalitics


class C41_FormFinanalitics(C20_PySideForm, Ui_form_finanalitics):
	""" Форма Финаналитика: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		self.InitMenuFinanalitics()

	def InitMenuFinanalitics(self):
		""" Инициализацию меню финсостава """
		icon_processing = QIcon("./L0/icons/processing.svg")

		self.menu_finanalitics                      = QMenu()
		self.menu_finanalitics_processing : QAction = self.menu_finanalitics.addAction(icon_processing, "Выполнить анализ")

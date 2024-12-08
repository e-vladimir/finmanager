# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtWidgets              import QHeaderView

from L00_form_processing_operations import SUBJECTS
from L60_form_processing_operations import C60_FormProcessingOperations


class C70_FormProcessingOperations(C60_FormProcessingOperations):
	""" Форма Обработка операций: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Обработка операций - {self.workspace.DmDyToString()}")

	# Список субъектов обработки
	def FillCbboxSubject(self):
		""" Заполнение списка субъектов обработки """
		self.cbbox_subject.clear()
		self.cbbox_subject.addItems([subject.value for subject in SUBJECTS])

	# Таблица правил
	def AdjustTableRules_Size(self):
		""" Таблица правил: Настройка размера """
		self.table_rules.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
		self.table_rules.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

		self.table_rules.resizeRowsToContents()

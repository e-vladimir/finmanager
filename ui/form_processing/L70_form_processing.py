# ФОРМА ОБРАБОТКА ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ
# 22 мар 2025

from PySide6.QtWidgets   import QHeaderView

from L00_form_processing import PROCESSING_FIELDS
from L60_form_processing import C60_FormProcessing


class C70_FormProcessing(C60_FormProcessing):
	""" Форма Обработка данных: Механика управления """

	# Рабочее поле
	def ControlProcessingField(self):
		""" Контроль значения рабочего поля """
		match self.processing_field:
			case PROCESSING_FIELDS.FILTER_DESCRIPTION            : self.on_RequestSetOperationsFilterDescription()
			case PROCESSING_FIELDS.PROCESSING_REPLACE_DESCRIPTION: self.on_RequestSetOperationsReplaceDescription()
			case PROCESSING_FIELDS.PROCESSING_SET_DESCRIPTION    : self.on_RequestSetOperationsSetDescription()
			case PROCESSING_FIELDS.PROCESSING_SET_COLOR          : self.on_RequestSetOperationsSetColor()

	# Дерево параметров Обработка операций
	def AdjustTreeDataOperations_Expand(self):
		""" Дерево данных Обработка операций: Настройка раскрытия """
		self.TreeDataOperations.expandAll()

	def AdjustTreeDataOperations_Size(self):
		""" Дерево данных Обработка операций: Настройка размеров """
		self.TreeDataOperations.setColumnWidth(0, 250)

		self.TreeDataOperations.header().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

	def AdjustTreeDataOperations_Color(self):
		""" Дерево данных Обработка операций: Настройка цветовой схемы """
		self.ModelDataOperations.adjustGroupView(True, True, True)

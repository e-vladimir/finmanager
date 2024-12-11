# ФОРМА СТАТИСТИКА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore     import Qt

from G11_convertor_data import AmountToString
from L20_PySide6 import C20_StandardItem
from L50_form_statistic import C50_FormStatistic


class C60_FormStatistic(C50_FormStatistic):
	""" Форма Статистика: Механика данных """

	# Модель данных статистики
	def InitModelStatistic(self):
		""" Инициализация модели статистики """
		self.model_statistic.removeAll()

		self.model_statistic.setHorizontalHeaderLabels(["Метка", "Объём\nпоступлений", "Объём\nсписаний"])

		self.model_statistic.horizontalHeaderItem(0).setTextAlignment(Qt.AlignmentFlag.AlignLeft  | Qt.AlignmentFlag.AlignVCenter)
		self.model_statistic.horizontalHeaderItem(1).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
		self.model_statistic.horizontalHeaderItem(2).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

	def LoadStatisticInModelStatistic(self):
		"""  """
		dy, dm = self.workspace.DyDm()

		for statistic_item in self.statistic.CaptureDataInDm(dy, dm):
			amount_income  : str = AmountToString(statistic_item.amount_income,  False, True) if statistic_item.amount_income  else ""
			amount_outcome : str = AmountToString(statistic_item.amount_outcome, False, True) if statistic_item.amount_outcome else ""

			item_label           = C20_StandardItem(statistic_item.label)
			item_amount_income   = C20_StandardItem(amount_income,  flag_align_right=True)
			item_amount_outcome  = C20_StandardItem(amount_outcome, flag_align_right=True)

			self.model_statistic.invisibleRootItem().appendRow([item_label, item_amount_income, item_amount_outcome])

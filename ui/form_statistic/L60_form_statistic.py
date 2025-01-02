# ФОРМА СТАТИСТИКА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore     import Qt

from G11_convertor_data import AmountToString

from L20_PySide6        import C20_StandardItem
from L50_form_statistic import C50_FormStatistic


class C60_FormStatistic(C50_FormStatistic):
	""" Форма Статистика: Механика данных """

	# Модель данных структуры статистики
	def InitModelStatisticStruct(self):
		""" Инициализация модели статистики со структурой """
		self.model_statistic_struct.removeAll()

		self.model_statistic_struct.setHorizontalHeaderLabels(["Метка", "Объём\nпоступлений", "Объём\nсписаний"])

		self.model_statistic_struct.horizontalHeaderItem(0).setTextAlignment(Qt.AlignmentFlag.AlignLeft  | Qt.AlignmentFlag.AlignVCenter)
		self.model_statistic_struct.horizontalHeaderItem(1).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
		self.model_statistic_struct.horizontalHeaderItem(2).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

	def LoadModelStatisticStruct(self):
		""" Загрузка модели структуры статистики """
		if self._processing_item is None: self._processing_item = self.model_statistic_struct.invisibleRootItem()

		dy, dm = self.workspace.DyDm()

		for statistic_item in self.statistic.CaptureDataInDmByLabels(dy, dm, self._processing_labels):
			if statistic_item.caption in self._processing_labels: continue

			amount_income  : str = AmountToString(statistic_item.amount_income,  False, True) if statistic_item.amount_income  else ""
			amount_outcome : str = AmountToString(statistic_item.amount_outcome, False, True) if statistic_item.amount_outcome else ""

			item_label           = C20_StandardItem(statistic_item.caption)
			item_amount_income   = C20_StandardItem(amount_income,  flag_align_right=True)
			item_amount_outcome  = C20_StandardItem(amount_outcome, flag_align_right=True)

			self._processing_item.appendRow([item_label, item_amount_income, item_amount_outcome])

	# Параметры
	def ReadProcessingItemFromTreeStatisticStruct(self):
		""" Чтение текущего элемента из дерева структуры статистики """
		current_index = self.tree_statistic_struct.currentIndex()
		self._processing_item = self.model_statistic_struct.itemFromIndex(current_index)

	def ReadProcessingLabelsFromCurrentItem(self):
		""" Чтение текущего набора меток из текущего элемента """
		self._processing_labels.clear()

		if self._processing_item is None: return

		self._processing_labels.append(self._processing_item.text())

		parent = self._processing_item.parent()

		while parent is not None:
			self._processing_labels.append(parent.text())
			parent = parent.parent()

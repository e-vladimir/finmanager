# ФОРМА СТАТИСТИКА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore     import Qt

from G11_convertor_data import AmountToString

from L20_PySide6        import C20_StandardItem, ROLES
from L50_form_statistic import C50_FormStatistic
from L90_analytics      import C90_AnalyticsItem


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
		""" Загрузка статистики """
		dy, dm = self.workspace.DyDm()

		for statistic_item in self.statistic.CaptureDataInDm(dy, dm):
			amount_income  : str = AmountToString(statistic_item.amount_income,  False, True) if statistic_item.amount_income  else ""
			amount_outcome : str = AmountToString(statistic_item.amount_outcome, False, True) if statistic_item.amount_outcome else ""

			item_label           = C20_StandardItem(statistic_item.caption)
			item_amount_income   = C20_StandardItem(amount_income,  flag_align_right=True)
			item_amount_outcome  = C20_StandardItem(amount_outcome, flag_align_right=True)

			self.model_statistic.invisibleRootItem().appendRow([item_label, item_amount_income, item_amount_outcome])

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

	# Модель данных аналитики
	def InitModelAnalytics(self):
		""" Инициализация модели аналитики """
		self.model_analytics.removeAll()

		self.model_analytics.setHorizontalHeaderLabels(["Фрагмент аналитики", "Включает", "Исключает", "Объём\nпоступлений", "Объём\nсписаний"])

		self.model_analytics.horizontalHeaderItem(0).setTextAlignment(Qt.AlignmentFlag.AlignLeft  | Qt.AlignmentFlag.AlignVCenter)
		self.model_analytics.horizontalHeaderItem(1).setTextAlignment(Qt.AlignmentFlag.AlignLeft  | Qt.AlignmentFlag.AlignVCenter)
		self.model_analytics.horizontalHeaderItem(2).setTextAlignment(Qt.AlignmentFlag.AlignLeft  | Qt.AlignmentFlag.AlignVCenter)
		self.model_analytics.horizontalHeaderItem(3).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
		self.model_analytics.horizontalHeaderItem(4).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

	def LoadAnalyticsItemToModelAnalytics(self):
		""" Загрузка элемента аналитики в модель """
		dy, dm         = self.workspace.DyDm()
		analytics_item = C90_AnalyticsItem(self._processing_ido)
		data           = analytics_item.CaptureAmountsInDm(dy, dm)

		if not self.model_analytics.checkIdo(self._processing_ido):
			item_name    = C20_StandardItem("", self._processing_ido, ROLES.IDO)
			item_include = C20_StandardItem("", self._processing_ido, ROLES.IDO)
			item_exclude = C20_StandardItem("", self._processing_ido, ROLES.IDO)
			item_income  = C20_StandardItem("", self._processing_ido, ROLES.IDO, flag_align_right = True)
			item_outcome = C20_StandardItem("", self._processing_ido, ROLES.IDO, flag_align_right = True)

			self.model_analytics.invisibleRootItem().appendRow([item_name, item_include, item_exclude, item_income, item_outcome])

		indexes        = self.model_analytics.indexesInRowByIdo(self._processing_ido)

		item_name      = self.model_analytics.itemFromIndex(indexes[0])
		item_name.setText(data.caption)

		item_include   = self.model_analytics.itemFromIndex(indexes[1])
		item_include.setText('\n'.join(analytics_item.LabelsInclude()))

		item_exclude   = self.model_analytics.itemFromIndex(indexes[2])
		item_exclude.setText('\n'.join(analytics_item.LabelsExclude()))

		item_income    = self.model_analytics.itemFromIndex(indexes[3])
		item_income.setText(AmountToString(data.amount_income, flag_sign = True))

		item_outcome   = self.model_analytics.itemFromIndex(indexes[4])
		item_outcome.setText(AmountToString(data.amount_outcome, flag_sign = True))

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

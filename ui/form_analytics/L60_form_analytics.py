# ФОРМА АНАЛИТИКА ДАННЫХ: МЕХАНИКА ДАННЫХ
# 11 апр 2025

from PySide6.QtCore     import QModelIndex

from G11_convertor_data import AmountToString
from L00_form_analytics import ANALYTICS_DATA, ANALYTICS_FIELDS
from L00_months import MONTHS_SHORT
from L20_PySide6        import C20_StandardItem, ROLES
from L50_form_analytics import C50_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C60_FormAnalytics(C50_FormAnalytics):
	""" Форма Аналитика данных: Механика данных """

	# Рабочий IDO
	@property
	def processing_ido(self) -> str:
		return self._processing_ido

	@processing_ido.setter
	def processing_ido(self, ido: str):
		self._processing_ido = ido

	def ReadProcessingIdoFromListDataItems(self):
		""" Чтение из дерева списка элементов аналитики """
		self.processing_ido = self.ListDataItems.currentIndex().data(ROLES.IDO)


	# Рабочий параметр
	@property
	def processing_field(self) -> ANALYTICS_FIELDS:
		return self._processing_field

	@processing_field.setter
	def processing_field(self, field: ANALYTICS_FIELDS):
		self._processing_field = field

	def ReadProcessingFieldFromTreeDataItem(self):
		""" Чтение из дерева параметров элемента аналитики """
		self.processing_field = self.TreeDataItem.currentIndex().data(ROLES.IDO)


	# Рабочий набор Признаки+
	@property
	def processing_include(self) -> list[str]:
		return self._processing_include[:]

	@processing_include.setter
	def processing_include(self, items: list[str]):
		self._processing_include = items[:]


	# Рабочий набор Признаки-
	@property
	def processing_exclude(self) -> list[str]:
		return self._processing_exclude[:]

	@processing_exclude.setter
	def processing_exclude(self, items: list[str]):
		self._processing_exclude = items[:]


	# Модель данных - Элементы аналитики
	def InitModelDataItems(self):
		""" Инициализация модели """
		self.ModelDataItems.removeAll()
		self.ModelDataItems.setHorizontalHeaderLabels(["Название"])

	def ClearModelDataItems(self):
		""" Очистка модели данных элементов аналитики """
		idos : list[str] = self.Analytics.Idos()

		for index_item in self.ModelDataItems.indexes(QModelIndex()):
			if index_item.data(ROLES.IDO) in idos: continue

			self.ModelDataItems.removeRow(index_item.row(), QModelIndex())

	def LoadAnalyticsItemInModel(self):
		""" Загрузка элемента аналитики в модель данных """
		if not self._processing_ido: return

		analytics_item = C90_AnalyticsItem(self.processing_ido)

		if not self.ModelDataItems.checkIdo(self.processing_ido):
			item_name = C20_StandardItem("")
			item_name.setData(self.processing_ido, ROLES.IDO)

			self.ModelDataItems.appendRow(item_name)

		item_name = self.ModelDataItems.itemByData(self.processing_ido, ROLES.IDO)
		item_name.setText(analytics_item.name)


	# Модель данных - Элемент аналитики
	def InitModelDataItem(self):
		""" Инициализация модели """
		self.ModelDataItem.removeAll()
		self.ModelDataItem.setHorizontalHeaderLabels(["Параметр", "Значение"])

		fields     = [ANALYTICS_FIELDS.INCLUDE,
		              ANALYTICS_FIELDS.EXCLUDE]

		item_group = C20_StandardItem("")
		item_group.setText("Область действия")

		for item in fields:
			item_field = C20_StandardItem(f"{item}", item, ROLES.IDO)
			item_value = C20_StandardItem(f""      , item, ROLES.IDO)
			item_group.appendRow([item_field, item_value])

		self.ModelDataItem.appendRow([item_group, C20_StandardItem("")])

	def LoadModelDataItem(self):
		""" Загрузка модели данных элемента аналитики """
		analytics_item = C90_AnalyticsItem(self.processing_ido)

		indexes        = self.ModelDataItem.indexesInRowByIdo(ANALYTICS_FIELDS.INCLUDE)
		item_value     = self.ModelDataItem.itemFromIndex(indexes[1])
		item_value.setText('\n'.join(analytics_item.include))

		indexes        = self.ModelDataItem.indexesInRowByIdo(ANALYTICS_FIELDS.EXCLUDE)
		item_value     = self.ModelDataItem.itemFromIndex(indexes[1])
		item_value.setText('\n'.join(analytics_item.exclude))


	# Модель данных - Аналитика данных
	def InitModelDataAnalytics(self):
		""" Инициализация модели данных аналитики """
		self.ModelDataAnalytics.removeAll()

		self.ModelDataAnalytics.setHorizontalHeaderLabels(["Показатель", "Значение-", "Значение+", "Баланс"])

	def LoadDataDynamicDyInModel(self):
		""" Загрузка данных динамики за год в модель """
		if not self.ModelDataAnalytics.checkIdo(ANALYTICS_DATA.DYNAMIC_DY):
			item_group   = C20_StandardItem("ДИНАМИКА ОБЪЁМА ЗА ГОД")
			item_group.setData(ANALYTICS_DATA.DYNAMIC_DY, ROLES.IDO)
			item_group.setData(ANALYTICS_DATA.DYNAMIC_DY, ROLES.GROUP)

			item_outcome = C20_StandardItem("Объём +", flag_align_right=True)
			item_outcome.setData(ANALYTICS_DATA.DYNAMIC_DY, ROLES.IDO)
			item_outcome.setData(ANALYTICS_DATA.DYNAMIC_DY, ROLES.GROUP)

			item_income  = C20_StandardItem("Объём -", flag_align_right=True)
			item_income.setData(ANALYTICS_DATA.DYNAMIC_DY, ROLES.IDO)
			item_income.setData(ANALYTICS_DATA.DYNAMIC_DY, ROLES.GROUP)

			item_delta   = C20_StandardItem("Баланс", flag_align_right=True)
			item_delta.setData(ANALYTICS_DATA.DYNAMIC_DY, ROLES.IDO)
			item_delta.setData(ANALYTICS_DATA.DYNAMIC_DY, ROLES.GROUP)

			self.ModelDataAnalytics.appendRow([item_group, item_income, item_outcome, item_delta])

		item_group = self.ModelDataAnalytics.itemByData(ANALYTICS_DATA.DYNAMIC_DY, ROLES.IDO)
		item_group.removeRows(0, item_group.rowCount())

		for data_item in self._data_dynamic_dy:
			item_name    = C20_StandardItem(f"{MONTHS_SHORT[data_item.dm]} {data_item.dy}")
			item_outcome = C20_StandardItem(f"{AmountToString(data_item.amount_outcome)}", flag_align_right=True)
			item_income  = C20_StandardItem(f"{AmountToString(data_item.amount_income)}", flag_align_right=True)
			item_delta   = C20_StandardItem(f"{AmountToString(data_item.amount_income - abs(data_item.amount_outcome))}", flag_align_right=True)

			item_group.appendRow([item_name, item_income, item_outcome, item_delta])

	def LoadDataDynamicDmInModel(self):
		""" Загрузка данных динамики за месяц в модель """
		pass

	def LoadDataIntervalsInModel(self):
		""" Загрузка данных интервалов в модель """
		pass

	def LoadDataDistributionInModel(self):
		""" Загрузка данных распределения в модель """
		pass

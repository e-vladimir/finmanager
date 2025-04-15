# ФОРМА АНАЛИТИКА ДАННЫХ: МЕХАНИКА ДАННЫХ
# 11 апр 2025

from PySide6.QtCore     import QModelIndex

from G10_datetime       import CalcDyDmByShiftDm
from G11_convertor_data import AmountToString

from L00_form_analytics import ANALYTICS_FIELDS
from L00_months import MONTHS_SHORT
from L20_PySide6        import C20_StandardItem, ROLES
from L20_form_analytics import T20_AnalyticItem, T20_Operation
from L50_form_analytics import C50_FormAnalytics
from L90_analytics      import C90_AnalyticsItem
from L90_operations     import C90_Operation


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


	# Данные об операциях
	def ReadOperations(self):
		""" Чтение данных """
		self._operations.clear()

		dy, dm    = self.Workspace.DyDm()
		operation = C90_Operation()
		for ido in self.Operations.Idos(dy, dm):
			operation.Ido(ido)

			labels    : set[str] = set(operation.labels)

			flag_skip : bool     = True
			flag_skip           &= bool(self.processing_include) and not labels.intersection(self.processing_include)
			flag_skip           &= bool(self.processing_exclude) and     labels.intersection(self.processing_exclude)

			if flag_skip: continue

			self._operations.append(T20_Operation(dd     = operation.dd,
			                                      amount = operation.amount,
			                                      labels = labels))


	# Данные динамики за год
	def ReadDataDynamicDy(self):
		""" Чтение данных """
		self._data_dynamic_dy.clear()

		operation = C90_Operation()
		dy, dm    = self.Workspace.DyDm()

		for _ in range(12):
			amounts : list[float] = []

			for ido in self.Operations.Idos(dy, dm):
				operation.Ido(ido)

				labels    : set[str] = set(operation.labels)

				flag_skip : bool     = True
				flag_skip           &= bool(self.processing_include) and not labels.intersection(self.processing_include)
				flag_skip           &= bool(self.processing_exclude) and     labels.intersection(self.processing_exclude)

				if flag_skip: continue

				amounts.append(operation.amount)

			income  : int         = int(sum([amount for amount in amounts if amount > 0]))
			outcome : int         = int(sum([amount for amount in amounts if amount < 0]))

			self._data_dynamic_dy.append(T20_AnalyticItem(name    = f"{MONTHS_SHORT[dm]} {dy}",
			                                              income  = income,
			                                              outcome = abs(outcome)))

			dy, dm                = CalcDyDmByShiftDm(dy, dm, -1)


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

		self.ModelDataAnalytics.setHorizontalHeaderLabels(["Показатель", "ед.изм", "+", "+ (%)", "-", "- (%)", "Разница"])

	def LoadDataDynamicDyInModel(self):
		""" Загрузка данных динамики за год в модель """
		item_root               = C20_StandardItem("ДИНАМИКА ОБЪЁМА ЗА ГОД")

		self.ModelDataAnalytics.appendRow([item_root,
		                                   C20_StandardItem("ед.изм.", flag_align_right=True),
		                                   C20_StandardItem("+"      , flag_align_right=True),
		                                   C20_StandardItem("+ (%)"  , flag_align_right=True),
		                                   C20_StandardItem("-"      , flag_align_right=True),
		                                   C20_StandardItem("- (%)"  , flag_align_right=True),
		                                   C20_StandardItem("Разница", flag_align_right=True),
		                                   ])

		incomes      : int      =     sum([item.income  for item in self._data_dynamic_dy])
		outcomes     : int      = abs(sum([item.outcome for item in self._data_dynamic_dy]))

		for item in self._data_dynamic_dy:
			item_root.appendRow([C20_StandardItem(f"{item.name}"),
			                     C20_StandardItem(f"руб",                                                          flag_align_right=True),
			                     C20_StandardItem(f"{AmountToString(item.income,                flag_sign=True)}", flag_align_right=True),
			                     C20_StandardItem(f"{100 * item.income  / max(1, incomes):.0f}%",                  flag_align_right=True),
			                     C20_StandardItem(f"{AmountToString(-item.outcome,              flag_sign=True)}", flag_align_right=True),
			                     C20_StandardItem(f"{100 * item.outcome / max(1, outcomes):.0f}%",                 flag_align_right=True),
			                     C20_StandardItem(f"{AmountToString(item.income - item.outcome, flag_sign=True)}", flag_align_right=True),
			                     ])

		avg_income  : int       = incomes  // 12
		avg_outcome : int       = outcomes // 12
		item_root.appendRow([C20_StandardItem(f"Средний объём за месяц"),
		                     C20_StandardItem(f"руб",                                                        flag_align_right=True),
		                     C20_StandardItem(f"{AmountToString(avg_income,               flag_sign=True)}", flag_align_right=True),
		                     C20_StandardItem(f""),
		                     C20_StandardItem(f"{AmountToString(-avg_outcome,             flag_sign=True)}", flag_align_right=True),
		                     C20_StandardItem(f""),
		                     C20_StandardItem(f"{AmountToString(avg_income - avg_outcome, flag_sign=True)}", flag_align_right=True),
		                     ])

		incomes     : list[int] = [item.income  for item in self._data_dynamic_dy if item.income  > 0]
		outcomes    : list[int] = [item.outcome for item in self._data_dynamic_dy if item.outcome > 0]
		avg_income  : int       = sum(incomes)  // max(1, len(incomes))
		avg_outcome : int       = sum(outcomes) // max(1, len(outcomes))
		item_root.appendRow([C20_StandardItem(f"Базовый объём за месяц"),
		                     C20_StandardItem(f"руб",                                                        flag_align_right=True),
		                     C20_StandardItem(f"{AmountToString(avg_income,               flag_sign=True)}", flag_align_right=True),
		                     C20_StandardItem(f""),
		                     C20_StandardItem(f"{AmountToString(-avg_outcome,             flag_sign=True)}", flag_align_right=True),
		                     C20_StandardItem(f""),
		                     C20_StandardItem(f"{AmountToString(avg_income - avg_outcome, flag_sign=True)}", flag_align_right=True),
		                     ])

	def LoadDataDynamicDmInModel(self):
		""" Загрузка данных динамики за месяц в модель """
		item_root = C20_StandardItem(f"ДИНАМИКА ОБЪЁМА ЗА {self.Workspace.DmDyToString().upper()}")

		self.ModelDataAnalytics.appendRow([item_root,
		                                   C20_StandardItem("ед.изм.", flag_align_right=True),
		                                   C20_StandardItem("+"      , flag_align_right=True),
		                                   C20_StandardItem("+ (%)"  , flag_align_right=True),
		                                   C20_StandardItem("-"      , flag_align_right=True),
		                                   C20_StandardItem("- (%)"  , flag_align_right=True),
		                                   C20_StandardItem("Разница", flag_align_right=True),
		                                   ])

	def LoadDataOperationsInModel(self):
		""" Загрузка данных интервалов в модель """
		item_root = C20_StandardItem("АНАЛИТИКА ОПЕРАЦИЙ")
		
		self.ModelDataAnalytics.appendRow([item_root,
		                                   C20_StandardItem("ед.изм.", flag_align_right=True),
		                                   C20_StandardItem("+"      , flag_align_right=True),
		                                   C20_StandardItem("+ (%)"  , flag_align_right=True),
		                                   C20_StandardItem("-"      , flag_align_right=True),
		                                   C20_StandardItem("- (%)"  , flag_align_right=True),
		                                   C20_StandardItem("Разница", flag_align_right=True),
		                                   ])

	def LoadDataDistributionInModel(self):
		""" Загрузка данных распределения в модель """
		item_root = C20_StandardItem("АНАЛИТИКА РАСПРЕДЕЛЕНИЯ ОБЪЁМА")

		self.ModelDataAnalytics.appendRow([item_root,
		                                   C20_StandardItem("ед.изм.", flag_align_right=True),
		                                   C20_StandardItem("+"      , flag_align_right=True),
		                                   C20_StandardItem("+ (%)"  , flag_align_right=True),
		                                   C20_StandardItem("-"      , flag_align_right=True),
		                                   C20_StandardItem("- (%)"  , flag_align_right=True),
		                                   C20_StandardItem("Разница", flag_align_right=True),
		                                   ])

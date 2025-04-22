# ФОРМА АНАЛИТИКА ДАННЫХ: МЕХАНИКА ДАННЫХ
# 11 апр 2025

import statistics

from PySide6.QtCore     import QModelIndex

from G10_datetime       import CalcDyDmByShiftDm, CountDdInDyDm
from G11_convertor_data import AmountToString

from L00_form_analytics import ANALYTICS_DATA, ANALYTICS_FIELDS
from L00_months         import MONTHS_SHORT
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

	def ResetProcessingInclude(self):
		""" Сброс данных """
		self.processing_include = []


	# Рабочий набор Признаки-
	@property
	def processing_exclude(self) -> list[str]:
		return self._processing_exclude[:]

	@processing_exclude.setter
	def processing_exclude(self, items: list[str]):
		self._processing_exclude = items[:]

	def ResetProcessingExclude(self):
		""" Сброс даных """
		self.processing_exclude = []


	# Рабочее название
	@property
	def processing_name(self) -> str:
		return self._processing_name

	@ processing_name.setter
	def processing_name(self, name: str):
		self._processing_name = name

	def ReadProcessingNameFromTreeDataAnalytics(self):
		""" Чтение из дерева данных """
		self.processing_name = self.TreeDataAnalytics.currentIndex().data(ROLES.TEXT)

	def ResetProcessingName(self):
		""" Сброс """
		self.processing_name = ""


	# Данные об операциях
	def ReadOperations(self):
		""" Чтение данных """
		self._operations.clear()

		dy, dm                   = self.Workspace.DyDm()
		operation                = C90_Operation()
		for ido in self.Operations.Idos(dy, dm, use_cache=True, exclude_skip=True, exclude_suboperations=False):
			operation.Ido(ido)

			labels    : set[str] = set(operation.labels)

			flag_skip : bool     = True
			flag_skip           &= bool(self.processing_include) and not labels.intersection(self.processing_include)
			flag_skip           |= bool(self.processing_exclude) and     labels.intersection(self.processing_exclude)

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

			for ido in self.Operations.Idos(dy, dm, exclude_skip=True, exclude_suboperations=False):
				operation.Ido(ido)

				labels    : set[str] = set(operation.labels)

				flag_skip : bool     = True
				flag_skip           &= bool(self.processing_include) and not labels.intersection(self.processing_include)
				flag_skip           |= bool(self.processing_exclude) and     labels.intersection(self.processing_exclude)

				if flag_skip: continue

				amounts.append(operation.amount)

			income  : int         = int(sum([amount for amount in amounts if amount > 0]))
			outcome : int         = int(sum([amount for amount in amounts if amount < 0]))

			self._data_dynamic_dy.append(T20_AnalyticItem(name    = f"{MONTHS_SHORT[dm]} {dy}",
			                                              income  = income,
			                                              outcome = abs(outcome)))

			dy, dm                = CalcDyDmByShiftDm(dy, dm, -1)


	# Данные динамики за месяц
	def ReadDataDynamicDm(self):
		""" Чтение данных """
		incomes_dd  : list[int] = [0 for _ in range(32)]
		outcomes_dd : list[int] = [0 for _ in range(32)]

		for operation in self._operations:
			if operation.amount > 0: incomes_dd[operation.dd]  +=     operation.amount
			else                   : outcomes_dd[operation.dd] += abs(operation.amount)

		self._data_dynamic_dm[ANALYTICS_DATA.VOLUME] = T20_AnalyticItem(name    = "Общий объём",
		                                                                income  = int(sum(incomes_dd)),
		                                                                outcome = int(sum(outcomes_dd)))

		income_25   : int       = 0
		income_50   : int       = 0
		income_75   : int       = 0
		outcome_25  : int       = 0
		outcome_50  : int       = 0
		outcome_75  : int       = 0

		volume      : int       = 0
		for idx_dd, amount in enumerate(incomes_dd):
			volume += amount

			if (not income_25) and volume > sum(incomes_dd) * 0.25: income_25 = idx_dd
			if (not income_50) and volume > sum(incomes_dd) * 0.50: income_50 = idx_dd
			if (not income_75) and volume > sum(incomes_dd) * 0.75: income_75 = idx_dd

		volume      : int       = 0
		for idx_dd, amount in enumerate(outcomes_dd):
			volume += amount

			if (not outcome_25) and volume > sum(outcomes_dd) * 0.25: outcome_25 = idx_dd
			if (not outcome_50) and volume > sum(outcomes_dd) * 0.50: outcome_50 = idx_dd
			if (not outcome_75) and volume > sum(outcomes_dd) * 0.75: outcome_75 = idx_dd

		self._data_dynamic_dm[ANALYTICS_DATA.VOLUME_25] = T20_AnalyticItem(name    = "25% объёма",
		                                                                   income  = income_25,
		                                                                   outcome = outcome_25)

		self._data_dynamic_dm[ANALYTICS_DATA.VOLUME_50] = T20_AnalyticItem(name    = "50% объёма",
		                                                                   income  = income_50,
		                                                                   outcome = outcome_50)

		self._data_dynamic_dm[ANALYTICS_DATA.VOLUME_75] = T20_AnalyticItem(name    = "75% объёма",
		                                                                   income  = income_75,
		                                                                   outcome = outcome_75)

		self._data_dynamic_dm[ANALYTICS_DATA.DW_1] = T20_AnalyticItem(name   = "1 неделя",
		                                                              income = int(sum(incomes_dd[:8])),
		                                                              outcome= int(sum(outcomes_dd[:8])))
		self._data_dynamic_dm[ANALYTICS_DATA.DW_2] = T20_AnalyticItem(name   = "2 неделя",
		                                                              income = int(sum(incomes_dd[8:16])),
		                                                              outcome= int(sum(outcomes_dd[8:16])))
		self._data_dynamic_dm[ANALYTICS_DATA.DW_3] = T20_AnalyticItem(name   = "3 неделя",
		                                                              income = int(sum(incomes_dd[16:24])),
		                                                              outcome= int(sum(outcomes_dd[16:24])))
		self._data_dynamic_dm[ANALYTICS_DATA.DW_4] = T20_AnalyticItem(name   = "4 неделя",
		                                                              income = int(sum(incomes_dd[24:])),
		                                                              outcome= int(sum(outcomes_dd[24:])))


	# Данные анализа операций
	def ReadDataOperations(self):
		""" Чтение данных """
		incomes  : list[int] = [int(item.amount)      for item in self._operations if item.amount > 0]
		outcomes : list[int] = [int(abs(item.amount)) for item in self._operations if item.amount < 0]

		income   : int       = 0 if len(incomes)  < 1 else int(statistics.mean(incomes))
		outcome  : int       = 0 if len(outcomes) < 1 else int(statistics.mean(outcomes))
		self._data_operations[ANALYTICS_DATA.VOLUME_AVG] = T20_AnalyticItem(name    = "Средний объём операции",
		                                                                    income  = income,
		                                                                    outcome = outcome)

		income   : int       = 0 if len(incomes)  < 2 else int(statistics.mode(incomes))
		outcome  : int       = 0 if len(outcomes) < 2 else int(statistics.mode(outcomes))
		self._data_operations[ANALYTICS_DATA.VOLUME_MODA] = T20_AnalyticItem(name    = "Обычный объём операции",
		                                                                    income  = income,
		                                                                    outcome = outcome)

		income   : int       = 0 if len(incomes)  < 2 else int(statistics.mode(sorted(incomes)[:int(len(incomes)   * 0.5)]))
		outcome  : int       = 0 if len(outcomes) < 2 else int(statistics.mode(sorted(outcomes)[:int(len(outcomes) * 0.5)]))
		self._data_operations[ANALYTICS_DATA.VOLUME_50] = T20_AnalyticItem(name    = "Обычный объём 50% операций",
		                                                                    income  = income,
		                                                                    outcome = outcome)

		income   : int       = 0 if len(incomes)  < 2 else int(statistics.mode(sorted(incomes)[:int(len(incomes)   * 0.8)]))
		outcome  : int       = 0 if len(outcomes) < 2 else int(statistics.mode(sorted(outcomes)[:int(len(outcomes) * 0.8)]))
		self._data_operations[ANALYTICS_DATA.VOLUME_80] = T20_AnalyticItem(name    = "Обычный объём 80% операций",
		                                                                    income  = income,
		                                                                    outcome = outcome)


	# Данные распределения объёма
	def ReadDataDistribution(self):
		""" Чтение данных """
		self._data_distribution.clear()

		dy, dm = self.Workspace.DyDm()

		for label in self.Operations.Labels(dy, dm, use_cache=True):
			amounts : list[float] = [operation.amount for operation in self._operations if label in operation.labels]

			income  : int         =     int(sum([amount for amount in amounts if amount > 0]))
			outcome : int         = abs(int(sum([amount for amount in amounts if amount < 0])))

			if (not income) and (not outcome): continue

			self._data_distribution[label] = T20_AnalyticItem(name    = label,
			                                                  income  = income,
			                                                  outcome = outcome)

		for ido in self.Analytics.Idos():
			analytic_item         = C90_AnalyticsItem(ido)
			amounts : list[float] = []

			for operation in self._operations:
				if analytic_item.include and not set(analytic_item.include).intersection(operation.labels): continue
				if analytic_item.exclude and     set(analytic_item.exclude).intersection(operation.labels): continue

				amounts.append(operation.amount)

			income  : int         =     int(sum([amount for amount in amounts if amount > 0]))
			outcome : int         = abs(int(sum([amount for amount in amounts if amount < 0])))

			self._data_distribution[analytic_item.name] = T20_AnalyticItem(name    = analytic_item.name,
						                                                   income  = income,
						                                                   outcome = outcome)


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
		item_root.appendRow([C20_StandardItem(f"Обычный объём за месяц"),
		                     C20_StandardItem(f"руб",                                                        flag_align_right=True),
		                     C20_StandardItem(f"{AmountToString(avg_income,               flag_sign=True)}", flag_align_right=True),
		                     C20_StandardItem(f""),
		                     C20_StandardItem(f"{AmountToString(-avg_outcome,             flag_sign=True)}", flag_align_right=True),
		                     C20_StandardItem(f""),
		                     C20_StandardItem(f"{AmountToString(avg_income - avg_outcome, flag_sign=True)}", flag_align_right=True),
		                     ])

		self.ModelDataAnalytics.fastAppendLabels([""])

	def LoadDataDynamicDmInModel(self):
		""" Загрузка данных динамики за месяц в модель """
		item_root    = C20_StandardItem(f"ДИНАМИКА ОБЪЁМА ЗА {self.Workspace.DmDyToString().upper()}")
		self.ModelDataAnalytics.appendRow([item_root,
		                                   C20_StandardItem(""),
		                                   C20_StandardItem(""),
		                                   C20_StandardItem(""),
		                                   C20_StandardItem(""),
		                                   C20_StandardItem(""),
		                                   C20_StandardItem(""),
		                                   ])

		item_subroot = C20_StandardItem("Достижение объёма")
		item_root.appendRow([item_subroot,
                             C20_StandardItem("ед.изм.", flag_align_right=True),
                             C20_StandardItem("+",       flag_align_right=True),
                             C20_StandardItem("",        flag_align_right=True),
                             C20_StandardItem("-",       flag_align_right=True),
                             C20_StandardItem("",        flag_align_right=True),
                             C20_StandardItem("Разница", flag_align_right=True),
                             ])

		for item in [ANALYTICS_DATA.VOLUME_25, ANALYTICS_DATA.VOLUME_50, ANALYTICS_DATA.VOLUME_75]:
			data = self._data_dynamic_dm[item]
			item_subroot.appendRow([C20_StandardItem(f"{data.name}"),
		                            C20_StandardItem(f"день",                                                         flag_align_right=True),
		                            C20_StandardItem(f"{data.income}",                                                flag_align_right=True),
		                            C20_StandardItem(f"",                                                             flag_align_right=True),
		                            C20_StandardItem(f"{data.outcome}",                                               flag_align_right=True),
		                            C20_StandardItem(f"",                                                             flag_align_right=True),
		                            C20_StandardItem(f"{AmountToString(data.outcome - data.income, flag_sign=True)}", flag_align_right=True),
		                            ])

		item_subroot = C20_StandardItem("Распределение объёма")
		item_root.appendRow([item_subroot,
                             C20_StandardItem("ед.изм.", flag_align_right=True),
                             C20_StandardItem("+"      , flag_align_right=True),
                             C20_StandardItem("+ (%)"  , flag_align_right=True),
                             C20_StandardItem("-"      , flag_align_right=True),
                             C20_StandardItem("- (%)"  , flag_align_right=True),
                             C20_StandardItem("Разница", flag_align_right=True),
                             ])

		income  = self._data_dynamic_dm[ANALYTICS_DATA.VOLUME].income
		outcome = self._data_dynamic_dm[ANALYTICS_DATA.VOLUME].outcome

		for item in [ANALYTICS_DATA.DW_1, ANALYTICS_DATA.DW_2, ANALYTICS_DATA.DW_3, ANALYTICS_DATA.DW_4]:
			data = self._data_dynamic_dm[item]
			item_subroot.appendRow([C20_StandardItem(f"{data.name}"),
		                            C20_StandardItem(f"руб, %",                                                       flag_align_right=True),
		                            C20_StandardItem(f"{AmountToString( data.income,               flag_sign=True)}", flag_align_right=True),
		                            C20_StandardItem(f"{100 * data.income  / max(1, income):.0f}%",                   flag_align_right=True),
		                            C20_StandardItem(f"{AmountToString(-data.outcome,              flag_sign=True)}", flag_align_right=True),
		                            C20_StandardItem(f"{100 * data.outcome / max(1, outcome):.0f}%",                  flag_align_right=True),
		                            C20_StandardItem(f"{AmountToString(data.income - data.outcome, flag_sign=True)}", flag_align_right=True),
		                            ])

		item_subroot = C20_StandardItem("Скорость изменения объёма")
		item_root.appendRow([item_subroot,
                             C20_StandardItem("ед.изм.", flag_align_right=True),
                             C20_StandardItem("+",       flag_align_right=True),
                             C20_StandardItem("",        flag_align_right=True),
                             C20_StandardItem("-",       flag_align_right=True),
                             C20_StandardItem("",        flag_align_right=True),
                             C20_StandardItem("Разница", flag_align_right=True),
                             ])

		for item in [ANALYTICS_DATA.DW_1, ANALYTICS_DATA.DW_2, ANALYTICS_DATA.DW_3, ANALYTICS_DATA.DW_4]:
			data = self._data_dynamic_dm[item]
			item_subroot.appendRow([C20_StandardItem(f"{data.name}"),
		                            C20_StandardItem(f"руб/день",                                                            flag_align_right=True),
		                            C20_StandardItem(f"{AmountToString( data.income                 // 7, flag_sign=True)}", flag_align_right=True),
		                            C20_StandardItem(f"",                                                                    flag_align_right=True),
		                            C20_StandardItem(f"{AmountToString(-data.outcome                // 7, flag_sign=True)}", flag_align_right=True),
		                            C20_StandardItem(f"",                                                                    flag_align_right=True),
		                            C20_StandardItem(f"{AmountToString((data.income - data.outcome) // 7, flag_sign=True)}", flag_align_right=True),
		                            ])

		dy, dm   = self.Workspace.DyDm()
		count_dd = CountDdInDyDm(dy, dm)
		item_subroot.appendRow([C20_StandardItem(f"Средняя скорость"),
	                            C20_StandardItem(f"руб/день",                                                         flag_align_right=True),
	                            C20_StandardItem(f"{AmountToString( income            // count_dd, flag_sign=True)}", flag_align_right=True),
	                            C20_StandardItem(f"",                                                                 flag_align_right=True),
	                            C20_StandardItem(f"{AmountToString(-outcome           // count_dd, flag_sign=True)}", flag_align_right=True),
	                            C20_StandardItem(f"",                                                                 flag_align_right=True),
	                            C20_StandardItem(f"{AmountToString((income - outcome) // count_dd, flag_sign=True)}", flag_align_right=True),
	                            ])

		self.ModelDataAnalytics.fastAppendLabels([""])

	def LoadDataOperationsInModel(self):
		""" Загрузка данных интервалов в модель """
		item_root = C20_StandardItem(f"АНАЛИТИКА ОПЕРАЦИЙ ЗА {self.Workspace.DmDyToString().upper()}")
		self.ModelDataAnalytics.appendRow([item_root,
		                                   C20_StandardItem("ед.изм.", flag_align_right=True),
		                                   C20_StandardItem("+",       flag_align_right=True),
		                                   C20_StandardItem("",        flag_align_right=True),
		                                   C20_StandardItem("-",       flag_align_right=True),
		                                   C20_StandardItem("",        flag_align_right=True),
		                                   C20_StandardItem("",        flag_align_right=True),
		                                   ])

		item_subroot = C20_StandardItem("Объём")
		item_root.appendRow([item_subroot,
		                     C20_StandardItem("ед.изм.", flag_align_right=True),
		                     C20_StandardItem("+",       flag_align_right=True),
		                     C20_StandardItem("",        flag_align_right=True),
		                     C20_StandardItem("-",       flag_align_right=True),
		                     C20_StandardItem("",        flag_align_right=True),
		                     C20_StandardItem("",        flag_align_right=True),
		                     ])
		for item in [ANALYTICS_DATA.VOLUME_AVG, ANALYTICS_DATA.VOLUME_MODA, ANALYTICS_DATA.VOLUME_50, ANALYTICS_DATA.VOLUME_80]:
			data = self._data_operations[item]
			item_subroot.appendRow([C20_StandardItem(f"{data.name}"),
		                            C20_StandardItem(f"руб",                                             flag_align_right=True),
		                            C20_StandardItem(f"{AmountToString(data.income,   flag_sign=True)}", flag_align_right=True),
		                            C20_StandardItem(f"",                                                flag_align_right=True),
		                            C20_StandardItem(f"{AmountToString(-data.outcome, flag_sign=True)}", flag_align_right=True),
		                            C20_StandardItem(f"",                                                flag_align_right=True),
		                            C20_StandardItem(f"",                                                flag_align_right=True),
		                            ])

		self.ModelDataAnalytics.fastAppendLabels([""])

	def LoadDataDistributionInModel(self):
		""" Загрузка данных распределения в модель """
		if not self._data_distribution: return

		item_root = C20_StandardItem(f"АНАЛИТИКА РАСПРЕДЕЛЕНИЯ ОБЪЁМА ЗА {self.Workspace.DmDyToString().upper()}")
		self.ModelDataAnalytics.appendRow([item_root,
		                                   C20_StandardItem("ед.изм.", flag_align_right=True),
		                                   C20_StandardItem("+",       flag_align_right=True),
		                                   C20_StandardItem("+ (%)",   flag_align_right=True),
		                                   C20_StandardItem("-",       flag_align_right=True),
		                                   C20_StandardItem("- (%)",   flag_align_right=True),
		                                   C20_StandardItem("",        flag_align_right=True),
		                                   ])

		incomes      : int      =     sum([item.amount for item in self._operations if item.amount > 0])
		outcomes     : int      = abs(sum([item.amount for item in self._operations if item.amount < 0]))

		for label in sorted(self._data_distribution.keys()):
			item = self._data_distribution[label]

			if not item.name: continue

			item_root.appendRow([C20_StandardItem(f"{item.name}", ANALYTICS_DATA.DISTRIBUTION, ROLES.GROUP),
			                     C20_StandardItem(f"руб",                                                          flag_align_right=True),
			                     C20_StandardItem(f"{AmountToString(item.income,                flag_sign=True)}", flag_align_right=True),
			                     C20_StandardItem(f"{100 * item.income  / max(1, incomes):.0f}%",                  flag_align_right=True),
			                     C20_StandardItem(f"{AmountToString(-item.outcome,              flag_sign=True)}", flag_align_right=True),
			                     C20_StandardItem(f"{100 * item.outcome / max(1, outcomes):.0f}%",                 flag_align_right=True),
			                     C20_StandardItem(f"",                                                             flag_align_right=True),
			                     ])

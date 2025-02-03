# ФОРМА АНАЛИТИКА: МЕХАНИКА ДАННЫХ

import datetime
import statistics
from collections import defaultdict

from   typing                 import Any
from   PySide6.QtCore         import Qt

from   G10_convertor_format   import StringToDateTime
from   G10_datetime           import CalcDyDmByShiftDm
from   G11_convertor_data     import AmountToString
from   G30_cactus_datafilters import C30_FilterLinear1D

from   L00_containers         import CONTAINERS
from   L00_form_analytics     import ANALYTICS
from   L00_months             import MONTHS_SHORT
from   L20_PySide6            import C20_StandardItem, ROLES
from   L20_struct_statistic   import T20_StructStatistic
from   L50_form_analytics     import C50_FormAnalytics
from   L90_analytics          import C90_AnalyticsItem
from   L90_operations         import C90_Operation


def  CalcBaseStatistic(data: list) -> (int | None, int | None, int | None, int | None):
	""" Расчёт базовых параметров статистики min avg mod max sum """
	result_min = None
	result_avg = None
	result_mod = None
	result_max = None
	result_sum = None

	try   : result_min = int(min(data))
	except: pass

	try   : result_avg = int(statistics.mean(data))
	except: pass

	try   : result_mod = int(statistics.mode(data))
	except: pass

	try   : result_max = int(max(data))
	except: pass

	try   : result_sum = int(sum(data))
	except: pass

	return result_min, result_avg, result_mod, result_max, result_sum


class C60_FormAnalytics(C50_FormAnalytics):
	""" Форма Аналитика: Механика данных """

	# Модель данных: Список элементов аналитики
	def InitModelDataItems(self):
		""" Инициализация модели данных: список элементов аналитики """
		self.model_items.removeAll()
		self.model_items.setHorizontalHeaderLabels(["Элемент аналитики"])

	def LoadItemInModelDataItems(self):
		""" Загрузка элемента аналитики в модель данных """
		if not self._processing_ido: return

		analytics_item                       = C90_AnalyticsItem(self._processing_ido)

		if not self.model_items.checkIdo(self._processing_ido):
			item_name = C20_StandardItem("", self._processing_ido, ROLES.IDO)
			self.model_items.appendRow(item_name)

		index_name : C20_StandardItem | None = self.model_items.indexByData(self._processing_ido, ROLES.IDO)
		if index_name is None: return

		item_name                            = self.model_items.itemFromIndex(index_name)
		item_name.setText(analytics_item.Name())

	# Модель данных: Элемент аналитики
	def InitModelDataItem(self):
		""" Инициализация модели данных: элемент аналитики """
		self.model_item.removeAll()
		self.model_item.setHorizontalHeaderLabels(["Параметр", "Значение"])

		group_main   = C20_StandardItem("Основные параметры")
		item_include = C20_StandardItem("Признаки+", ANALYTICS.INCLUDE, ROLES.IDO)
		item_exclude = C20_StandardItem("Признаки-", ANALYTICS.EXCLUDE, ROLES.IDO)
		group_main.appendRow([item_include, C20_StandardItem("", ANALYTICS.INCLUDE, ROLES.IDO)])
		group_main.appendRow([item_exclude, C20_StandardItem("", ANALYTICS.EXCLUDE, ROLES.IDO)])
		self.model_item.appendRow([group_main, C20_StandardItem("")])

		group_main   = C20_StandardItem("Объёмный анализ")
		item_volume  = C20_StandardItem("Объёмная величина",          ANALYTICS.VALUE, ROLES.IDO)
		item_unit    = C20_StandardItem("Объёмная единица измерения", ANALYTICS.UNIT,  ROLES.IDO)
		group_main.appendRow([item_volume, C20_StandardItem("", ANALYTICS.VALUE, ROLES.IDO)])
		group_main.appendRow([item_unit,   C20_StandardItem("", ANALYTICS.UNIT,   ROLES.IDO)])
		self.model_item.appendRow([group_main, C20_StandardItem("")])

	def LoadModelDataItem(self):
		""" Загрузка модели данных: элемент аналитики """
		analytics_item = C90_AnalyticsItem(self._processing_ido)

		indexes        = self.model_item.indexesInRowByIdo(ANALYTICS.INCLUDE)
		item_value     = self.model_item.itemFromIndex(indexes[1])
		item_value.setText('\n'.join(analytics_item.Include()))

		indexes        = self.model_item.indexesInRowByIdo(ANALYTICS.EXCLUDE)
		item_value     = self.model_item.itemFromIndex(indexes[1])
		item_value.setText('\n'.join(analytics_item.Exclude()))

		indexes        = self.model_item.indexesInRowByIdo(ANALYTICS.VALUE)
		item_value     = self.model_item.itemFromIndex(indexes[1])
		item_value.setText(AmountToString(analytics_item.MeasurementValue(), flag_point=False))

		indexes        = self.model_item.indexesInRowByIdo(ANALYTICS.UNIT)
		item_value     = self.model_item.itemFromIndex(indexes[1])
		item_value.setText(f"{analytics_item.MeasurementUnit()}")

	# Модель данных: Структура месяца
	def InitModelDataDm(self):
		""" Инициализация модели Структура месяца """
		self.model_dm.removeAll()
		self.model_dm.setHorizontalHeaderLabels(["Элемент аналитики", "Поступление", "Списание"])

		self.model_dm.horizontalHeaderItem(1).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
		self.model_dm.horizontalHeaderItem(2).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

	def LoadModelDataDm(self):
		""" Загрузка модели данных Структура месяца """
		dy, dm     = self.workspace.DyDm()

		item_group = C20_StandardItem("Назначение")
		for data in self.statistic.CaptureDestinationsInDm(dy, dm):
			item_name    = C20_StandardItem(data.name,
			                                ANALYTICS.DESTINATION,
			                                ROLES.IDO)
			item_income  = C20_StandardItem(AmountToString(data.amount_income,  flag_sign=True),
			                                ANALYTICS.DESTINATION,
			                                ROLES.IDO,
			                                flag_align_right=True)
			item_outcome = C20_StandardItem(AmountToString(data.amount_outcome, flag_sign=True),
			                                ANALYTICS.DESTINATION,
			                                ROLES.IDO,
			                                flag_align_right=True)

			item_group.appendRow([item_name, item_income, item_outcome])
		self.model_dm.appendRow([item_group, C20_StandardItem(""), C20_StandardItem("")])

		item_group = C20_StandardItem("Объект внутренний")
		for data in self.statistic.CaptureObjectsIntInDm(dy, dm):
			item_name    = C20_StandardItem(data.name,
			                                ANALYTICS.OBJECT_INT,
			                                ROLES.IDO)
			item_income  = C20_StandardItem(AmountToString(data.amount_income,  flag_sign=True),
			                                ANALYTICS.OBJECT_INT,
			                                ROLES.IDO,
											flag_align_right=True)
			item_outcome = C20_StandardItem(AmountToString(data.amount_outcome, flag_sign=True),
			                                ANALYTICS.OBJECT_INT,
			                                ROLES.IDO,
											flag_align_right=True)

			item_group.appendRow([item_name, item_income, item_outcome])
		self.model_dm.appendRow([item_group, C20_StandardItem(""), C20_StandardItem("")])

		item_group = C20_StandardItem("Объект внешний")
		for data in self.statistic.CaptureObjectsExtInDm(dy, dm):
			item_name    = C20_StandardItem(data.name,
			                                ANALYTICS.OBJECT_EXT,
			                                ROLES.IDO)
			item_income  = C20_StandardItem(AmountToString(data.amount_income,  flag_sign=True),
			                                ANALYTICS.OBJECT_EXT,
			                                ROLES.IDO,
			                                flag_align_right=True)
			item_outcome = C20_StandardItem(AmountToString(data.amount_outcome, flag_sign=True),
			                                ANALYTICS.OBJECT_EXT,
			                                ROLES.IDO,
			                                flag_align_right=True)

			item_group.appendRow([item_name, item_income, item_outcome])
		self.model_dm.appendRow([item_group, C20_StandardItem(""), C20_StandardItem("")])

		item_group = C20_StandardItem("Элементы аналитики")
		for ido in self.analytics.Idos():
			data         = C90_AnalyticsItem(ido).CaptureAmountInDm(dy, dm)
			item_name    = C20_StandardItem(data.name,
			                                ANALYTICS.ITEM,
			                                ROLES.IDO)
			item_income  = C20_StandardItem(AmountToString(data.amount_income,  flag_sign=True),
			                                ANALYTICS.ITEM,
			                                ROLES.IDO,
			                                flag_align_right=True)
			item_outcome = C20_StandardItem(AmountToString(data.amount_outcome, flag_sign=True),
			                                ANALYTICS.ITEM,
			                                ROLES.IDO,
			                                flag_align_right=True)

			item_group.appendRow([item_name, item_income, item_outcome])
		self.model_dm.appendRow([item_group, C20_StandardItem(""), C20_StandardItem("")])

	# Модель данных: Динамика
	def InitModelDataDy(self):
		""" Инициализация модели данных Динамика """
		self.model_dy.removeAll()
		self.model_dy.setHorizontalHeaderLabels(["Элемент аналитики", "Поступление", "Списание"])

		self.model_dy.horizontalHeaderItem(1).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
		self.model_dy.horizontalHeaderItem(2).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

	def LoadModelDataDy(self):
		""" Загрузка модели данных Динамика """
		analytics_item                                  = C90_AnalyticsItem()

		flag_analytics_item : bool                      = analytics_item.SwitchByName(self._processing_object)
		flag_destination    : bool                      = self._processing_object in self.operations.Destinations()
		flag_object_int     : bool                      = self._processing_object in self.operations.ObjectsInt()
		flag_object_ext     : bool                      = self._processing_object in self.operations.ObjectsExt()

		if not any([flag_analytics_item,
		            flag_destination,
		            flag_object_int,
		            flag_object_ext]): return

		dy, dm                                          = self.workspace.DyDm()
		data                : list[T20_StructStatistic] = []

		for idx in range(13):
			if   flag_analytics_item: subdata = analytics_item.CaptureAmountInDm(dy, dm)
			elif flag_destination   : subdata = self.statistic.CaptureDestinationInDm(dy, dm, self._processing_object)
			elif flag_object_int    : subdata = self.statistic.CaptureObjectIntInDm(dy, dm, self._processing_object)
			elif flag_object_ext    : subdata = self.statistic.CaptureObjectExtInDm(dy, dm, self._processing_object)
			else                    : break

			subdata.name = f"{MONTHS_SHORT[dm]} {dy}"
			data.append(subdata)

			dy, dm  = CalcDyDmByShiftDm(dy, dm, -1)

		income_min          : int                       = min([subdata.amount_income  for subdata in data])
		income_max          : int                       = max([subdata.amount_income  for subdata in data])
		income_delta        : int                       = abs(income_max - income_min)
		income_avg          : int                       = abs(income_min + income_delta // 2)

		outcome_min         : int                       = min([subdata.amount_outcome for subdata in data])
		outcome_max         : int                       = max([subdata.amount_outcome for subdata in data])
		outcome_delta       : int                       = abs(outcome_max - outcome_min)
		outcome_avg         : int                       = abs(outcome_min + outcome_delta // 2)

		item_group = C20_StandardItem("Расчётные значения")
		item_avg   = C20_StandardItem("Средние значения")
		item_group.appendRow([item_avg,
		                      C20_StandardItem(AmountToString( income_avg,  flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(-outcome_avg, flag_sign=True), flag_align_right=True),
		                      ])
		self.model_dy.appendRow([item_group,
		                         C20_StandardItem(""),
		                         C20_StandardItem("")
		                         ])

		item_group = C20_StandardItem("Динамика за 12 месяцев")
		for subdata in data:
			item_group.appendRow([C20_StandardItem(subdata.name),
			                      C20_StandardItem(AmountToString(subdata.amount_income,  flag_sign=True), flag_align_right=True),
			                      C20_StandardItem(AmountToString(subdata.amount_outcome, flag_sign=True), flag_align_right=True),
			                      ])
		self.model_dy.appendRow([item_group,
		                         C20_StandardItem(""),
		                         C20_StandardItem("")
		                         ])

	# Модель данных: Аналитика
	def InitModelDataAnalytics(self):
		""" Инициализация модели данных Аналитика """
		self.model_analytics.removeAll()
		self.model_analytics.setHorizontalHeaderLabels(["Критерий анализа", "1М", "3М", "12М", "ВВ"])

		self.model_analytics.horizontalHeaderItem(1).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
		self.model_analytics.horizontalHeaderItem(2).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
		self.model_analytics.horizontalHeaderItem(3).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
		self.model_analytics.horizontalHeaderItem(4).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

	def LoadModelDataAnalytics(self):
		""" Загрузка модели данных Аналитика """
		operation                            = C90_Operation()
		idc                                  = operation.Idc().data
		idp_destination                      = operation.f_destination.Idp().data
		idp_object_int                       = operation.f_object_int.Idp().data
		idp_object_ext                       = operation.f_object_ext.Idp().data
		idp_amount                           = operation.f_amount.Idp().data

		if   self._processing_object in self.analytics.Names()        :
			idos_include : set[str] = set()
			idos_exclude : set[str] = set()

			analytics_item          = C90_AnalyticsItem()
			analytics_item.SwitchByName(self._processing_object)

			for item_include in analytics_item.Include():
				filter_data      = C30_FilterLinear1D(idc)
				filter_data.FilterIdpVlpByInclude(idp_destination, item_include)
				filter_data.FilterIdpVlpByMore(idp_amount, 0, self._processing_mode == ANALYTICS.OUTCOME)
				filter_data.Capture(CONTAINERS.DISK)
				idos_include.update(set(filter_data.Idos().data))

				filter_data      = C30_FilterLinear1D(idc)
				filter_data.FilterIdpVlpByInclude(idp_object_int, item_include)
				filter_data.FilterIdpVlpByMore(idp_amount, 0, self._processing_mode == ANALYTICS.OUTCOME)
				filter_data.Capture(CONTAINERS.DISK)
				idos_include.update(set(filter_data.Idos().data))

				filter_data      = C30_FilterLinear1D(idc)
				filter_data.FilterIdpVlpByInclude(idp_object_ext, item_include)
				filter_data.FilterIdpVlpByMore(idp_amount, 0, self._processing_mode == ANALYTICS.OUTCOME)
				filter_data.Capture(CONTAINERS.DISK)
				idos_include.update(set(filter_data.Idos().data))

			for item_exclude in analytics_item.Exclude():
				filter_data      = C30_FilterLinear1D(idc)
				filter_data.FilterIdpVlpByInclude(idp_destination, item_exclude)
				filter_data.FilterIdpVlpByMore(idp_amount, 0, self._processing_mode == ANALYTICS.OUTCOME)
				filter_data.Capture(CONTAINERS.DISK)
				idos_exclude.update(set(filter_data.Idos().data))

				filter_data      = C30_FilterLinear1D(idc)
				filter_data.FilterIdpVlpByInclude(idp_object_int, item_exclude)
				filter_data.FilterIdpVlpByMore(idp_amount, 0, self._processing_mode == ANALYTICS.OUTCOME)
				filter_data.Capture(CONTAINERS.DISK)
				idos_exclude.update(set(filter_data.Idos().data))

				filter_data      = C30_FilterLinear1D(idc)
				filter_data.FilterIdpVlpByInclude(idp_object_ext, item_exclude)
				filter_data.FilterIdpVlpByMore(idp_amount, 0, self._processing_mode == ANALYTICS.OUTCOME)
				filter_data.Capture(CONTAINERS.DISK)
				idos_exclude.update(set(filter_data.Idos().data))

			idos           = list(idos_include.difference(idos_exclude))

		elif self._processing_object in self.operations.Destinations():
			filter_data = C30_FilterLinear1D(idc)
			filter_data.FilterIdpVlpByInclude(idp_destination, self._processing_object)
			filter_data.FilterIdpVlpByMore(idp_amount, 0, self._processing_mode == ANALYTICS.OUTCOME)
			filter_data.Capture(CONTAINERS.DISK)

			idos        = filter_data.Idos().data

		elif self._processing_object in self.operations.ObjectsInt()  :
			filter_data = C30_FilterLinear1D(idc)
			filter_data.FilterIdpVlpByInclude(idp_object_int,  self._processing_object)
			filter_data.FilterIdpVlpByMore(idp_amount, 0, self._processing_mode == ANALYTICS.OUTCOME)
			filter_data.Capture(CONTAINERS.DISK)

			idos        = filter_data.Idos().data

		elif self._processing_object in self.operations.ObjectsExt()  :
			filter_data = C30_FilterLinear1D(idc)
			filter_data.FilterIdpVlpByInclude(idp_object_ext,  self._processing_object)
			filter_data.FilterIdpVlpByMore(idp_amount, 0, self._processing_mode == ANALYTICS.OUTCOME)
			filter_data.Capture(CONTAINERS.DISK)

			idos        = filter_data.Idos().data

		else: return

		dy, dm                               = self.workspace.DyDm()
		dydm_01M       : int                 = dy*100 + dm

		dy, dm                               = CalcDyDmByShiftDm(dy, dm, -3)
		dydm_03M       : int                 = dy*100 + dm

		dy, dm                               = CalcDyDmByShiftDm(dy, dm, -9)
		dydm_12M       : int                 = dy*100 + dm

		data_01M       : dict[str, Any]      = dict()
		data_01M[ANALYTICS.AMOUNTS]          = []
		data_01M[ANALYTICS.DATES]            = []
		data_01M[ANALYTICS.INTERVALS]        = []
		data_01M[ANALYTICS.DESTINATION]      = defaultdict(int)
		data_01M[ANALYTICS.OBJECT_INT]       = defaultdict(int)
		data_01M[ANALYTICS.OBJECT_EXT]       = defaultdict(int)

		data_03M       : dict[str, Any]      = dict()
		data_03M[ANALYTICS.AMOUNTS]          = []
		data_03M[ANALYTICS.DATES]            = []
		data_03M[ANALYTICS.INTERVALS]        = []
		data_03M[ANALYTICS.DESTINATION]      = defaultdict(int)
		data_03M[ANALYTICS.OBJECT_INT]       = defaultdict(int)
		data_03M[ANALYTICS.OBJECT_EXT]       = defaultdict(int)

		data_12M       : dict[str, Any]      = dict()
		data_12M[ANALYTICS.AMOUNTS]          = []
		data_12M[ANALYTICS.DATES]            = []
		data_12M[ANALYTICS.INTERVALS]        = []
		data_12M[ANALYTICS.DESTINATION]      = defaultdict(int)
		data_12M[ANALYTICS.OBJECT_INT]       = defaultdict(int)
		data_12M[ANALYTICS.OBJECT_EXT]       = defaultdict(int)

		data_ALL       : dict[str, Any]      = dict()
		data_ALL[ANALYTICS.AMOUNTS]          = []
		data_ALL[ANALYTICS.DATES]            = []
		data_ALL[ANALYTICS.INTERVALS]        = []
		data_ALL[ANALYTICS.DESTINATION]      = defaultdict(int)
		data_ALL[ANALYTICS.OBJECT_INT]       = defaultdict(int)
		data_ALL[ANALYTICS.OBJECT_EXT]       = defaultdict(int)

		for ido in idos:
			operation                       = C90_Operation(ido)
			destination : str               = operation.Destination()
			object_int  : str               = operation.ObjectInt()
			object_ext  : str               = operation.ObjectExt()
			dy          : int               = operation.Dy()
			dm          : int               = operation.Dm()
			dd          : int               = operation.Dd()
			dydm        : int               = dy * 100 + dm
			dtime       : datetime.datetime = StringToDateTime(f"{dd:02d}-{dm:02d}-{dy:04d}")

			amount      : int               = int(operation.Amount())

			if dydm >= dydm_01M:
				data_01M[ANALYTICS.AMOUNTS].append(amount)
				data_01M[ANALYTICS.DATES].append(dtime)

				data_01M[ANALYTICS.DESTINATION][destination] += abs(amount)
				data_01M[ANALYTICS.OBJECT_INT][object_int]   += abs(amount)
				data_01M[ANALYTICS.OBJECT_EXT][object_ext]   += abs(amount)

			if dydm >= dydm_03M:
				data_03M[ANALYTICS.AMOUNTS].append(amount)
				data_03M[ANALYTICS.DATES].append(dtime)

				data_03M[ANALYTICS.DESTINATION][destination] += abs(amount)
				data_03M[ANALYTICS.OBJECT_INT][object_int]   += abs(amount)
				data_03M[ANALYTICS.OBJECT_EXT][object_ext]   += abs(amount)

			if dydm >= dydm_12M:
				data_12M[ANALYTICS.AMOUNTS].append(amount)
				data_12M[ANALYTICS.DATES].append(dtime)

				data_12M[ANALYTICS.DESTINATION][destination] += abs(amount)
				data_12M[ANALYTICS.OBJECT_INT][object_int]   += abs(amount)
				data_12M[ANALYTICS.OBJECT_EXT][object_ext]   += abs(amount)

			data_ALL[ANALYTICS.AMOUNTS].append(amount)
			data_ALL[ANALYTICS.DATES].append(dtime)

			data_ALL[ANALYTICS.DESTINATION][destination] += abs(amount)
			data_ALL[ANALYTICS.OBJECT_INT][object_int]   += abs(amount)
			data_ALL[ANALYTICS.OBJECT_EXT][object_ext]   += abs(amount)

		data_01M[ANALYTICS.DATES].sort()
		data_03M[ANALYTICS.DATES].sort()
		data_12M[ANALYTICS.DATES].sort()
		data_ALL[ANALYTICS.DATES].sort()

		data_01M[ANALYTICS.INTERVALS] = [(data_01M[ANALYTICS.DATES][idx + 1] - data_01M[ANALYTICS.DATES][idx]).days for idx in range(len(data_01M[ANALYTICS.DATES]) - 1)]
		data_03M[ANALYTICS.INTERVALS] = [(data_03M[ANALYTICS.DATES][idx + 1] - data_03M[ANALYTICS.DATES][idx]).days for idx in range(len(data_03M[ANALYTICS.DATES]) - 1)]
		data_12M[ANALYTICS.INTERVALS] = [(data_12M[ANALYTICS.DATES][idx + 1] - data_12M[ANALYTICS.DATES][idx]).days for idx in range(len(data_12M[ANALYTICS.DATES]) - 1)]
		data_ALL[ANALYTICS.INTERVALS] = [(data_ALL[ANALYTICS.DATES][idx + 1] - data_ALL[ANALYTICS.DATES][idx]).days for idx in range(len(data_ALL[ANALYTICS.DATES]) - 1)]

		item_group        = C20_StandardItem("Объём операций")
		(amounts_01M_min,
		 amounts_01M_avg,
		 amounts_01M_mod,
		 amounts_01M_max,
		 amounts_01M_sum) = CalcBaseStatistic(data_01M[ANALYTICS.AMOUNTS])
		(amounts_03M_min,
		 amounts_03M_avg,
		 amounts_03M_mod,
		 amounts_03M_max,
		 amounts_03M_sum) = CalcBaseStatistic(data_03M[ANALYTICS.AMOUNTS])
		(amounts_12M_min,
		 amounts_12M_avg,
		 amounts_12M_mod,
		 amounts_12M_max,
		 amounts_12M_sum) = CalcBaseStatistic(data_12M[ANALYTICS.AMOUNTS])
		(amounts_ALL_min,
		 amounts_ALL_avg,
		 amounts_ALL_mod,
		 amounts_ALL_max,
		 amounts_ALL_sum) = CalcBaseStatistic(data_ALL[ANALYTICS.AMOUNTS])

		item_group.appendRow([C20_StandardItem("Минимальный объём операции"),
		                      C20_StandardItem(AmountToString(amounts_01M_min, flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(amounts_03M_min, flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(amounts_12M_min, flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(amounts_ALL_min, flag_sign=True), flag_align_right=True),
		                      ])
		item_group.appendRow([C20_StandardItem("Средний объём операции"),
		                      C20_StandardItem(AmountToString(amounts_01M_avg, flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(amounts_03M_avg, flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(amounts_12M_avg, flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(amounts_ALL_avg, flag_sign=True), flag_align_right=True),
		                      ])
		item_group.appendRow([C20_StandardItem("Типовой объём операции"),
		                      C20_StandardItem(AmountToString(amounts_01M_mod, flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(amounts_03M_mod, flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(amounts_12M_mod, flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(amounts_ALL_mod, flag_sign=True), flag_align_right=True),
		                      ])
		item_group.appendRow([C20_StandardItem("Максимальный объём операции"),
		                      C20_StandardItem(AmountToString(amounts_01M_max, flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(amounts_03M_max, flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(amounts_12M_max, flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(amounts_ALL_max, flag_sign=True), flag_align_right=True),
		                      ])
		item_group.appendRow([C20_StandardItem("Общий объём операций"),
		                      C20_StandardItem(AmountToString(amounts_01M_sum, flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(amounts_03M_sum, flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(amounts_12M_sum, flag_sign=True), flag_align_right=True),
		                      C20_StandardItem(AmountToString(amounts_ALL_sum, flag_sign=True), flag_align_right=True),
		                      ])
		self.model_analytics.appendRow([item_group,
		                                C20_StandardItem("руб.", flag_align_right=True),
		                                C20_StandardItem("руб.", flag_align_right=True),
		                                C20_StandardItem("руб.", flag_align_right=True),
		                                C20_StandardItem("руб.", flag_align_right=True),
		                                ])

		item_group = C20_StandardItem("Интервал операций")
		(intervals_01M_min,
		 intervals_01M_avg,
		 intervals_01M_mod,
		 intervals_01M_max,
		 intervals_01M_sum) = CalcBaseStatistic(data_01M[ANALYTICS.INTERVALS])
		(intervals_03M_min,
		 intervals_03M_avg,
		 intervals_03M_mod,
		 intervals_03M_max,
		 intervals_03M_sum) = CalcBaseStatistic(data_03M[ANALYTICS.INTERVALS])
		(intervals_12M_min,
		 intervals_12M_avg,
		 intervals_12M_mod,
		 intervals_12M_max,
		 intervals_12M_sum) = CalcBaseStatistic(data_12M[ANALYTICS.INTERVALS])
		(intervals_ALL_min,
		 intervals_ALL_avg,
		 intervals_ALL_mod,
		 intervals_ALL_max,
		 intervals_ALL_sum) = CalcBaseStatistic(data_ALL[ANALYTICS.INTERVALS])

		item_group.appendRow([C20_StandardItem("Минимальный интервал"),
		                      C20_StandardItem(AmountToString(intervals_01M_min), flag_align_right=True),
		                      C20_StandardItem(AmountToString(intervals_03M_min), flag_align_right=True),
		                      C20_StandardItem(AmountToString(intervals_12M_min), flag_align_right=True),
		                      C20_StandardItem(AmountToString(intervals_ALL_min), flag_align_right=True),
		                      ])
		item_group.appendRow([C20_StandardItem("Средний интервал"),
		                      C20_StandardItem(AmountToString(intervals_01M_avg), flag_align_right=True),
		                      C20_StandardItem(AmountToString(intervals_03M_avg), flag_align_right=True),
		                      C20_StandardItem(AmountToString(intervals_12M_avg), flag_align_right=True),
		                      C20_StandardItem(AmountToString(intervals_ALL_avg), flag_align_right=True),
		                      ])
		item_group.appendRow([C20_StandardItem("Типовой интервал"),
		                      C20_StandardItem(AmountToString(intervals_01M_mod), flag_align_right=True),
		                      C20_StandardItem(AmountToString(intervals_03M_mod), flag_align_right=True),
		                      C20_StandardItem(AmountToString(intervals_12M_mod), flag_align_right=True),
		                      C20_StandardItem(AmountToString(intervals_ALL_mod), flag_align_right=True),
		                      ])
		item_group.appendRow([C20_StandardItem("Максимальный интервал"),
		                      C20_StandardItem(AmountToString(intervals_01M_max), flag_align_right=True),
		                      C20_StandardItem(AmountToString(intervals_03M_max), flag_align_right=True),
		                      C20_StandardItem(AmountToString(intervals_12M_max), flag_align_right=True),
		                      C20_StandardItem(AmountToString(intervals_ALL_max), flag_align_right=True),
		                      ])
		self.model_analytics.appendRow([item_group,
		                                C20_StandardItem("дн.", flag_align_right=True),
		                                C20_StandardItem("дн.", flag_align_right=True),
		                                C20_StandardItem("дн.", flag_align_right=True),
		                                C20_StandardItem("дн.", flag_align_right=True),
		                                ])

		if   self._processing_object in self.analytics.Names()        :
			analytics_item          = C90_AnalyticsItem()
			analytics_item.SwitchByName(self._processing_object)

			if analytics_item.MeasurementValue():
				item_group = C20_StandardItem("Объёмная стоимость")
				item_group.appendRow([C20_StandardItem(f"Стоимость 1 {analytics_item.MeasurementUnit()}"),
				                      C20_StandardItem("", flag_align_right=True),
				                      C20_StandardItem("", flag_align_right=True),
				                      C20_StandardItem("", flag_align_right=True),
				                      C20_StandardItem(AmountToString(abs(amounts_ALL_sum / analytics_item.MeasurementValue()), flag_point=True), flag_align_right=True),
				                      ])
				self.model_analytics.appendRow([item_group,
				                                C20_StandardItem("",     flag_align_right=True),
				                                C20_StandardItem("",     flag_align_right=True),
				                                C20_StandardItem("",     flag_align_right=True),
				                                C20_StandardItem("руб.", flag_align_right=True),
				                                ])

		item_group        = C20_StandardItem("Объёмный состав по назначению")
		labels : set[str] = (set(data_01M[ANALYTICS.DESTINATION]).union(data_03M[ANALYTICS.DESTINATION])
		                                                         .union(data_12M[ANALYTICS.DESTINATION])
		                                                         .union(data_ALL[ANALYTICS.DESTINATION]))

		for label in sorted(labels):
			if not label: continue

			item_group.appendRow([C20_StandardItem(f"{label}"),
			                      C20_StandardItem(f"{(100 * data_01M[ANALYTICS.DESTINATION][label]/abs(amounts_01M_sum)):.0f}%" if amounts_01M_sum else "", flag_align_right=True),
			                      C20_StandardItem(f"{(100 * data_03M[ANALYTICS.DESTINATION][label]/abs(amounts_03M_sum)):.0f}%" if amounts_03M_sum else "", flag_align_right=True),
			                      C20_StandardItem(f"{(100 * data_12M[ANALYTICS.DESTINATION][label]/abs(amounts_12M_sum)):.0f}%" if amounts_12M_sum else "", flag_align_right=True),
			                      C20_StandardItem(f"{(100 * data_ALL[ANALYTICS.DESTINATION][label]/abs(amounts_ALL_sum)):.0f}%" if amounts_ALL_sum else "", flag_align_right=True),
			                      ])
		self.model_analytics.appendRow([item_group,
		                                C20_StandardItem("%", flag_align_right=True),
		                                C20_StandardItem("%", flag_align_right=True),
		                                C20_StandardItem("%", flag_align_right=True),
		                                C20_StandardItem("%", flag_align_right=True),
		                                ])

		item_group        = C20_StandardItem("Объёмный состав по объекту внутреннему")
		labels : set[str] = (set(data_01M[ANALYTICS.OBJECT_INT]).union(data_03M[ANALYTICS.OBJECT_INT])
		                                                        .union(data_12M[ANALYTICS.OBJECT_INT])
		                                                        .union(data_ALL[ANALYTICS.OBJECT_INT]))

		for label in sorted(labels):
			if not label: continue

			item_group.appendRow([C20_StandardItem(f"{label}"),
			                      C20_StandardItem(f"{(100 * data_01M[ANALYTICS.OBJECT_INT][label]/abs(amounts_01M_sum)):.0f}%" if amounts_01M_sum else "", flag_align_right=True),
			                      C20_StandardItem(f"{(100 * data_03M[ANALYTICS.OBJECT_INT][label]/abs(amounts_03M_sum)):.0f}%" if amounts_03M_sum else "", flag_align_right=True),
			                      C20_StandardItem(f"{(100 * data_12M[ANALYTICS.OBJECT_INT][label]/abs(amounts_12M_sum)):.0f}%" if amounts_12M_sum else "", flag_align_right=True),
			                      C20_StandardItem(f"{(100 * data_ALL[ANALYTICS.OBJECT_INT][label]/abs(amounts_ALL_sum)):.0f}%" if amounts_ALL_sum else "", flag_align_right=True),
			                      ])
		self.model_analytics.appendRow([item_group,
		                                C20_StandardItem("%", flag_align_right=True),
		                                C20_StandardItem("%", flag_align_right=True),
		                                C20_StandardItem("%", flag_align_right=True),
		                                C20_StandardItem("%", flag_align_right=True),
		                                ])

		item_group        = C20_StandardItem("Объёмный состав по объекту внутреннему")
		labels : set[str] = (set(data_01M[ANALYTICS.OBJECT_EXT]).union(data_03M[ANALYTICS.OBJECT_EXT])
		                                                        .union(data_12M[ANALYTICS.OBJECT_EXT])
		                                                        .union(data_ALL[ANALYTICS.OBJECT_EXT]))

		for label in sorted(labels):
			if not label: continue

			item_group.appendRow([C20_StandardItem(f"{label}"),
			                      C20_StandardItem(f"{(100 * data_01M[ANALYTICS.OBJECT_EXT][label]/abs(amounts_01M_sum)):.0f}%" if amounts_01M_sum else "", flag_align_right=True),
			                      C20_StandardItem(f"{(100 * data_03M[ANALYTICS.OBJECT_EXT][label]/abs(amounts_03M_sum)):.0f}%" if amounts_03M_sum else "", flag_align_right=True),
			                      C20_StandardItem(f"{(100 * data_12M[ANALYTICS.OBJECT_EXT][label]/abs(amounts_12M_sum)):.0f}%" if amounts_12M_sum else "", flag_align_right=True),
			                      C20_StandardItem(f"{(100 * data_ALL[ANALYTICS.OBJECT_EXT][label]/abs(amounts_ALL_sum)):.0f}%" if amounts_ALL_sum else "", flag_align_right=True),
			                      ])
		self.model_analytics.appendRow([item_group,
		                                C20_StandardItem("%", flag_align_right=True),
		                                C20_StandardItem("%", flag_align_right=True),
		                                C20_StandardItem("%", flag_align_right=True),
		                                C20_StandardItem("%", flag_align_right=True),
		                                ])

	# Параметры
	def ReadProcessingIdoFromListItems(self):
		""" Чтение текущего IDO из списка элементов аналитики """
		self._processing_ido = self.list_items.currentIndex().data(ROLES.IDO)

	def ReadProcessingIdoFromTreeDataItem(self):
		""" Чтение текущего IDO из дерева параметров элемента аналитики """
		self._processing_ido = self.tree_data_item.currentIndex().data(ROLES.IDO)

	def ReadProcessingObjectFromTreeDataDm(self):
		""" Чтение текущего объекта из дерева Структура месяца """
		current_index = self.tree_data_dm.currentIndex()
		if current_index.data(ROLES.IDO) not in ANALYTICS: return

		self._processing_object = current_index.data(ROLES.TEXT)

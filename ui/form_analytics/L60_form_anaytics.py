# ФОРМА АНАЛИТИКА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore       import Qt

from G10_datetime         import CalcDyDmByShiftDm
from G11_convertor_data   import AmountToString

from L00_form_analytics   import ANALYTICS
from L00_months           import MONTHS_SHORT
from L20_PySide6          import C20_StandardItem, ROLES
from L20_struct_statistic import T20_StructStatistic
from L50_form_analytics   import C50_FormAnalytics
from L90_analytics        import C90_AnalyticsItem


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

		self.model_item.appendRow([group_main, C20_StandardItem("")])
		group_main.appendRow([item_include, C20_StandardItem("", ANALYTICS.INCLUDE, ROLES.IDO)])
		group_main.appendRow([item_exclude, C20_StandardItem("", ANALYTICS.EXCLUDE, ROLES.IDO)])

	def LoadModelDataItem(self):
		""" Загрузка модели данных: элемент аналитики """
		analytics_item = C90_AnalyticsItem(self._processing_ido)

		indexes        = self.model_item.indexesInRowByIdo(ANALYTICS.INCLUDE)
		item_include   = self.model_item.itemFromIndex(indexes[1])
		item_include.setText('\n'.join(analytics_item.Include()))

		indexes        = self.model_item.indexesInRowByIdo(ANALYTICS.EXCLUDE)
		item_exclude   = self.model_item.itemFromIndex(indexes[1])
		item_exclude.setText('\n'.join(analytics_item.Exclude()))

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

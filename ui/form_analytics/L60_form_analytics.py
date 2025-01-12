# ФОРМА АНАЛИТИКА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore     import QModelIndex

from L00_form_analytics import IDOS_ANALYTICS
from L20_PySide6        import C20_StandardItem, ROLES
from L50_form_analytics import C50_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C60_FormAnalytics(C50_FormAnalytics):
	""" Форма Аналитика: Механика данных """

	# Модель Элементы аналитики
	def InitModelItems(self):
		""" Инициализация модели Элементы аналитики """
		self.model_items.removeAll()

	def LoadItemAnalyticsInModelItems(self):
		""" Загрузка элемента аналитики в модель данных """
		if not self._processing_ido: return

		if not self.model_items.checkIdo(self._processing_ido):
			item_name = C20_StandardItem("", self._processing_ido, ROLES.IDO)

			self.model_items.invisibleRootItem().appendRow([item_name])

		analytics_item = C90_AnalyticsItem(self._processing_ido)

		index_name : QModelIndex | None = self.model_items.indexByData(self._processing_ido, ROLES.IDO)
		if index_name is None: return

		item_name  : C20_StandardItem   = self.model_items.itemFromIndex(index_name)
		item_name.setText(analytics_item.Name())

	# Модель данных Параметры
	def InitModelDataOptions(self):
		""" Инициализация модели Параметры """
		self.model_data_options.removeAll()
		self.model_data_options.setHorizontalHeaderLabels(["Параметр", "Значение"])

		group_labels = C20_StandardItem("Основные параметры")
		item_field   = C20_StandardItem("Признаки включения",  IDOS_ANALYTICS.INCLUDE, ROLES.IDO)
		item_value   = C20_StandardItem("",                    IDOS_ANALYTICS.INCLUDE, ROLES.IDO)
		group_labels.appendRow([item_field, item_value])
		item_field   = C20_StandardItem("Признаки исключения", IDOS_ANALYTICS.EXCLUDE, ROLES.IDO)
		item_value   = C20_StandardItem("",                    IDOS_ANALYTICS.EXCLUDE, ROLES.IDO)
		group_labels.appendRow([item_field, item_value])

		self.model_data_options.appendRow(group_labels)

	def LoadModelDataOptions(self):
		""" Загрузка модели данных Параметры """
		analytics_item = C90_AnalyticsItem(self._processing_ido)

		indexes        = self.model_data_options.indexesInRowByIdo(IDOS_ANALYTICS.INCLUDE)
		item_data      = self.model_data_options.itemFromIndex(indexes[1])
		item_data.setText('\n'.join(analytics_item.Include()))

		indexes        = self.model_data_options.indexesInRowByIdo(IDOS_ANALYTICS.EXCLUDE)
		item_data      = self.model_data_options.itemFromIndex(indexes[1])
		item_data.setText('\n'.join(analytics_item.Exclude()))

	# Модель данных Объёмная стоимость
	def InitModelDataVolumes(self):
		""" Инициализация модели Объёмная стоимость """
		self.model_data_volumes.removeAll()

	# Динамика
	def InitDynamic(self):
		""" Инициализация динамики """
		pass

	# Параметры
	def ReadProcessingIdoFromListItems(self):
		""" Чтение IDO из списка элементов аналитики """
		try   : self._processing_ido = self.list_items.selectedIndexes()[0].data(ROLES.IDO)
		except: self._processing_ido = ""

	def ReadProcessingIdoFromTreeOptions(self):
		""" Чтение IDO из дерева параметров """
		self._processing_ido = self.tree_data_options.currentIndex().data(ROLES.IDO)

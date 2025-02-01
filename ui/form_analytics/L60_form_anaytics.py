# ФОРМА АНАЛИТИКА: МЕХАНИКА ДАННЫХ

from L00_form_analytics import ANALYTICS
from L20_PySide6        import C20_StandardItem, ROLES
from L50_form_analytics import C50_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


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

	# Параметры
	def ReadProcessingIdoFromListItems(self):
		""" Чтение текущего IDO из списка элементов аналитики """
		self._processing_ido = self.list_items.currentIndex().data(ROLES.IDO)

	def ReadProcessingIdoFromTreeDataItem(self):
		""" Чтение текущего IDO из дерева параметров элемента аналитики """
		self._processing_ido = self.tree_data_item.currentIndex().data(ROLES.IDO)

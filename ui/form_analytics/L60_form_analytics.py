# ФОРМА АНАЛИТИКА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore     import QModelIndex

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

	# Модель данных Объёмная стоимость
	def InitModelDataVolumes(self):
		""" Инициализация модели Объёмная стоимость """
		self.model_data_options.removeAll()

# ФОРМА АНАЛИТИКА: МЕХАНИКА ДАННЫХ

from L20_PySide6        import C20_StandardItem, ROLES
from L50_form_analytics import C50_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C60_FormAnalytics(C50_FormAnalytics):
	""" Форма Аналитика: Механика данных """

	# Модель данных: Список элементов аналитики
	def InitModelDataItems(self):
		""" Инициализация модели данных: список элементов аналитики """
		pass

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

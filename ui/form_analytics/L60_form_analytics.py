# ФОРМА АНАЛИТИКА: МЕХАНИКА ДАННЫХ

from L20_PySide6        import C20_StandardItem, ROLES
from L50_form_analytics import C50_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C60_FormAnalytics(C50_FormAnalytics):
	""" Форма Аналитика: Механика данных """

	# Модель элементов аналитики
	def InitModelItems(self):
		""" Инициализация модели элементов аналитики """
		self.model_items.removeAll()

		self.model_items.setHorizontalHeaderLabels(["Название"])

	def LoadAnalyticsItem(self):
		""" Загрузка элемента аналитики в модель данных """
		if not self._processing_ido: return

		analytics_item = C90_AnalyticsItem(self._processing_ido)

		if not self.model_items.checkIdo(self._processing_ido):
			item_item = C20_StandardItem(analytics_item.Name(), self._processing_ido, ROLES.IDO)
			self.model_items.invisibleRootItem().appendRow(item_item)

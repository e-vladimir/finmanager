# ФОРМА АНАЛИТИКА ДАННЫХ: МЕХАНИКА ДАННЫХ
# 11 апр 2025
from L20_PySide6 import C20_StandardItem, ROLES
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


	# Модель данных - Элементы аналитики
	def InitModelDataItems(self):
		""" Инициализация модели """
		self.ModelDataItems.removeAll()

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

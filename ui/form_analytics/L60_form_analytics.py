# ФОРМА АНАЛИТИКА ДАННЫХ: МЕХАНИКА ДАННЫХ
# 11 апр 2025

from PySide6.QtCore     import QModelIndex

from L00_form_analytics import ANALYTICS_FIELDS
from L20_PySide6        import C20_StandardItem, ROLES
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

	def ReadProcessingIdoFromListDataItems(self):
		""" Чтение из дерева списка элементов аналитики """
		self.processing_ido = self.ListDataItems.currentIndex().data(ROLES.IDO)


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

		items = [ANALYTICS_FIELDS.INCLUDE,
		         ANALYTICS_FIELDS.EXCLUDE]

		item_group = C20_StandardItem("")
		item_group.setText("Пространство действия")

		for item in items:
			item_field = C20_StandardItem(f"{item}", item, ROLES.IDO)
			item_value = C20_StandardItem(f""      , item, ROLES.IDO)
			item_group.appendRow([item_field, item_value])

		self.ModelDataItem.appendRow([item_group, C20_StandardItem("")])

	def LoadModelDataItem(self):
		""" Загрузка модели данных элемента аналитики """
		pass

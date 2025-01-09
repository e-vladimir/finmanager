# ФОРМА АНАЛИТИКА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore     import QModelIndex

from L20_PySide6        import C20_StandardItem, ROLES
from L50_form_analytics import C50_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C60_FormAnalytics(C50_FormAnalytics):
	""" Форма Аналитика: Механика данных """

	# Модель данных Элементы аналитики
	def InitModelItems(self):
		""" Инициализация модели данных Элементы аналитики """
		self.model_items.removeAll()

		self.model_data.setHorizontalHeaderLabels(["Элемент аналитики"])

	def LoadAnalyticsItemInModelItems(self):
		""" Загрузка элемента аналитики в модель """
		if not self._processing_ido: return

		if not self.model_items.checkIdo(self._processing_ido):
			item_name = C20_StandardItem("", self._processing_ido, ROLES.IDO)
			self.model_items.invisibleRootItem().appendRow(item_name)

		index_name : QModelIndex | None = self.model_items.indexByData(self._processing_ido, ROLES.IDO)
		if index_name is None: return

		analytics_item                  = C90_AnalyticsItem(self._processing_ido)

		item_name  : C20_StandardItem   = self.model_items.itemFromIndex(index_name)
		item_name.setText(analytics_item.Name())

	# Модель данных Данные аналитики
	def InitModelData(self):
		""" Инициализация модели данных Данные аналитики """
		self.model_data.removeAll()

		self.model_data.setHorizontalHeaderLabels(["Показатель", "Значение"])

	def LoadAnalyticsItemInModelData(self):
		""" Загрузка элемента аналитики в модель данных """
		if not self._processing_ido: return

	# Параметры
	def ReadProcessingIdoFromListItems(self):
		""" Чтение текущего IDO из списка элементов аналитики """
		self._processing_ido = ""

		try   : self._processing_ido = self.list_items.selectedIndexes()[0].data(ROLES.IDO)
		except: pass

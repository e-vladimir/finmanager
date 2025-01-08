# ФОРМА АНАЛИТИКА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore     import QModelIndex

from L20_PySide6        import C20_StandardItem, ROLES
from L50_form_analytics import C50_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C60_FormAnalytics(C50_FormAnalytics):
	""" Форма Аналитика: Механика данных """

	# Модель данных элементов аналитики
	def InitModelItems(self):
		""" Инициализация модели данных элементов аналитики """
		self.model_items.removeAll()

		self.model_items.setHorizontalHeaderLabels(["Наименование", "Признаки+", "Признаки-"])

	def LoadAnalyticsItemInModel(self):
		""" Загрузка элемента аналитики в модель данных """
		if not self._processing_ido: return

		analytics_item                   = C90_AnalyticsItem(self._processing_ido)

		if not self.model_items.checkIdo(self._processing_ido):
			item_name       = C20_StandardItem("", self._processing_ido, ROLES.IDO, flag_bold=True)
			item_include    = C20_StandardItem("", self._processing_ido, ROLES.IDO)
			item_exclude    = C20_StandardItem("", self._processing_ido, ROLES.IDO)

			self.model_items.invisibleRootItem().appendRow([item_name, item_include, item_exclude])

		indexes_row  : list[QModelIndex] = self.model_items.indexesInRowByIdo(self._processing_ido)

		item_name    : C20_StandardItem  = self.model_items.itemFromIndex(indexes_row[0])
		item_name.setText(analytics_item.Name())

		item_include : C20_StandardItem  = self.model_items.itemFromIndex(indexes_row[1])
		item_include.setText('\n'.join(analytics_item.Include()))

		item_exclude : C20_StandardItem  = self.model_items.itemFromIndex(indexes_row[2])
		item_exclude.setText('\n'.join(analytics_item.Exclude()))

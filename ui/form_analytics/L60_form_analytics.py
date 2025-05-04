# ФОРМА АНАЛИТИКА ДАННЫХ: МЕХАНИКА ДАННЫХ
# 27 апр 2025

from PySide6.QtCore     import QModelIndex

from L00_form_analytics import GROUPS
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

	def ReadProcessingIdoFromTreeData(self):
		""" Чтение из дерева данных """
		self.processing_ido = self.TreeData.currentIndex().data(ROLES.IDO) or ""

		if self.processing_ido not in [GROUPS.DISTRIBUTION]: return

		self.processing_ido = ""


	# Рабочая группа
	@property
	def processing_group(self) -> str:
		return self._processing_group

	@processing_group.setter
	def processing_group(self, text: str):
		self._processing_group = text

	def ReadProcessingGroupFromTreeData(self):
		""" Чтение из дерева данных """
		self.processing_group = self.TreeData.currentIndex().data(ROLES.GROUP) or ""


	# Рабочая корневой уровень
	@property
	def processing_parent(self) -> str:
		return self._processing_parent

	@processing_parent.setter
	def processing_parent(self, text: str):
		self._processing_parent = text

	def ReadProcessingParentFromTreeData(self):
		""" Чтение из дерева данных """
		self.processing_parent = self.TreeData.currentIndex().data(ROLES.PARENT) or ""

		if self.processing_parent not in [GROUPS.DISTRIBUTION]: return

		self.processing_parent = ""


	# IDO в памяти
	@property
	def memory_ido(self) -> str:
		return self._memory_ido

	@memory_ido.setter
	def memory_ido(self, ido: str):
		self._memory_ido = ido

	def ReadMemoryIdo(self):
		""" Чтение из дерева данных """
		self.memory_ido = self.processing_ido


	# Модель данных
	def InitModelData(self):
		""" Инициализация модели данных """
		self.ModelData.removeAll()
		self.ModelData.setHorizontalHeaderLabels(["Назначение/Уточнение"])


	# Данные распределения
	def ReinitDistributionInModel(self):
		""" Сброс распределения месяца """
		index_group       = self.ModelData.indexByData(GROUPS.DISTRIBUTION, ROLES.IDO)
		if index_group is None: return

		self.ModelData.removeRow(index_group.row(), QModelIndex())

	def LoadDistributionInModel(self):
		""" Загрузка распределения месяца в модель """
		if not self.ModelData.checkIdo(GROUPS.DISTRIBUTION):
			item_group = C20_StandardItem(GROUPS.DISTRIBUTION)
			item_group.setData(GROUPS.DISTRIBUTION, ROLES.IDO)
			item_group.setData(GROUPS.DISTRIBUTION, ROLES.GROUP)

			self.ModelData.appendRow([item_group])

		item_group       = self.ModelData.itemByData(GROUPS.DISTRIBUTION, ROLES.IDO)

		idos : list[str] = self.Analytics.Idos("")

		for ido in idos:
			idos.extend(self.Analytics.Idos(ido))

			analytics_item   = C90_AnalyticsItem(ido)

			if not self.ModelData.checkIdo(ido):
				item_destination = C20_StandardItem("")
				item_destination.setData(ido,                       ROLES.IDO)
				item_destination.setData(GROUPS.DISTRIBUTION,       ROLES.GROUP)
				item_destination.setData(analytics_item.parent_ido, ROLES.PARENT)

				item_parent      = self.ModelData.itemByData(analytics_item.parent_ido, ROLES.IDO) or item_group
				item_parent.appendRow([item_destination])

			item_destination = self.ModelData.itemByData(ido, ROLES.IDO)
			item_destination.setText(analytics_item.name)

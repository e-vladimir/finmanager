# ФОРМА АНАЛИТИКА ДАННЫХ: ЛОГИКА ДАННЫХ
# 27 апр 2025

from L00_containers     import CONTAINERS
from L20_PySide6        import RequestConfirm, RequestText
from L70_form_analytics import C70_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C80_FormAnalytics(C70_FormAnalytics):
	""" Форма Аналитика данных: Логика данных """

	# Структура аналитики
	def ResetDestinations(self):
		""" Сброс элементов аналитики """
		if not RequestConfirm("Сброс данных", "Удаление всех назначений"): return

		for ido in self.Analytics.Idos(""): C90_AnalyticsItem(ido).DeleteObject(CONTAINERS.DISK)

		self.on_StructChanged()


	# Элемент структуры аналитики
	def CreateDestination(self):
		""" Создание назначения в структуре аналитики """
		analytics_item            = C90_AnalyticsItem(self.processing_ido)
		parent_name : str         = C90_AnalyticsItem(self.processing_parent).name or "Структура аналитики"

		destination : str | None  = RequestText("Структура аналитики", f"Создание назначения в группе: {parent_name}")
		if destination is None                  : return
		if destination in self.Analytics.Names(): return

		analytics_item.GenerateIdo()
		analytics_item.RegisterObject(CONTAINERS.DISK)

		analytics_item.name       = destination
		analytics_item.parent_ido = self.processing_parent

		self.on_DestinationCreated()

	def EditDestinationName(self):
		""" Редактирование названия назначения """
		analytics_item            = C90_AnalyticsItem(self.processing_ido)
		parent_name : str         = C90_AnalyticsItem(self.processing_parent).name or "Структура аналитики"

		destination : str | None  = RequestText("Структура аналитики", f"{parent_name}/{analytics_item.name}", analytics_item.name)
		if destination is None                  : return
		if destination in self.Analytics.Names(): return

		analytics_item.name = destination

		self.on_DestinationChanged()

	def DeleteDestination(self):
		""" Удаление назначения """
		idos : list[str] = self.Analytics.Idos(self.processing_ido)

		if idos:
			parent_name = C90_AnalyticsItem(self.processing_parent).name or "Корневой уровень"

			if RequestConfirm("Удаление назначения", f"Перенести дочерние элементы на место <{parent_name}>?"):
				for ido in idos: C90_AnalyticsItem(ido).parent_ido = self.processing_parent
				idos.clear()
			else:
				for ido in idos: idos.extend(self.Analytics.Idos(ido))

		idos.append(self.processing_ido)

		for ido in idos: C90_AnalyticsItem(ido).DeleteObject(CONTAINERS.DISK)

		self.on_StructChanged()

# АНАЛИТИКА ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 12 апр 2025

from L80_analytics import C80_Analytics, C80_AnalyticsItem


class C90_AnalyticsItem(C80_AnalyticsItem):
	""" Элемент аналитики данных: Логика управления """

	def on_ObjectRegistered(self, container_name: str):
		""" Объект создан """
		self.name    = ""
		self.include = []
		self.exclude = []


class C90_Analytics(C80_Analytics):
	""" Аналитика данных: Логика управления """
	pass

# АНАЛИТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_analytics import C80_Analytics, C80_AnalyticsItem


class C90_AnalyticsItem(C80_AnalyticsItem):
	""" Элемент аналитики: Логика управления """

	def on_ObjectRegistered(self, container_name: str):
		""" Объект зарегистрирован """
		self.Name("")
		self.Include([])
		self.Exclude([])


class C90_Analytics(C80_Analytics):
	""" Аналитика: Логика управления """
	pass

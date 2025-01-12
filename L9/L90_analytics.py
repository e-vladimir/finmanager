# АНАЛИТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_analytics import C80_AnalyticsItem, C80_Analytics


class C90_AnalyticsItem(C80_AnalyticsItem):
	""" Элемент аналитики: Логика управления """

	def on_ObjectRegistered(self, container_name: str):
		""" Объект зарегистрирован """
		self.Name("")
		self.Include([])
		self.Exclude([])
		self.VolumeTitle("")
		self.VolumeValue(0)


class C90_Analytics(C80_Analytics):
	""" Аналитика: Логика управления """
	pass

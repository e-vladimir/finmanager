# АНАЛИТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_analytics import C80_AnalyticsItem


class C90_AnalyticsItem(C80_AnalyticsItem):
	""" Фрагмент аналитики: Логика управления """

	def on_ObjectRegistered(self, container_name: str):
		""" Выполнена регистрация объекта """
		self.Name("")
		self.LabelsInclude([])
		self.LabelsExclude([])

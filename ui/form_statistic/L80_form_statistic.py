# ФОРМА СТАТИСТИКА: ЛОГИКА ДАННЫХ

from L00_containers     import CONTAINERS
from L70_form_statistic import C70_FormStatistic
from L90_analytics      import C90_AnalyticsItem


class C80_FormStatistic(C70_FormStatistic):
	""" Форма Статистика: Логика данных """

	# Модель данных аналитики
	def ShowAnalytics(self):
		""" Отображение аналитики """
		for self._processing_ido in C90_AnalyticsItem.Idos(CONTAINERS.DISK).data:
			self.LoadAnalyticsItemToModelAnalytics()

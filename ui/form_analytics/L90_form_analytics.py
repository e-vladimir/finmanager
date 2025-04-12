# ФОРМА АНАЛИТИКА ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 11 апр 2025

from L80_form_analytics import C80_FormAnalytics


class C90_FormAnalytics(C80_FormAnalytics):
	""" Форма Аналитика данных: Логика управления """

	# Форма
	def on_Opened(self):
		""" Форма открыта """
		self.ShowTitle()

		self.InitModelDataItems()
		self.LoadAnalyticsItems()
		self.AdjustListItems_Sort()

		self.InitModelDataItem()

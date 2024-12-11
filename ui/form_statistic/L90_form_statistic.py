# ФОРМА СТАТИСТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_statistic import C80_FormStatistic


class C90_FormStatistic(C80_FormStatistic):
	""" Форма Статистика: Логика управления """

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.InitModelStatistic()
		self.LoadStatisticInModelStatistic()
		self.AdjustTableStatistic_Size()
		self.AdjustTableStatistic_Sort()

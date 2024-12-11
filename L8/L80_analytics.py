# АНАЛИТИКА: ЛОГИКА ДАННЫХ

from L20_data_struct import T20_StatisticItem
from L70_analytics   import C70_AnalyticsItem
from L90_operations  import C90_Operation, C90_Operations


class C80_AnalyticsItem(C70_AnalyticsItem):
	""" Фрагмент аналитики: Логика данных """

	# Захват данных
	def CaptureAmountsInDm(self, dy: int, dm: int) -> T20_StatisticItem:
		""" Захват данных за указанный месяц """
		amounts        : list[int] = []

		labels_include : set[str]  = set(self.LabelsInclude())
		labels_exclude : set[str]  = set(self.LabelsExclude())

		operations                 = C90_Operations()

		for ido in operations.OperationsIdosInDyDmDd(dy, dm):
			operation         = C90_Operation(ido)

			labels : set[str] = set(operation.Labels())

			if len(labels.intersection(labels_include)) == 0: continue
			if len(labels.intersection(labels_exclude))  > 0: continue

			amounts.append(int(operation.Amount()))

		amount_income  : int       = sum(filter(lambda amount: amount > 0, amounts))
		amount_outcome : int       = sum(filter(lambda amount: amount < 0, amounts))

		return T20_StatisticItem(self.Name(), amount_income, amount_outcome)

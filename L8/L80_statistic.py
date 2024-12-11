# СТАТИСТИКА: ЛОГИКА ДАННЫХ

from collections     import defaultdict

from L20_data_struct import T20_StatisticItem
from L70_statistic   import C70_Statistic
from L90_operations  import C90_Operation, C90_Operations


class C80_Statistic(C70_Statistic):
	""" Статистика: Логика данных """

	# Сбор данных
	def CaptureDataInDm(self, dy: int, dm: int) -> list[T20_StatisticItem]:
		""" Сбор данных по всем меткам в пределах месяца  """
		operations                           = C90_Operations()

		data   : defaultdict[str, list[int]] = defaultdict(list)

		for ido in operations.OperationsIdosInDyDmDd(dy, dm):
			operation          = C90_Operation(ido)

			amount : int       = int(operation.Amount())
			labels : list[str] = operation.Labels()

			for label in labels: data[label].append(amount)

		result : list[T20_StatisticItem]     = []
		for label, amounts in data.items():
			amount_income  : int = sum(filter(lambda amount: amount > 0, amounts))
			amount_outcome : int = sum(filter(lambda amount: amount < 0, amounts))

			result.append(T20_StatisticItem(label, amount_income, amount_outcome))

		return result

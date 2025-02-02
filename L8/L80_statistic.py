# СТАТИСТИКА: ЛОГИКА ДАННЫХ

from collections          import defaultdict

from L20_struct_statistic import T20_StructStatistic
from L70_statistic        import C70_Statistic
from L90_operations       import C90_Operation, C90_Operations


class C80_Statistic(C70_Statistic):
	""" Статистика: Логика данных """

	# Выборка данных
	def CaptureDestinationsInDm(self, dy: int, dm: int) -> list[T20_StructStatistic]:
		""" Захват данных по назначению за месяц """
		data   : defaultdict[str, list[float]]  = defaultdict(list)

		for ido in C90_Operations.OperationsIdosInDyDmDd(dy, dm):
			operation = C90_Operation(ido)
			data[operation.Destination()].append(operation.Amount())

		result : list[T20_StructStatistic]      = list()

		for destination, amounts in data.items():
			if not destination: continue
			result.append(T20_StructStatistic(destination,
			                                  int(sum(filter(lambda amount: amount > 0, amounts))),
			                                  int(sum(filter(lambda amount: amount < 0, amounts)))
			                                  )
			              )

		return result

	def CaptureObjectsIntInDm(self, dy: int, dm: int) -> list[T20_StructStatistic]:
		""" Захват данных по объектам внутренним за месяц """
		data   : defaultdict[str, list[float]]  = defaultdict(list)

		for ido in C90_Operations.OperationsIdosInDyDmDd(dy, dm):
			operation = C90_Operation(ido)
			data[operation.ObjectInt()].append(operation.Amount())

		result : list[T20_StructStatistic]      = list()

		for object_int, amounts in data.items():
			if not object_int: continue
			result.append(T20_StructStatistic(object_int,
			                                  int(sum(filter(lambda amount: amount > 0, amounts))),
			                                  int(sum(filter(lambda amount: amount < 0, amounts)))
			                                  )
			              )

		return result

	def CaptureObjectsExtInDm(self, dy: int, dm: int) -> list[T20_StructStatistic]:
		""" Захват данных по объектам внешним за месяц """
		data   : defaultdict[str, list[float]]  = defaultdict(list)

		for ido in C90_Operations.OperationsIdosInDyDmDd(dy, dm):
			operation = C90_Operation(ido)
			data[operation.ObjectExt()].append(operation.Amount())

		result : list[T20_StructStatistic]      = list()

		for object_ext, amounts in data.items():
			if not object_ext: continue
			result.append(T20_StructStatistic(object_ext,
			                                  int(sum(filter(lambda amount: amount > 0, amounts))),
			                                  int(sum(filter(lambda amount: amount < 0, amounts)))
			                                  )
			              )

		return result

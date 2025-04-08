# ПРЕДИКТИВНЫЙ АНАЛИЗАТОР ДАННЫХ: ЛОГИКА ДАННЫХ
# 08 апр 2025
import operator

from L20_finmanager_struct import T20_PredictItem
from L70_data_completer    import C70_DataCompleter


class C80_DataCompleter(C70_DataCompleter):
	""" Предиктивный анализатор данных: Логика данных """

	# Предиктивная модель определения назначения
	def PredictDestination(self, description: str) -> str:
		""" Предиктивное определение назначения """
		return self._data_destination.get(description, T20_PredictItem()).output or description

	def PredictDestinations(self, description: str) -> list[str]:
		""" Предиктивное определение назначения """
		return (dict(
				sorted(self._data_destination.get(description,
				                                  T20_PredictItem()).outputs.items(),
				       key=operator.itemgetter(1))).keys()
		        or [description])

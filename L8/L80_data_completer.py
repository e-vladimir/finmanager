# ПРЕДИКТИВНЫЙ АНАЛИЗАТОР ДАННЫХ: ЛОГИКА ДАННЫХ
# 08 апр 2025

from L20_finmanager_struct import T20_PredictItem
from L70_data_completer    import C70_DataCompleter


class C80_DataCompleter(C70_DataCompleter):
	""" Предиктивный анализатор данных: Логика данных """

	# Предиктивная модель определения назначения
	def PredictDestination(self, description: str) -> str:
		""" Предиктивное определение назначения """
		data = list(self._data_destination.get(description, T20_PredictItem()).data.items())
		data = sorted(data, key=lambda item: item[1] * 100 + len(item[0]), reverse=True)

		if not data: return ""

		return data[0][0]

	def PredictDestinations(self, description: str) -> list[str]:
		""" Предиктивное определение назначения """
		data = list(self._data_destination.get(description, T20_PredictItem()).data.items())
		data = sorted(data, key=lambda item: item[1] * 100 + len(item[0]), reverse=True)
		return list([item[0] for item in data])


	# Предиктивная модель определения меток
	def PredictLabels(self, description: str, destination: str) -> list[str]:
		""" Предиктивное определение меток """
		return []

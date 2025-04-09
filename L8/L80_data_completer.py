# ПРЕДИКТИВНЫЙ АНАЛИЗАТОР ДАННЫХ: ЛОГИКА ДАННЫХ
# 08 апр 2025

import operator

from   L20_finmanager_struct import T20_PredictItem
from   L70_data_completer    import C70_DataCompleter


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


	# Предиктивная модель определения меток
	def PredictLabels(self, description: str, destination: str) -> list[str]:
		""" Предиктивное определение меток """
		labels     : dict[str, float] = dict()

		src        : str              = f"{description} {destination}".lower()

		for label, predict_item in self._data_labels.items():
			processing_weight : float = 0.00

			for word, weight in predict_item.inputs.items():
				if word not in src: continue
				processing_weight += weight

			if processing_weight < 0.05 : continue

			labels[label] = processing_weight

		if not labels: return []

		result     : list[str]        = []

		for label, weight in labels.items():
			if weight < 0.50: continue

			result.append(label)

		return result

# ПРЕДИКТИВНЫЙ АНАЛИЗАТОР ДАННЫХ: ЛОГИКА ДАННЫХ
# 08 апр 2025

from L20_finmanager_struct import T20_PredictDescriptionItem
from L70_data_completer    import C70_DataCompleter


class C80_DataCompleter(C70_DataCompleter):
	""" Предиктивный анализатор данных: Логика данных """

	# Управление
	def Start(self):
		""" Запуск """
		self.on_Started()

	# Предиктивная модель определения описания
	def PredictDescription(self, description: str) -> str:
		""" Предиктивное определение описания """
		data = list(self._data_descriptions.get(description, T20_PredictDescriptionItem()).data.items())
		data = sorted(data, key=lambda item: item[1] * 100 + len(item[0]), reverse=True)

		if not data: return ""

		return data[0][0]

	def PredictDescriptions(self, description: str) -> list[str]:
		""" Предиктивное определение описаний """
		data = list(self._data_descriptions.get(description, T20_PredictDescriptionItem()).data.items())
		data = sorted(data, key=lambda item: item[1] * 100 + len(item[0]), reverse=True)
		return list([item[0] for item in data])


	# Предиктивная модель назначения
	def PredictDestination(self, description: str) -> list[str]:
		""" Предиктивное определение назначения """
		predicted_tags = self.data_predict_destinations.inverse_transform(self.model_predict_destinations.predict(self.vectorizer_predict_destination.transform([description])))
		return sorted(list(predicted_tags[0]))

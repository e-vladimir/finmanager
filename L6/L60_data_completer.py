# ПРЕДИКТИВНЫЙ АНАЛИЗАТОР ДАННЫХ: МЕХАНИКА ДАННЫХ
# 08 апр 2025

import pandas

from   sklearn.model_selection import train_test_split

from   G10_datetime            import CurrentDy
from   G30_cactus_datafilters  import C30_FilterLinear1D

from   L00_containers          import CONTAINERS
from   L20_finmanager_struct   import T20_PredictDescriptionItem
from   L50_data_completer      import C50_DataCompleter
from   L90_operations          import C90_Operation


class C60_DataCompleter(C50_DataCompleter):
	""" Предиктивный анализатор данных: Механика данных """

	# Исходные данные по операциям
	def ClearDataOperations(self):
		""" Сброс данных """
		self._data_operations.clear()

	def ReadDataOperations(self):
		""" Чтение из БД """
		operation                       = C90_Operation()
		idc                 : str       = operation.Idc().data
		idp_dy              : str       = operation.FDy.Idp().data
		idp_src_description : str       = operation.FSrcDescription.Idp().data

		filter_data                     = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_src_description, "", True)
		filter_data.FilterIdpVlpByMore(idp_dy, CurrentDy() - 3)
		filter_data.Capture(CONTAINERS.DISK)

		idos                : list[str] = filter_data.Idos().data

		for ido in idos: self._data_operations[ido] = C90_Operation(ido).ToT20_RawOperation()

		self.on_DataOperationsLoaded()

	def UpdateDescriptionInDataOperations(self, ido: str):
		""" Обновление данных """
		self._data_operations[ido] = C90_Operation(ido).ToT20_RawOperation()

		self.on_RequestCalcDataDescriptions()

	def UpdateDestinationInDataOperations(self, ido: str):
		""" Обновление данных """
		self._data_operations[ido] = C90_Operation(ido).ToT20_RawOperation()

		self.on_RequestCalcDataDestinations()

	# Данные предиктивного определения описания
	def CalcDataDescriptions(self):
		""" Формирование данных """
		self._data_descriptions.clear()

		for operation in self._data_operations.values():
			if not operation.description: continue
			if     operation.src_description not in self._data_descriptions: self._data_descriptions[operation.src_description] = T20_PredictDescriptionItem()

			processing_string : str = ""

			for word in operation.description.split(' '):
				processing_string = (processing_string + ' ' + word).strip()

				self._data_descriptions[operation.src_description].Append(processing_string)


	# Данные предиктивного определения назначения
	def CalcDataDestinations(self):
		""" Обучение модели предиктивного определения назначения """
		data          = []

		for operation in self._data_operations.values():
			if not operation.destination: continue

			data.append({"description": operation.description or operation.src_description, "destination": operation.destination})

		data_frame    = pandas.DataFrame(data)
		descriptions  = data_frame["description"]
		destinations  = data_frame["destination"]

		y             = self.data_predict_destinations.fit_transform(destinations)
		X_train, X_test, y_train, y_test = train_test_split(descriptions, y, test_size=0.3, random_state=42)
		X_train_tfidf = self.vectorizer_predict_destination.fit_transform(X_train)

		self.model_predict_destinations.fit(X_train_tfidf, y_train)

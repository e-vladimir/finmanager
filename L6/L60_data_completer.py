# ПРЕДИКТИВНЫЙ АНАЛИЗАТОР ДАННЫХ: МЕХАНИКА ДАННЫХ
# 08 апр 2025

from G10_datetime           import CurrentDy
from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L20_finmanager_struct  import T20_PredictItem
from L50_data_completer     import C50_DataCompleter
from L90_operations         import C90_Operation


class C60_DataCompleter(C50_DataCompleter):
	""" Предиктивный анализатор данных: Механика данных """

	# Исходные данные по операциям
	def ClearDataOperations(self):
		""" Сброс данных """
		self._data_operations.clear()

	def ReadDataOperations(self):
		""" Чтение из БД """
		operation                   = C90_Operation()
		idc             : str       = operation.Idc().data
		idp_dy          : str       = operation.FDy.Idp().data
		idp_description : str       = operation.FDescription.Idp().data
		idp_destination : str       = operation.FDestination.Idp().data

		filter_data                 = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_description, "", True)
		filter_data.FilterIdpVlpByEqual(idp_destination, "", True)
		filter_data.FilterIdpVlpByMore(idp_dy, CurrentDy() - 3)
		filter_data.Capture(CONTAINERS.DISK)

		idos            : list[str] = filter_data.Idos().data

		for ido in idos[-300:]: self.AppendDataOperations(ido)

	def AppendDataOperations(self, ido: str):
		""" Добавление данных """
		data = C90_Operation(ido).ToT20_RawOperation()
		if data in self._data_operations: self._data_operations.remove(data)

		self._data_operations.add(data)


	# Данные предиктивного определения назначения
	def CalcDataDestination(self):
		""" Формирование данных """
		self._data_destination.clear()

		for operation in self._data_operations:
			predict_item                                  = self._data_destination.get(operation.description, T20_PredictItem())
			predict_item.IncOutputs([operation.destination])

			self._data_destination[operation.description] = predict_item

		for description, predict_item in self._data_destination.items():
			predict_item.CalcOutputsWights()
			predict_item.CalcOutput()


	# Данные предиктивного определения меток
	def CalcDataLabels(self):
		""" Формирование данных """
		self._data_labels.clear()

		for operation in self._data_operations:
			if not operation.labels: continue

			for label in operation.labels:
				predict_item = self._data_labels.get(label, T20_PredictItem())
				predict_item.IncInputs(operation.description.lower().split(' '))
				predict_item.IncInputs(operation.destination.lower().split(' '))

				self._data_labels[label] = predict_item

		for label, predict_item in self._data_labels.items():
			predict_item.CalcInputsWights()

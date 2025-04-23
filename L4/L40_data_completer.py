# ПРЕДИКТИВНЫЙ АНАЛИЗАТОР ДАННЫХ: МОДЕЛЬ ДАННЫХ
# 08 апр 2025

from G31_cactus_frame      import C31_StructFrameWithEvents

from L20_finmanager_struct import T20_PredictItem, T20_RawOperation


class C40_DataCompleter(C31_StructFrameWithEvents):
	""" Предиктивный анализатор данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._data_operations  : dict[str, T20_RawOperation] = dict()
		self._data_destination : dict[str, T20_PredictItem]  = dict()

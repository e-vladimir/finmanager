# ФИНАНАЛИТИКА: МОДЕЛЬ ДАННЫХ

from G20_meta_frame import C20_MetaFrame

from L90_finactions import C90_Finactions


class C40_Finanalitics(C20_MetaFrame):
	""" Финаналитика: Модель данных """

	def Init_00(self):
		self._labels_include : list[str]      = []
		self._labels_exclude : list[str]      = []

		self._processing_dy  : int            = 0
		self._processing_dm  : int            = 0

		self._data           : dict[str, any] = dict()

	def Init_10(self):
		self.finactions = C90_Finactions()

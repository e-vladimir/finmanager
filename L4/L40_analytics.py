# АНАЛИТИКА: МОДЕЛЬ ДАННЫХ

from G30_cactus_frame import C30_StructField
from G31_cactus_frame import C31_StructFrameWithEvents


class C40_AnalyticsItem(C31_StructFrameWithEvents):
	""" Элемент аналитики: Модель данных """

	_idc = "Фрагмент аналитики"

	def Init_10(self):
		super().Init_10()

		self.f_name           = C30_StructField(self, "Наименование")
		self.f_labels_include = C30_StructField(self, "Метки включения")
		self.f_labels_exclude = C30_StructField(self, "Метки исключения")

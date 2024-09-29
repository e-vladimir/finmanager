# ФОРМА ФИНАНАЛИТИКА: ЛОГИКА ДАННЫХ

from L70_form_finanalitics import C70_FormFinanalitics


class C80_FormFinanalitics(C70_FormFinanalitics):
	""" Форма Финаналитика: Логика данных """

	# Модель параметров
	def LoadOptionsLabels(self):
		""" Загрузка параметров: Метки """
		for self._processing_label in self.finanalitics.Labels(): self.LoadLabelInModelOptions()

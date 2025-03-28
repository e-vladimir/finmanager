# ФОРМА ОБРАБОТКА ДАННЫХ: МОДЕЛЬ СОБЫТИЙ
# 22 мар 2025

from L42_form_processing import C42_FormProcessing


class C50_FormProcessing(C42_FormProcessing):
	""" Форма Обработка данных: Модель событий """

	# Вкладки режимов обработки
	def on_TabMainChanged(self): pass

	# Меню ручной обработки данных
	def on_RequestShowMenuManual(self): pass

	# Меню автоматической обработки данных
	def on_RequestShowMenuAuto(self): pass

	# Параметры ручной обработки данных
	def on_RequestSwitchProcessingObjectsTypeToOperations(self): pass
	def on_RequestEditOptionsManual(self): pass

	def on_ProcessingObjectsTypeChanged(self): pass
	def on_OptionsManualChanged(self): pass

	def on_RequestManualProcessing(self): pass

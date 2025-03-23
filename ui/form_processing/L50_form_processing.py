# ФОРМА ОБРАБОТКА ДАННЫХ: МОДЕЛЬ СОБЫТИЙ
# 22 мар 2025

from L42_form_processing import C42_FormProcessing


class C50_FormProcessing(C42_FormProcessing):
	""" Форма Обработка данных: Модель событий """

	# Параметры Обработка операций
	def on_RequestSetOperationsDescriptionInclude(self): pass
	def on_RequestSetOperationsDescriptionEqual(self): pass
	def on_RequestSetOperationsDescriptionReplace(self): pass
	def on_RequestSetOperationsDescriptionSet(self): pass
	def on_RequestSetOperationsColorSet(self): pass

	def on_ProcessingOperationsChanged(self): pass

	# Дерево данных Обработка операций
	def on_TreeDataProcessingOperationsDoubleClicked(self): pass

	# Меню Обработка операций
	def on_RequestShowMenuOperations(self): pass

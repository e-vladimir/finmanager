# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: МОДЕЛЬ СОБЫТИЙ

from L42_form_record_finactions import C42_FormRecordFinactions


class C50_FormRecordFinactions(C42_FormRecordFinactions):
	""" Форма Запись финдействий: Модель событий """

	# Данные записи финдействий
	def on_DataChanged(self): pass

	# Таблица данных
	def on_RequestProcessingTblDataClick(self): pass

	# Дерево значений
	def on_RequestProcessingTreValuesClick(self): pass
	def on_RequestIncludeValue(self): pass
	def on_RequestExcludeValue(self): pass

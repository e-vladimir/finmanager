# ФОРМА УПРАВЛЕНИЕ НАЗНАЧЕНИЕМ: МОДЕЛЬ СОБЫТИЙ

from L42_form_control_destination import C42_FormControlDestination


class C50_FormControlDestination(C42_FormControlDestination):
	""" Форма Управление назначением: Модель событий """

	# Меню сопоставления назначения
	def on_RequestShowMenuRules(self): pass

	# Таблица правил
	def on_RequestProcessingTableRules_DbClick(self): pass

	# Правила сопоставления назначения
	def on_RequestApplyRules(self): pass

	# Правило сопоставления назначения
	def on_RequestCreateRule(self): pass
	def on_RequestDeleteRule(self): pass
	def on_RequestEditInput(self): pass
	def on_RequestEditOutput(self): pass

	# Список доступных фрагментов
	def on_RequestListControlReplaceAvailable_DbClick(self): pass

	# Вкладка Поиск и замена
	def on_RequestExecReplace(self): pass

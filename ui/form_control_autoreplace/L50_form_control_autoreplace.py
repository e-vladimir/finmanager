# ФОРМА УПРАВЛЕНИЕ АВТОЗАМЕНОЙ: МОДЕЛЬ СОБЫТИЙ

from L42_form_control_autoreplace import C42_FormControlAutoreplace


class C50_FormControlAutoreplace(C42_FormControlAutoreplace):
	""" Форма Управление автозаменой: Модель событий """

	# Меню правил автозамены
	def on_RequestShowMenuRules(self): pass

	# Правило автозамены
	def on_RequestCreateRule(self): pass
	def on_RequestEditInput(self): pass
	def on_RequestEditOutput(self): pass

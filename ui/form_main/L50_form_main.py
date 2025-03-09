# ФОРМА ОСНОВНАЯ: МОДЕЛЬ СОБЫТИЙ
# 12 фев 2025

from L42_form_main import C42_FormMain


class C50_FormMain(C42_FormMain):
	""" Форма Основная: Модель событий """

	# Рабочий период
	def on_RequestSwitchDyDmToNextDm(self): pass
	def on_RequestSwitchDyDmToPrevDm(self): pass
	def on_RequestEditDyDm(self): pass

	def on_DyDmChanged(self): pass

	# Счета
	def on_RequestOpenAccounts(self): pass

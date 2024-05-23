# ФОРМА ФИНАНАЛИЗ: МОДЕЛЬ СОБЫТИЙ

from L42_form_finanalytics import C42_FormFinanalytics


class C50_FormFinanalytics(C42_FormFinanalytics):
	""" Форма Финанализ: Модель событий """

	# Динамика финсостава
	def on_RequestShowFindescriptionDynamic(self): pass
	def on_RequestIncFindescriptionDynamic(self): pass
	def on_RequestDecFindescriptionDynamic(self): pass

	# Меню динамики финсостава
	def on_RequestShowMenuFindescriptionDynamic(self): pass

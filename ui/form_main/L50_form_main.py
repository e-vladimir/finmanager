# ФОРМА ОСНОВНАЯ: МОДЕЛЬ СОБЫТИЙ

from L42_form_main import C42_FormMain


class C50_FormMain(C42_FormMain):
	""" Форма основная: Модель событий """

	# Финпериод
	def on_RequestNextDm(self): pass
	def on_RequestPrevDm(self): pass

	def on_SwitchDyDm(self):    pass

	# Каталоги
	def on_RequestOpenFindescription(self): pass

	# Оперативные данные
	def on_RequestOpenFinstruct(self): pass

	# Инструментарий
	def on_RequestOpenRules(self): pass

	# Аналитика
	def on_RequestOpenFinstatistic(self): pass
	def on_RequestOpenFinanalytics(self): pass

	# Отчётность
	def on_RequestSummaryReport(self): pass
	def on_RequestFinstateReport(self): pass

	# Утилиты
	def on_RequestOpenCleaner(self): pass

	def on_RequestOpenBackups(self): pass

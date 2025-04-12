# ФОРМА АНАЛИТИКА ДАННЫХ: МОДЕЛЬ UI
# 11 апр 2025

from L20_PySide6        import C20_PySideForm
from L40_form_analytics import Ui_FormAnalytics


class C41_FormAnalytics(C20_PySideForm, Ui_FormAnalytics):
	""" Форма Аналитика данных: Модель UI """

	def InitUi(self): self.setupUi(self)

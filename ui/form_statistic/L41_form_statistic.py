# ФОРМА СТАТИСТИКА: МОДЕЛЬ UI

from L20_PySide6        import C20_PySideForm
from L40_form_statistic import Ui_frm_statistic


class C41_FormStatistic(C20_PySideForm, Ui_frm_statistic):
	""" Форма Статистика: Модель UI """

	def InitUi(self): self.setupUi(self)

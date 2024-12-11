# ФОРМА СТАТИСТИКА: МОДЕЛЬ ДАННЫХ

from L20_PySide6        import C20_StandardItemModel
from L41_form_statistic import C41_FormStatistic
from L90_statistic      import C90_Statistic
from L90_workspace      import C90_Workspace


class C42_FormStatistic(C41_FormStatistic):
	""" Форма Статистика: Модель данных """

	def Init_10(self):
		super().Init_10()

		self.model_statistic = C20_StandardItemModel()

		self.statistic       = C90_Statistic()
		self.workspace       = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.table_statistic.setModel(self.model_statistic)

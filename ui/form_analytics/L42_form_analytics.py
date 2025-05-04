# ФОРМА АНАЛИТИКА ДАННЫХ: МОДЕЛЬ ДАННЫХ
# 27 апр 2025

from L20_PySide6        import C20_StandardItemModel
from L41_form_analytics import C41_FormAnalytics
from L90_analytics      import C90_Analytics
from L90_workspace      import C90_Workspace


class C42_FormAnalytics(C41_FormAnalytics):
	""" Форма Аналитика данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_ido    : str = ""
		self._processing_group  : str = ""
		self._processing_parent : str = ""

	def Init_10(self):
		super().Init_10()

		self.ModelData = C20_StandardItemModel()

		self.Analytics = C90_Analytics()
		self.Workspace = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.Workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.TreeData.setModel(self.ModelData)

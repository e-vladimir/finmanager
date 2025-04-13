# ФОРМА АНАЛИТИКА ДАННЫХ: МОДЕЛЬ ДАННЫХ
# 11 апр 2025

from L00_form_analytics import ANALYTICS_FIELDS
from L20_PySide6        import C20_StandardItemModel
from L41_form_analytics import C41_FormAnalytics
from L90_analytics      import C90_Analytics
from L90_operations     import C90_Operations
from L90_workspace      import C90_Workspace


class C42_FormAnalytics(C41_FormAnalytics):
	""" Форма Аналитика данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_ido   : str              = ""
		self._processing_field : ANALYTICS_FIELDS = ANALYTICS_FIELDS.NONE

	def Init_10(self):
		super().Init_10()

		self.ModelDataItem  = C20_StandardItemModel()
		self.ModelDataItems = C20_StandardItemModel()

		self.Analytics      = C90_Analytics()
		self.Operations     = C90_Operations()
		self.Workspace      = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.Workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.ListDataItems.setModel(self.ModelDataItems)
		self.TreeDataItem.setModel(self.ModelDataItem)

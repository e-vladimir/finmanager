# ФОРМА АНАЛИТИКА: МОДЕЛЬ ДАННЫХ

from L20_PySide6        import C20_StandardItemModel
from L41_form_analytics import C41_FormAnalytics
from L90_analytics      import C90_Analytics
from L90_operations     import C90_Operations
from L90_workspace      import C90_Workspace


class C42_FormAnalytics(C41_FormAnalytics):
	""" Форма Аналитика: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_ido : str = ""

	def Init_10(self):
		super().Init_10()

		self.model_items     = C20_StandardItemModel()
		self.model_item      = C20_StandardItemModel()
		self.model_dm        = C20_StandardItemModel()
		self.model_dy        = C20_StandardItemModel()
		self.model_analytics = C20_StandardItemModel()

		self.analytics       = C90_Analytics()
		self.operations      = C90_Operations()
		self.workspace       = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.list_items.setModel(self.model_items)
		self.tree_data_item.setModel(self.model_item)
		self.tree_data_dm.setModel(self.model_dm)
		self.tree_data_dy.setModel(self.model_dy)

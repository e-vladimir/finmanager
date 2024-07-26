# ФОРМА ФИНАНАЛИЗ: МОДЕЛЬ ДАННЫХ

from L20_PySide6           import C20_StandardItemModel
from L41_form_finanalytics import C41_FormFinanalytics
from L90_findescription    import C90_Findescription
from L90_finstatistic      import C90_Finstatistic
from L90_workspace         import C90_Workspace


class C42_FormFinanalytics(C41_FormFinanalytics):
	""" Форма Финанализ: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._ido_processing                      : str                  = ""

		self._idos_findescription_dynamic         : list[str]            = []
		self._data_findescription_dynamic_income  : dict[str, list[int]] = dict()
		self._data_findescription_dynamic_outcome : dict[str, list[int]] = dict()

	def Init_10(self):
		super().Init_10()

		self.model_findescription_dynamic = C20_StandardItemModel(None)

		self.findescription               = C90_Findescription()
		self.finstatistic                 = C90_Finstatistic()

		self.workspace                    = C90_Workspace()

	def Init_20(self):
		super().Init_20()

		self.table_findescription_dynamic.setModel(self.model_findescription_dynamic)

		self.workspace.SwitchToMain()

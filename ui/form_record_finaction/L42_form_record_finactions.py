# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: МОДЕЛЬ ДАННЫХ

from L20_PySide6                import C20_StandardItemModel
from L41_form_record_finactions import C41_FormRecordFinactions
from L90_finactions             import C90_RecordFinactions
from L90_findescription         import C90_Findescription
from L90_finstruct              import C90_Finstruct
from L90_workspace              import C90_Workspace


class C42_FormRecordFinactions(C41_FormRecordFinactions):
	""" Форма Запись финдействий: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._ido_processing   : str = ""
		self._name_processing  : str = ""
		self._value_processing : str = ""

	def Init_10(self):
		super().Init_10()

		self.model_data        = C20_StandardItemModel(None)
		self.model_values      = C20_StandardItemModel(None)

		self.finstruct         = C90_Finstruct()
		self.findescription    = C90_Findescription()
		self.record_finactions = C90_RecordFinactions()

		self.workspace         = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.tbl_data.setModel(self.model_data)
		self.tre_values.setModel(self.model_values)

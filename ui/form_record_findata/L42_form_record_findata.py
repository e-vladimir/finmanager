# ФОРМА ЗАПИСИ ФИНДАННЫХ: МОДЕЛЬ ДАННЫХ

from L20_PySide6             import C20_StandardItemModel
from L41_form_record_findata import C41_FormRecordFindata
from L90_findata             import C90_RecordFindata
from L90_finstruct           import C90_Finstruct
from L90_workspace           import C90_Workspace


class C42_FormRecordFindata(C41_FormRecordFindata):
	""" Форма записи финданных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._lock_reading     : bool = False
		self._row_processing   : int  = -1
		self._oid_processing   : str  = ""

	def Init_10(self):
		super().Init_10()

		self.record_findata = C90_RecordFindata()

		self.finstruct      = C90_Finstruct()

		self.workspace      = C90_Workspace()

		self.model_data     = C20_StandardItemModel(None)
		self.model_values   = C20_StandardItemModel(None)

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.table_data.setModel(self.model_data)
		self.table_values.setModel(self.model_values)

# ФОРМА ФИНДАННЫЕ: МОДЕЛЬ ДАННЫХ

from L20_PySide6        import C20_StandardItemModel
from L41_form_findata   import C41_FormFindata
from L90_finactions     import C90_Finactions
from L90_findata        import C90_Findata
from L90_findescription import C90_Findescription
from L90_finstruct      import C90_Finstruct
from L90_workspace      import C90_Workspace


class C42_FormFindata(C41_FormFindata):
	""" Форма Финданные: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._dd_processing              : int       =  0
		self._index_col_processing       : int       = -1

		self._flag_processing_quick      : bool      = False
		self._flag_processing_dec        : bool      = False
		self._flag_processing_skip       : bool      = False

		self._oid_processing_findata     : str       = ""
		self._oid_processing_finactions  : str       = ""

		self._oids_processing_findata    : list[str] = []
		self._oids_processing_finactions : list[str] = []

	def Init_10(self):
		super().Init_10()

		self.model_data = C20_StandardItemModel(None)

		self.finactions = C90_Finactions()
		self.findata    = C90_Findata()
		self.finstruct  = C90_Finstruct()
		self.findescription = C90_Findescription()

		self.workspace  = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.tree_data.setModel(self.model_data)

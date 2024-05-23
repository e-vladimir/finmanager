# ФОРМА СБРОС ДАННЫХ: МОДЕЛЬ ДАННЫХ

from L20_PySide6          import C20_StandardItemModel
from L41_form_reset       import C41_FormReset
from L90_finactions       import C90_Finactions
from L90_findata          import C90_Findata
from L90_findescription   import C90_Findescription
from L90_finstate         import C90_Finstate
from L90_finstruct        import C90_Finstruct
from L90_processing_rules import C90_ProcessingRules
from L90_workspace        import C90_Workspace


class C42_FormReset(C41_FormReset):
	""" Форма Сброс данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._flag_all_periods                         : bool = False

		self._flag_finstruct                           : bool = False
		self._flag_finactions                          : bool = False
		self._flag_findescription_in_finactions        : bool = False
		self._flag_findescription                      : bool = False
		self._flag_finstate                            : bool = False
		self._flag_findata                             : bool = False
		self._flag_rules_replace_text                  : bool = False
		self._flag_rules_detect_findescription_by_text : bool = False

		self._oids_finstruct                           : list[str] = []
		self._oids_finactions                          : list[str] = []
		self._oids_findescription                      : list[str] = []
		self._oids_findescription_in_finactions        : list[str] = []
		self._oids_finstate                            : list[str] = []
		self._oids_findata                             : list[str] = []
		self._oids_rules                               : list[str] = []

	def Init_10(self):
		super().Init_10()

		self.model_objects  = C20_StandardItemModel(None)

		self.findescription = C90_Findescription()
		self.finstruct      = C90_Finstruct()
		self.finstate       = C90_Finstate()
		self.findata        = C90_Findata()
		self.finactions     = C90_Finactions()
		self.rules          = C90_ProcessingRules()

		self.workspace      = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.tre_objects.setModel(self.model_objects)

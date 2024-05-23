# ГЕНЕТАОР ОТЧЁТОВ: МОДЕЛЬ ДАННЫХ

from pathlib            import Path

from G20_meta_frame     import C20_MetaFrame

from L90_finactions     import C90_Finactions
from L90_findata        import C90_Findata
from L90_findescription import C90_Findescription
from L90_finstate       import C90_Finstate
from L90_finstatistic   import C90_Finstatistic
from L90_finstruct      import C90_Finstruct
from L90_workspace      import C90_Workspace


class C40_Report(C20_MetaFrame):
	""" Генератор отчётов: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._names_processing : list[str]   = []
		self._name_processing  : str         = ""

		self._report_type      : str         = ""
		self._report_dy        : int         = 0
		self._report_dm        : int         = 0
		self._report_data      : list[str]   = []

		self._report_patterns  : list[str]   = [''] * 1000

		self._path_report      : Path | None = None

	def Init_10(self):
		super().Init_10()

		self.finstruct    = C90_Finstruct()
		self.finstate     = C90_Finstate()
		self.findata      = C90_Findata()
		self.finactions   = C90_Finactions()
		self.finstatistic = C90_Finstatistic()
		self.findescription = C90_Findescription()
		self.workspace    = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

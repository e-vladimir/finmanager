# ФОРМА ОСНОВНАЯ: МОДЕЛЬ ДАННЫХ

from L00_reports    import REPORTS
from L41_form_main  import C41_FormMain
from L90_finreports import C90_Finreports
from L90_workspace  import C90_Workspace


class C42_FormMain(C41_FormMain):
	""" Форма основная: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_dy     : int            = 0
		self._processing_dm     : int            = 0

		self._processing_report : REPORTS | None = None

	def Init_10(self):
		super().Init_10()

		self.finreports = C90_Finreports()

		self.workspace  = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.workspace.SwitchToMain()

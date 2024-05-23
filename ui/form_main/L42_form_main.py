# ФОРМА ОСНОВНАЯ: МОДЕЛЬ ДАННЫХ

from L41_form_main import C41_FormMain
from L90_report    import C90_Report
from L90_workspace import C90_Workspace


class C42_FormMain(C41_FormMain):
	""" Форма основная: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._dy           : int = 0
		self._dm           : int = 0

		self._flag_loading : bool = False

	def Init_10(self):
		super().Init_10()

		self.report    = C90_Report()
		self.workspace = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.report.LoadPatterns()

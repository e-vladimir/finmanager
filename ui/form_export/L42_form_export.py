# ФОРМА ЭКСПОРТА: МОДЕЛЬ ДАННЫХ

from pathlib         import Path

from PySide6.QtCore  import QTimer

from L41_form_export import C41_FormExport
from L90_findata     import C90_Findata
from L90_finstruct   import C90_Finstruct
from L90_workspace   import C90_Workspace


class C42_FormExport(C41_FormExport):
	""" Форма экспорта: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._findata_dy                : int         = 0
		self._findata_dm                : int         = 0
		self._findata_finstruct         : str         = ""
		self._findata_filename          : str         = ""
		self._findata_folder            : Path | None = None

		self._flag_loading              : bool        = False
		self._flag_exporting            : bool        = False

		self._statistic_count_total     : int         = 0
		self._statistic_count_processed : int         = 0
		self._statistic_count_left      : int         = 0
		self._statistic_count_exported  : int         = 0
		self._statistic_time_started    : int         = 0
		self._statistic_time_processing : int         = 0
		self._statistic_time_left       : int         = 0

	def Init_10(self):
		super().Init_10()

		self.timer_statistic = QTimer(self)

		self.findata         = C90_Findata()
		self.finstruct       = C90_Finstruct()
		self.workspace       = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.timer_statistic.setInterval(100)

		self.workspace.SwitchToMain()

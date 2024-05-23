# ФОРМА ИМПОРТА ДАННЫХ: МОДЕЛЬ ДАННЫХ

from pathlib         import Path

from PySide6.QtCore  import QTimer

from L41_form_import import C41_FormImport
from L90_findata     import C90_Findata
from L90_finstruct   import C90_Finstruct
from L90_workspace   import C90_Workspace


class C42_FormImport(C41_FormImport):
	""" Форма импорта данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._flag_processing           : bool        = False

		self._findata_path_file         : Path | None = None
		self._findata_finstruct_name    : str         = ""
		self._findata_format            : str         = ""

		self._statistic_count_total     : int         = 0
		self._statistic_count_processed : int         = 0
		self._statistic_count_left      : int         = 0
		self._statistic_count_imported  : int         = 0
		self._statistic_count_skipped   : int         = 0
		self._statistic_time_processed  : int         = 0
		self._statistic_time_left       : int         = 0

		self._statistic_utime_start     : int         = 0

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

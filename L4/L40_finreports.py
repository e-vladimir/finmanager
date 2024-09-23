# ФИНОТЧЁТНОСТЬ: МОДЕЛЬ ДАННЫХ

from pathlib                   import Path

from G20_meta_frame            import C20_MetaFrame

from L00_reports               import REPORTS
from L90_finactions            import C90_Finactions
from L90_finstatistics         import C90_Finstatistics
from L90_finstructs            import C90_Finstruct


class C40_Finreports(C20_MetaFrame):
	""" Финотчётность: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._file_name      : str            = ""
		self._file_path      : Path           = Path()
		self._directory_path : Path           = Path()

		self._report_type    : REPORTS | None = None

		self._dy             : int            = 0
		self._dm             : int            = 0

	def Init_10(self):
		super().Init_10()

		self.finstruct                = C90_Finstruct()
		self.finactions               = C90_Finactions()
		self.finstatistics            = C90_Finstatistics()

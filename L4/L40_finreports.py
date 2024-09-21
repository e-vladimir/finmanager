# ФИНОТЧЁТНОСТЬ: МОДЕЛЬ ДАННЫХ

from pathlib                   import Path
from borb.pdf                  import TrueTypeFont, Document, Page, PageLayout, SingleColumnLayout
from borb.pdf.canvas.font.font import Font

from G20_meta_frame            import C20_MetaFrame

from L00_reports               import REPORTS
from L90_finactions            import C90_Finactions
from L90_finstructs            import C90_Finstruct


class C40_Finreports(C20_MetaFrame):
	""" Финотчётность: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._file_name      : str            = ""
		self._file_path      : Path           = Path()
		self._directory_path : Path           = Path()

		self._report_type    : REPORTS | None = None

	def Init_10(self):
		super().Init_10()

		self.document    : Document   = Document()
		self.page        : Page       = Page()
		self.layout      : PageLayout = SingleColumnLayout(self.page)

		self.font_default: Font       = TrueTypeFont.true_type_font_from_file(Path("./L0/fonts/IBMPlexMono-Regular.ttf"))
		self.font_bold   : Font       = TrueTypeFont.true_type_font_from_file(Path("./L0/fonts/IBMPlexMono-Bold.ttf"))

		self.finstruct                = C90_Finstruct()
		self.finactions               = C90_Finactions()

# ФИНОТЧЁТНОСТЬ: МЕХАНИКА ДАННЫХ

from enum                    import Enum
from pathlib                 import Path

from borb.io.read.types      import Decimal
from borb.pdf                import Page, SingleColumnLayout, PDF, Paragraph, RGBColor, HexColor, FixedColumnWidthTable, TableCell, Alignment
from borb.pdf.page.page_size import PageSize

from L00_reports             import REPORTS
from L50_finreports          import C50_Finreports


K_PAGE_MM = 842 / 297


class C60_Finreports(C50_Finreports):
	""" Финотчётность: Механика данных """

	# Параметры
	def ReportType(self, data: Enum = None) -> Enum:
		""" Тип отчёта """
		if data is None: return self._report_type
		else           :        self._report_type = data

	def DirectoryPath(self, directory: Path = None) -> Path:
		""" Директория отчётов """
		if directory is None: return self._directory_path
		else                :        self._directory_path = directory

	def CalcFilename(self):
		""" Вычисление имени файла """
		match self._report_type:
			case REPORTS.HISTORY_FINSTATE: self._file_name = "Хронология финсостояния"

	# Документ
	def CreateDocument(self):
		""" Создание документа """
		self.document.clear()

	def SaveDocument(self):
		""" Сохранение документа """
		if not self._file_name: return

		file_path = self._directory_path.joinpath(f"{self._file_name}.pdf")

		with open(f"{file_path.absolute()}", "wb") as pdf_file_handle: PDF.dumps(pdf_file_handle, self.document)

	# Страница
	def CreatePage(self):
		""" Создание страницы """
		A4_w, A4_h = PageSize.A4_PORTRAIT.value
		self.page  = Page(A4_w, A4_h)

		self.document.add_page(self.page)

	# Разметка
	def SetupLayoutSingle(self):
		""" Установка линейной разметки """
		margin_l = Decimal(30 * K_PAGE_MM)
		margin_r = Decimal(15 * K_PAGE_MM)
		margin_t = Decimal(10 * K_PAGE_MM)
		margin_b = Decimal(10 * K_PAGE_MM)
		self.layout                = SingleColumnLayout(self.page)
		self.layout._margin_left   = margin_l
		self.layout._margin_right  = margin_r
		self.layout._margin_top    = margin_t
		self.layout._margin_bottom = margin_b

	# Блоки отчёта
	def AppendReportHeader(self):
		""" Добавление заголовка отчёта """
		header : str = ""

		match self._report_type:
			case REPORTS.HISTORY_FINSTATE: header = "ХРОНОЛОГИЯ ФИНСОСТОЯНИЯ"

		if not header: return

		block_header = Paragraph(header,
		                         font          = self.font_bold,
		                         font_size     = Decimal(16))

		self.layout.add(block_header)

	def AppendFinstructHistory(self, finstruct_name: str, data: list):
		""" Добавление таблицы хронологии финструктуры """
		block_header = Paragraph(finstruct_name,
		                         font          = self.font_bold,
		                         font_size     = Decimal(12))

		table        = FixedColumnWidthTable(number_of_columns=6, number_of_rows=len(data) + 1)
		table.add(TableCell(block_header, column_span=6))

		for row_index, row_data in enumerate(data):
			for col_index, col_data in enumerate(row_data):
				block_text = Paragraph(col_data, font=self.font_default,  font_size=Decimal(9))
				cell_text  = TableCell(block_text)

				if col_index  > 0:
					block_text._horizontal_alignment = Alignment.RIGHT

				if row_index == 0:
					block_text._font_color         = HexColor("#FFFFFF")

					cell_text._background_color = HexColor("#262626")

				table.add(cell_text)

		table.set_padding_on_all_cells(Decimal(3), Decimal(2), Decimal(-1), Decimal(2))
		table.set_borders_on_all_cells(False, False, True, False)
		table.set_border_width_on_all_cells(Decimal(0.1))
		table.set_border_color_on_all_cells(HexColor("#AAAAAA"))

		self.layout.add(table)

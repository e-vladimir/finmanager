# ФОРМА ФИНСОСТАВ: ЛОГИКА ДАННЫХ

from L20_PySide6             import RequestText
from L70_form_fincomposition import C70_FormFincomposition
from L90_fincomposition      import C90_FincompositionRecord


class C80_FormFincomposition(C70_FormFincomposition):
	""" Форма Финсостав: Логика данных """

	# Финсостав
	def LoadFincomposition(self):
		""" Загрузка финсостава """
		for self._ido_processing in self.fincomposition.TopIdos(): self.LoadRecordFincomposition()

	# Запись финсостава
	def CreateTopRecordFincomposition(self):
		""" Создание записи финсостава корневого уровня """
		record_name : str | None = RequestText("Управление финсоставом", "Создание записи финсостава корневого уровня")
		if record_name is None: return

		self.fincomposition.CreateRecord(record_name, "")

	def CreateRecordFincomposition(self):
		""" Создание записи финсостава """
		parent_record = C90_FincompositionRecord(self._ido_processing)

		record_name : str | None = RequestText("Управление финсоставом", f"Создание записи финсостава в группе [{parent_record.Name()}]")
		if record_name is None: return

		self.fincomposition.CreateRecord(record_name, self._ido_processing)

# ФОРМА ФИНСОСТАВ: ЛОГИКА ДАННЫХ

from L20_PySide6             import RequestText
from L70_form_fincomposition import C70_FormFincomposition


class C80_FormFincomposition(C70_FormFincomposition):
	""" Форма Финсостав: Логика данных """

	# Финсостав
	def LoadFincomposition(self):
		""" Загрузка финсостава """
		for self._ido_processing in self.fincomposition.TopIdos(): self.LoadRecordFincomposition()

	# Запись финсостава
	def AppendRecordFincompositionToTop(self):
		""" Создание записи финсостава корневого уровня """
		record_name : str | None = RequestText("Управление финсоставом", "Добавление записи финсостава верхнего уровня")
		if record_name is None: return

		self.fincomposition.Append(record_name, "")

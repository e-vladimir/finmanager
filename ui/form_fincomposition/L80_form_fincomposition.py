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
		""" Добавление записи финсостава верхнего уровня """
		record_name : str | None = RequestText("Управление финсоставом", "Добавление записи финсостава верхнего уровня")
		if record_name is None: return

		self.fincomposition.Append(record_name, "")

	def AppendRecordFincomposition(self):
		""" Добавление вложенной записи финсостава """
		record_name : str | None = RequestText("Управление финсоставом", f"Добавление записи финсостава в [{self._name_processing}]")
		if record_name is None: return

		self.fincomposition.Append(record_name, self._name_processing)

	def RenameRecordFincomposition(self):
		""" Изменение наименования записи финсостава """
		record_name : str | None = RequestText("Управление финсоставом", f"Изменение наименования [{self._name_processing}]", self._name_processing)
		if record_name is None: return

		self.fincomposition.Rename(self._name_processing, record_name)

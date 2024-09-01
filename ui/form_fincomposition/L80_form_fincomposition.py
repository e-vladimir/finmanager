# ФОРМА ФИНСОСТАВ: ЛОГИКА ДАННЫХ

from L20_PySide6             import RequestText, RequestConfirm, RequestItem
from L70_form_fincomposition import C70_FormFincomposition
from L90_fincomposition      import C90_FincompositionRecord


class C80_FormFincomposition(C70_FormFincomposition):
	""" Форма Финсостав: Логика данных """

	# Финсостав
	def LoadFincomposition(self):
		""" Загрузка финсостава """
		for self._processing_ido in self.fincomposition.TopIdos(): self.LoadRecordFincomposition()

	# Запись финсостава
	def AppendFincompositionRecordToTop(self):
		""" Добавление записи финсостава верхнего уровня """
		record_name : str | None = RequestText("Управление финсоставом", "Добавление записи финсостава верхнего уровня")
		if record_name is None: return

		self.fincomposition.Append(record_name, "")

	def AppendFincompositionRecord(self):
		""" Добавление вложенной записи финсостава """
		record_name : str | None = RequestText("Управление финсоставом", f"Добавление записи финсостава в [{self._processing_name}]")
		if record_name is None: return

		self.fincomposition.Append(record_name, self._processing_name)

	def RenameFincompositionRecord(self):
		""" Изменение наименования записи финсостава """
		record_name : str | None = RequestText("Управление финсоставом", f"Изменение наименования [{self._processing_name}]", self._processing_name)
		if record_name is None: return

		self.fincomposition.Rename(self._processing_name, record_name)

	def DeleteFincompositionRecord(self):
		""" Удаление записи финсостава """
		mode_move   : str        = "Сместить вложенные записи уровнем выше"
		mode_struct : str        = "Удалить все вложенные записи"

		if not RequestConfirm("Управление финсоставом", f"Подтверждение удаления записи финсостава [{self._processing_name}]"): return

		delete_mode : str | None = RequestItem("Управление финсоставом", "Режим удаления записи финсостава", [mode_move, mode_struct])
		if     delete_mode is None                                                                                            : return

		self.fincomposition.Delete(self._processing_name, delete_mode == mode_struct)

		if not self._name_memory == self._processing_name: return
		self._name_memory = ""

	def MoveUpFincompositionRecord(self):
		""" Перемещение записи финсостава уровне выше """
		if not self._processing_ido: return

		record = C90_FincompositionRecord(self._processing_ido)
		record.MoveUp()

	def PasteFincompositionRecord(self):
		""" Вставка записи финсостава """
		if not self._processing_ido: return

		record = C90_FincompositionRecord()
		record.SwitchByName(self._name_memory)
		record.ParentIdo(self._processing_ido)

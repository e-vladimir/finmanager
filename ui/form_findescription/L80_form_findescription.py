# ФОРМА ФИНСОСТАВА: ЛОГИКА ДАННЫХ

from L20_PySide6             import RequestText, RequestConfirm
from L70_form_findescription import C70_FormFindescription
from L90_findescription      import C90_RecordFindescription


class C80_FormFindescription(C70_FormFindescription):
	""" Форма Финсостав: Логика данных """

	# Финсостав
	def LoadFindescription(self):
		""" Отображение финсостава """
		for self._ido_processing in self.findescription.SubIdos(""): self.LoadRecordFindescription()

		self.on_FindescriptionLoaded()

	# Запись финсостава
	def CreateRecord(self):
		""" Создание записи финсостава """
		record_findescription     = C90_RecordFindescription(self._ido_processing)
		parent_record             = C90_RecordFindescription(record_findescription.ParentIdo())
		parent_value : str        = parent_record.Name()

		group_text   : str        = f"{parent_value}" if parent_value else "Без группы"

		record_value : str | None = RequestText("Создание записи финсостава", f"Группа финсостава: {group_text}", "Значение")
		if     record_value is None                                        : return

		if not self.findescription.CreateRecord(parent_value, record_value): return

		self.on_RecordCreated()

	def CreateSubRecord(self):
		""" Создание записи финсостава """
		record_findescription     = C90_RecordFindescription(self._ido_processing)
		parent_value : str        = record_findescription.Name()

		group_text   : str        = f"{parent_value}" if parent_value else "Без группы"

		record_value : str | None = RequestText("Создание записи финсостава", f"Группа финсостава: {group_text}", "Значение")
		if     record_value is None                                        : return

		if not self.findescription.CreateRecord(parent_value, record_value): return

		self.on_SubRecordCreated()

	def EditNameRecord(self):
		""" Редактирование значения записи финсостава """
		if not self._ido_processing                                  : return

		record_findescription  = C90_RecordFindescription(self._ido_processing)
		value_old : str        = record_findescription.Name()

		value_new : str | None = RequestText("Редактирование записи финсостава", f"Редактирование записи финсостава", value_old)
		if     value_new is None                                     : return

		if not self.findescription.RenameRecord(value_old, value_new): return

		self.on_RecordRenamed()

	def DeleteRecord(self):
		""" Удаление записи финсостава """
		if not self._ido_processing  : return

		record_findescription        = C90_RecordFindescription(self._ido_processing)

		confirm_delete : bool | None = RequestConfirm("Удаление записи финсостава", f"Удалить {record_findescription.Name()} как структуру?", True)
		parent_ido     : str         = record_findescription.ParentIdo()

		if     confirm_delete is None: return

		self.findescription.DeleteRecord(record_findescription.Name(), confirm_delete)

		self._ido_processing = parent_ido

		self.on_RecordDeleted()

	def MoveUpRecord(self):
		""" Перемещение записи финсостава уровнем выше """
		if not self._ido_processing  : return

		record_findescription = C90_RecordFindescription(self._ido_processing)
		parent_ido : str      = record_findescription.ParentIdo()
		if not parent_ido            : return

		record_parent         = C90_RecordFindescription(parent_ido)
		record_findescription.ParentIdo(record_parent.ParentIdo())

		self.on_RecordMoved()

	def PasteRecord(self):
		""" Перемещение записи в тот же уровень """
		record_memory     = C90_RecordFindescription(self._ido_memory)
		record_processing = C90_RecordFindescription(self._ido_processing)

		record_memory.ParentIdo(record_processing.ParentIdo())

		self.on_RecordMoved()

	def SubPasteRecord(self):
		""" Перемещение записи в дочерний уровень """
		record_memory     = C90_RecordFindescription(self._ido_memory)

		record_memory.ParentIdo(self._ido_processing)

		self.on_RecordMoved()

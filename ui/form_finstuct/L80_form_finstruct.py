# ФОРМА ФИНСТРУКТУРЫ: ЛОГИКА ДАННЫХ

from L00_containers     import CONTAINER_LOCAL

from L20_PySide6        import RequestText, RequestConfirm, RequestValue
from L70_form_finstruct import C70_FormFinstruct
from L90_finstate       import C90_RecordFinstate
from L90_finstruct      import C90_RecordFinstruct


class C80_FormFinstruct(C70_FormFinstruct):
	""" Форма Финструктуры: Логика данных """

	# Финструктура
	def LoadFinstruct(self):
		""" Отображение финструктуры """
		dy : int = self.workspace.Dy()
		dm : int = self.workspace.Dm()

		for self._ido_processing in self.finstruct.SubIdos(dy, dm): self.LoadRecordFinstruct()

		self.on_FinstructLoaded()

	# Запись финструктуры
	def CreateRecord(self):
		""" Создание записи финструктуры """
		dy           : int        = self.workspace.Dy()
		dm           : int        = self.workspace.Dm()
		record_finstruct          = C90_RecordFinstruct(self._ido_processing)
		parent_record             = C90_RecordFinstruct(record_finstruct.ParentIdo())
		parent_value : str        = parent_record.Name()

		group_text   : str        = f"{parent_value}" if parent_value else "Без группы"

		record_value : str | None = RequestText("Создание записи финструктуры", f"Группа финструктуры: {group_text}", "Значение")
		if record_value is None: return

		if not self.finstruct.CreateRecordFinstruct(dy, dm, parent_value, record_value): return

		self.on_RecordCreated()

	def CreateSubRecord(self):
		""" Создание записи финструктуры """
		dy           : int        = self.workspace.Dy()
		dm           : int        = self.workspace.Dm()
		record_finstruct          = C90_RecordFinstruct(self._ido_processing)
		parent_value : str        = record_finstruct.Name()

		group_text   : str        = f"{parent_value}" if parent_value else "Без группы"

		record_value : str | None = RequestText("Создание записи финструктуры", f"Группа финструктуры: {group_text}", "Значение")
		if record_value is None: return

		if not self.finstruct.CreateRecordFinstruct(dy, dm, parent_value, record_value): return

		self.on_SubRecordCreated()

	def EditNameRecord(self):
		""" Редактирование наименования записи финструктуры """
		if not self._ido_processing                                     : return

		dy        : int        = self.workspace.Dy()
		dm        : int        = self.workspace.Dm()
		record_finstruct       = C90_RecordFinstruct(self._ido_processing)
		value_old : str        = record_finstruct.Name()

		value_new : str | None = RequestText("Редактирование записи финструктуры", f"Редактирование записи финструктуры", value_old)
		if value_new is None: return

		if not self.finstruct.RenameRecordFinstruct(dy, dm, value_old, value_new): return

		self.on_RecordRenamed()

	def DeleteRecord(self):
		""" Удаление записи финструктуры """
		if not self._ido_processing  : return

		dy             : int         = self.workspace.Dy()
		dm             : int         = self.workspace.Dm()
		record_finstruct             = C90_RecordFinstruct(self._ido_processing)

		confirm_delete : bool | None = RequestConfirm("Удаление записи финструктуры", f"Удалить {record_finstruct.Name()} как структуру?", True)
		parent_ido     : str         = record_finstruct.ParentIdo()

		if     confirm_delete is None: return

		record_finstate              = C90_RecordFinstate()
		if record_finstate.SwitchByFinstructIdo(self._ido_processing): record_finstate.DeleteObject(CONTAINER_LOCAL)

		self.finstruct.DeleteRecordFinstruct(dy, dm, record_finstruct.Name(), confirm_delete)

		self._ido_processing = parent_ido

		self.on_RecordDeleted()

	def MoveUpRecord(self):
		""" Перемещение записи уровнем выше """
		if not self._ido_processing  : return

		record_finstruct = C90_RecordFinstruct(self._ido_processing)
		parent_ido : str = record_finstruct.ParentIdo()
		if not parent_ido: return

		record_parent    = C90_RecordFinstruct(parent_ido)
		record_finstruct.ParentIdo(record_parent.ParentIdo())

		self.on_RecordMoved()

	def PasteRecord(self):
		""" Перемещение записи в тот же уровень """
		record_memory     = C90_RecordFinstruct(self._ido_memory)
		record_processing = C90_RecordFinstruct(self._ido_processing)

		record_memory.ParentIdo(record_processing.ParentIdo())

		self.on_RecordMoved()

	def SubPasteRecord(self):
		""" Перемещение записи в дочерний уровень """
		record_memory = C90_RecordFinstruct(self._ido_memory)

		record_memory.ParentIdo(self._ido_processing)

		self.on_RecordMoved()

	def CopyRecordToNextDm(self):
		""" Перенос записи финструктуры в следующий финпериод """
		if not self._ido_processing: return

		record_finstruct = C90_RecordFinstruct(self._ido_processing)
		record_finstruct.TransferToAnotherDm(1)

		record_finstate  = C90_RecordFinstate()
		record_finstate.SwitchByFinstructIdo(self._ido_processing)
		record_finstate.TransferToNextDm()

	def CopyRecordToPrevDm(self):
		""" Перенос записи финструктуры в предыдущий финпериод """
		if not self._ido_processing: return

		record_finstruct = C90_RecordFinstruct(self._ido_processing)
		record_finstruct.TransferToAnotherDm(-1)

	def SetPriorityRecord(self):
		""" Установка записи приоритетной """
		if not self._ido_processing: return

		self.finstruct.SetPriorityRecord(self._ido_processing)

		self.LoadFinstruct()

	# Финсостояние
	def RequestEditRemainInitial(self):
		""" Запрос на редактирование остатка начального """
		if not self._ido_processing: return

		record_finstruct    = C90_RecordFinstruct(self._ido_processing)
		record_finstate     = C90_RecordFinstate()

		if not record_finstate.SwitchByFinstructIdo(self._ido_processing):
			record_finstate.GenerateIdo()
			record_finstate.RegisterObject(CONTAINER_LOCAL)
			record_finstate.FinstructIdo(self._ido_processing)
			record_finstate.RemainsInitial(0)

		remain : int | None = record_finstate.RemainsInitial()
		remain              = RequestValue(record_finstruct.Name(), "Остаток начальный", remain, -99999999, 99999999)
		if remain is None: return

		record_finstate.RemainsInitial(remain)

		self.on_RecordChanged()

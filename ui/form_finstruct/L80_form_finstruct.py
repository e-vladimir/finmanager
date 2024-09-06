# ФОРМА ФИНСТРУКТУРА: ЛОГИКА ДАННЫХ

from L00_containers     import CONTAINER_LOCAL
from L20_PySide6        import RequestText, RequestConfirm, RequestValue
from L70_form_finstruct import C70_FormFinstruct
from L90_finstruct      import C90_FinstructRecord


class C80_FormFinstruct(C70_FormFinstruct):
	""" Форма Финструктура: Логика данных """

	# Финструктура
	def LoadFinstruct(self):
		""" Загрузка финструктуры """
		dy, dm = self.workspace.DyDm()

		for self._processing_name in self.finstruct.Groups(dy, dm): self.LoadFinstructGroup()
		for self._processing_ido  in self.finstruct.Idos(dy, dm)  : self.LoadFinstructRecord()

	# Запись финструктуры
	def CreateFinstructRecord(self):
		""" Создание записи финструктуры """
		dy, dm                    = self.workspace.DyDm()
		group_name   : str | None = RequestText("Управление финструктурой", f"Наименование группы счетов", items=self.finstruct.Groups(dy, dm))
		if group_name is None: return

		record_name : str | None = RequestText("Управление финструктурой", f"Наименование счёта в группе {group_name}")
		if record_name is None: return

		self.finstruct.Create(dy, dm, record_name, group_name)

	def CreateFinstructRecordInGroup(self):
		""" Создание записи финструктуры в текущей группе """
		if not self._group_processing: return

		dy, dm = self.workspace.DyDm()
		record_name : str | None = RequestText("Управление финструктурой", f"Наименование счёта в группе {self._group_processing}")
		if record_name is None: return

		self.finstruct.Create(dy, dm, record_name, self._group_processing)

	def RenameFinstructRecord(self):
		""" Изменение наименования записи финструктуры """
		if not self._processing_ido: return

		record_name : str | None = RequestText("Управление финструктурой", f"Наименование счёта в группе {self._group_processing}", self._processing_name)
		if record_name is None: return

		dy, dm = self.workspace.DyDm()
		self.finstruct.Rename(dy, dm, self._processing_name, record_name)

	def DeleteFinstructRecord(self):
		""" Удаление записи финструктуры """
		if not self._processing_ido: return

		if not RequestConfirm("Управление финструктурой", f"Удаление счёта {self._processing_name}"): return

		record = C90_FinstructRecord(self._processing_ido)
		record.DeleteObject(CONTAINER_LOCAL)

	def RegroupFinstructRecord(self):
		""" Изменение группы счета """
		if not self._processing_ido: return

		dy, dm = self.workspace.DyDm()
		group_name : str | None = RequestText("Управление финструктурой", f"Наименование группы счетов", old_text=self._group_processing, items=self.finstruct.Groups(dy, dm))
		if group_name is None: return

		if group_name in self.finstruct.Groups(dy, dm): return

		record = C90_FinstructRecord(self._processing_ido)
		record.Group(group_name)

	def RenameGroupFinstruct(self):
		""" Изменение наименования группы счетов """
		group_name : str | None = RequestText("Управление финструктурой", f"Наименование группы счетов", self._group_processing)
		if group_name is None: return

		dy, dm = self.workspace.DyDm()
		self.finstruct.Regroup(dy, dm, self._group_processing, group_name)

	# Финсостояние
	def EditBalanceStartFinstructRecord(self):
		""" Редактирование баланса начального """
		if not self._processing_ido: return

		record              = C90_FinstructRecord(self._processing_ido)
		amount : int | None = RequestValue("Финсостояние", f"{record.Name()}\nБаланс счёта на начало {self.workspace.DmDyToString()}", int(record.BalanceStart()), -99999999, 99999999)

		record.BalanceStart(amount)

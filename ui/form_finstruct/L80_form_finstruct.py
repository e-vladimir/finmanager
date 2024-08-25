# ФОРМА ФИНСТРУКТУРА: ЛОГИКА ДАННЫХ

from L20_PySide6        import RequestText
from L70_form_finstruct import C70_FormFinstruct


class C80_FormFinstruct(C70_FormFinstruct):
	""" Форма Финструктура: Логика данных """

	# Финструктура
	def LoadFinstruct(self):
		""" Загрузка финструктуры """
		dy, dm = self.workspace.DyDm()

		for self._name_processing in self.finstruct.Groups(dy, dm): self.LoadFinstructGroup()
		for self._ido_processing  in self.finstruct.Idos(dy, dm)  : self.LoadFinstructRecord()

	# Запись финструктуры
	def CreateFinstructRecord(self):
		""" Создание записи финструктуры """
		dy, dm = self.workspace.DyDm()
		group_name : str | None = RequestText("Управление финструктурой", f"Наименование группы счетов", items=self.finstruct.Groups(dy, dm))
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

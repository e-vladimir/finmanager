# ФИНСОСТАВ: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL
from L70_fincomposition     import C70_Fincomposition, C70_FincompositionRecord


class C80_FincompositionRecord(C70_FincompositionRecord):
	""" Запись финсостава: Логика данных """

	# Выборки данных
	def SubNames(self) -> list[str]:
		""" Наименования вложенных записей """
		filter_data = C30_FilterLinear1D(self.Idc().data)
		filter_data.FilterIdpVlpByEqual(self.f_parent_ido.Idp().data, self.Ido().data)
		filter_data.Capture(CONTAINER_LOCAL)

		return filter_data.ToStrings(self.f_name.Idp().data, flag_sort=True).data

	def SubIdos(self, flag_include_struct: bool = False) -> list[str]:
		""" IDO вложенных записей """
		filter_data = C30_FilterLinear1D(self.Idc().data)
		filter_data.FilterIdpVlpByEqual(self.f_parent_ido.Idp().data, self.Ido().data)
		filter_data.Capture(CONTAINER_LOCAL)

		idos : list[str] = filter_data.Idos(self.f_name.Idp().data).data

		if not flag_include_struct: return idos

		for ido in idos.copy():
			subrecord = C80_FincompositionRecord(ido)

			idos.extend(subrecord.SubIdos(flag_include_struct))

		return idos

	def MoveUp(self):
		""" Перемещение вверх """
		if not self.ParentIdo(): return

		parent = C80_FincompositionRecord(self.ParentIdo())
		self.ParentIdo(parent.ParentIdo())


class C80_Fincomposition(C70_Fincomposition):
	""" Финсостав: Логика данных """

	# Выборки данных
	def NameToIdo(self, record_name: str) -> str:
		""" Преобразование наименования в IDO """
		record = C80_FincompositionRecord()
		record.SwitchByName(record_name)

		return record.Ido().data

	def Names(self) -> list[str]:
		""" Список наименований """
		record = C80_FincompositionRecord()

		filter_data = C30_FilterLinear1D(record.Idc().data)
		filter_data.Capture(CONTAINER_LOCAL)

		return filter_data.ToStrings(record.f_name.Idp().data, flag_sort=True).data

	def TopNames(self) -> list[str]:
		""" Список наименований верхнего уровня """
		record = C80_FincompositionRecord()

		filter_data = C30_FilterLinear1D(record.Idc().data)
		filter_data.FilterIdpVlpByEqual(record.f_parent_ido.Idp().data, "")
		filter_data.Capture(CONTAINER_LOCAL)

		return filter_data.ToStrings(record.f_name.Idp().data, flag_sort=True).data

	def TopIdos(self) -> list[str]:
		""" Список IDO верхнего уровня """
		record = C80_FincompositionRecord()

		filter_data = C30_FilterLinear1D(record.Idc().data)
		filter_data.FilterIdpVlpByEqual(record.f_parent_ido.Idp().data, "")
		filter_data.Capture(CONTAINER_LOCAL)

		return filter_data.Idos(record.f_name.Idp().data).data

	# Управление записями
	def Append(self, record_name: str, parent_name: str = "") -> bool:
		""" Добавление записи """
		if record_name in self.Names(): return False

		parent_ido : str = self.NameToIdo(parent_name)

		record = C80_FincompositionRecord()
		record.GenerateIdo()
		record.RegisterObject(CONTAINER_LOCAL)

		record.Name(record_name)
		record.ParentIdo(parent_ido)

		return True

	def Rename(self, name_old: str, name_new: str) -> bool:
		""" Изменение наименования записи """
		if name_new in self.Names(): return False

		record = C80_FincompositionRecord()
		record.SwitchByName(name_old)
		record.Name(name_new)

		return True

	def Delete(self, record_name: str, flag_delete_struct: bool = False) -> bool:
		""" Удаление записи финсостава """
		record                 = C80_FincompositionRecord()
		if not record.SwitchByName(record_name): return False

		parent_ido : str       = record.ParentIdo()
		oids       : list[str] = record.SubIdos(flag_delete_struct)

		record.DeleteObject(CONTAINER_LOCAL)

		for oid in oids:
			record = C80_FincompositionRecord(oid)

			if flag_delete_struct: record.DeleteObject(CONTAINER_LOCAL)
			else                 : record.ParentIdo(parent_ido)

		return True

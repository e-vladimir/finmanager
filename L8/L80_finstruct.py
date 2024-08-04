# ФИНСТРУКТУРА: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL

from L11_datetime           import CalcDyDmByShiftDm
from L70_finstruct          import C70_RecordFinstruct, C70_Finstruct


class C80_RecordFinstruct(C70_RecordFinstruct):
	""" Запись финструктуры: Логика данных """

	# Переключение
	def SwitchByName(self, dy: int, dm: int, name: str) -> bool:
		""" Смена OID по значению """
		filter_finstruct = C30_FilterLinear1D(self.Idc().data)
		filter_finstruct.FilterIdpVlpByEqual(self.f_name.Idp().data, name)
		filter_finstruct.FilterIdpVlpByEqual(self.f_dy.Idp().data, dy)
		filter_finstruct.FilterIdpVlpByEqual(self.f_dm.Idp().data, dm)
		filter_finstruct.Capture(CONTAINER_LOCAL)

		idos : list[str] = filter_finstruct.Idos().data
		if not idos: return False

		self.Ido(idos[0])
		return True

	# Выборки данных
	def SubIdos(self, flag_all_subidos: bool = False) -> list[str]:
		""" Список OID """
		filter_finstruct   = C30_FilterLinear1D(self.Idc().data)
		filter_finstruct.FilterIdpVlpByEqual(self.f_parent_ido.Idp().data, self.Ido().data)
		filter_finstruct.FilterIdpVlpByEqual(self.f_dy.Idp().data, self.Dy())
		filter_finstruct.FilterIdpVlpByEqual(self.f_dm.Idp().data, self.Dm())
		filter_finstruct.Capture(CONTAINER_LOCAL)

		result : list[str] = filter_finstruct.Idos(self.f_name.Idp().data).data

		if not flag_all_subidos: return result

		for subido in result:
			subrecord = C80_RecordFinstruct(subido)

			result.extend(subrecord.SubIdos(flag_all_subidos))

		return result

	# Перемещение данных
	def TransferToAnotherDm(self, shift_dm: int):
		""" Перенос в другой финпериод """
		dy_next, dm_next = CalcDyDmByShiftDm(self.Dy(), self.Dm(), shift_dm)
		parent_current   = C80_RecordFinstruct(self.ParentIdo())

		parent_next      = C80_RecordFinstruct()
		parent_next.SwitchByName(dy_next, dm_next, parent_current.Name())

		record_next      = C80_RecordFinstruct()
		if not record_next.SwitchByName(dy_next, dm_next, self.Name()):
			record_next.GenerateIdo()
			record_next.RegisterObject(CONTAINER_LOCAL)
			record_next.Name(self.Name())
			record_next.Dy(dy_next)
			record_next.Dm(dm_next)

		record_next.ParentIdo(parent_next.Ido().data)

		for sub_ido in self.SubIdos(): C80_RecordFinstruct(sub_ido).TransferToAnotherDm(shift_dm)


class C80_Finstruct(C70_Finstruct):
	""" Финструктура: Логика данных """

	# Выборки данных
	def IdosInDyDm(self, dy: int, dm: int) -> list[str]:
		""" Список OID всех записей финструктуры """
		filter_finstruct = C30_FilterLinear1D(self._idc)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_dy, dy)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_dm, dm)
		filter_finstruct.Capture(CONTAINER_LOCAL)

		return filter_finstruct.Idos(self._idp_name).data

	def NamesInDyDm(self, dy: int, dm: int) -> list[str]:
		""" Список наименований всех записей финструктуры """
		filter_finstruct = C30_FilterLinear1D(self._idc)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_dy, dy)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_dm, dm)
		filter_finstruct.Capture(CONTAINER_LOCAL)

		return filter_finstruct.ToStrings(self._idp_name, False, True).data

	def SubNamesInDyDm(self, dy: int, dm: int, parent_name: str = "") -> list[str]:
		""" Получить список наименований подчинённых записей финструктуры """
		record_finstruct = C80_RecordFinstruct()
		record_finstruct.SwitchByName(dy, dm, parent_name)

		filter_finstruct = C30_FilterLinear1D(self._idc)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_dy, dy)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_dm, dm)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_parent_ido, record_finstruct.Ido().data)

		filter_finstruct.Capture(CONTAINER_LOCAL)

		return filter_finstruct.ToStrings(self._idp_name, False, True).data

	def SubIdos(self, dy: int, dm: int, ido: str = "") -> list[str]:
		""" Получить список OID подчинённых записей финструктуры """
		filter_finstruct = C30_FilterLinear1D(self._idc)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_dy, dy)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_dm, dm)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_parent_ido, ido)

		filter_finstruct.Capture(CONTAINER_LOCAL)

		return filter_finstruct.Idos(self._idp_name).data

	def IdosToNames(self, idos: list[str]) -> list[str]:
		""" Имена финструктуры по списку OID """
		result : list[str] = []

		for ido in idos:
			record_finstruct = C80_RecordFinstruct(ido)
			result.append(record_finstruct.Name())

		return sorted(result)

	def StructuredNamesInDyDm(self, dy: int, dm: int, parent_name: str = "", padding: str = "") -> list[str]:
		""" Список OID с учётом структуры """
		result : list[str] = []

		for name in self.SubNamesInDyDm(dy, dm, parent_name):
			result.append(f"{padding}{name}")
			result.extend(self.StructuredNamesInDyDm(dy, dm, name, padding + '  '))

		return result

	# Управление значениями
	def CreateRecordFinstruct(self, dy: int, dm: int, parent_name, name: str) -> bool:
		""" Создание записи финструктуры """
		if not self.ValidateName(name)   : return False
		if     name in self.NamesInDyDm(dy, dm): return False

		record_parent    = C80_RecordFinstruct()
		record_parent.SwitchByName(dy, dm, parent_name)

		record_finstruct = C80_RecordFinstruct()
		record_finstruct.GenerateIdo()
		record_finstruct.RegisterObject(CONTAINER_LOCAL)

		record_finstruct.Name(name)
		record_finstruct.ParentIdo(record_parent.Ido().data)
		record_finstruct.Dy(dy)
		record_finstruct.Dm(dm)

		return True

	def RenameRecordFinstruct(self, dy: int, dm: int, name_old: str, name_new: str) -> bool:
		""" Переименование записи финструктуры """
		if not self.ValidateName(name_new)                    : return False
		if     name_new in self.NamesInDyDm(dy, dm)                 : return False

		record_finstruct = C80_RecordFinstruct()
		if not record_finstruct.SwitchByName(dy, dm, name_old): return False

		record_finstruct.Name(name_new)

		return True

	def DeleteRecordFinstruct(self, dy: int, dm: int, name: str, delete_subrecords: bool = False) -> bool:
		""" Удаление значения финсостава """
		record_finstruct = C80_RecordFinstruct()

		if not record_finstruct.SwitchByName(dy, dm, name): return False

		parent_ido : str = record_finstruct.ParentIdo()

		if delete_subrecords:
			for subido in record_finstruct.SubIdos(True) : C80_RecordFinstruct(subido).DeleteObject(CONTAINER_LOCAL)
		else:
			for subido in record_finstruct.SubIdos(False):	C80_RecordFinstruct(subido).ParentIdo(parent_ido)

		record_finstruct.DeleteObject(CONTAINER_LOCAL)

		return True

	# Управление приоритетом записей
	def SetPriorityRecord(self, ido: str):
		""" Установка приоритетной записи """
		if not ido                                                      : return
		if     ido not in C80_RecordFinstruct.Idos(CONTAINER_LOCAL).data: return

		record_finstruct = C80_RecordFinstruct(ido)
		dy   : int       = record_finstruct.Dy()
		dm   : int       = record_finstruct.Dm()

		filter_finstruct = C30_FilterLinear1D(self._idc)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_dy, dy)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_dm, dm)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_priority, True)
		filter_finstruct.Capture(CONTAINER_LOCAL)

		priority_idos : list[str] = filter_finstruct.Idos().data
		for priority_ido in priority_idos:
			record_finstruct = C80_RecordFinstruct(priority_ido)
			record_finstruct.Priority(False)

		record_finstruct = C80_RecordFinstruct(ido)
		record_finstruct.Priority(True)

	def GetPriorityRecord(self, dy: int, dm: int) -> str:
		""" Получение OID приоритетной записи """
		filter_finstruct = C30_FilterLinear1D(self._idc)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_dy, dy)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_dm, dm)
		filter_finstruct.FilterIdpVlpByEqual(self._idp_priority, True)
		filter_finstruct.Capture(CONTAINER_LOCAL)

		priority_idos : list[str] = filter_finstruct.Idos().data
		if not priority_idos: return ""

		return priority_idos[0]

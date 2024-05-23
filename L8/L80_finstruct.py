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
		filter_finstruct = C30_FilterLinear1D(self.Oci().text)
		filter_finstruct.FilterPidCvlByEqual(self.f_name.Pid().text, name)
		filter_finstruct.FilterPidCvlByEqual(self.f_dy.Pid().text, dy)
		filter_finstruct.FilterPidCvlByEqual(self.f_dm.Pid().text, dm)
		filter_finstruct.Capture(CONTAINER_LOCAL)

		oids : list[str] = filter_finstruct.Oids().items
		if not oids: return False

		self.Oid(oids[0])
		return True

	# Выборки данных
	def SubOids(self, flag_all_suboids: bool = False) -> list[str]:
		""" Список OID """
		filter_finstruct   = C30_FilterLinear1D(self.Oci().text)
		filter_finstruct.FilterPidCvlByEqual(self.f_parent_oid.Pid().text, self.Oid().text)
		filter_finstruct.FilterPidCvlByEqual(self.f_dy.Pid().text, self.Dy())
		filter_finstruct.FilterPidCvlByEqual(self.f_dm.Pid().text, self.Dm())
		filter_finstruct.Capture(CONTAINER_LOCAL)

		result : list[str] = filter_finstruct.Oids(self.f_name.Pid().text).items

		if not flag_all_suboids: return result

		for suboid in result:
			subrecord = C80_RecordFinstruct(suboid)

			result.extend(subrecord.SubOids(flag_all_suboids))

		return result

	# Перемещение данных
	def TransferToAnotherDm(self, shift_dm: int):
		""" Перенос в другой финпериод """
		dy_next, dm_next = CalcDyDmByShiftDm(self.Dy(), self.Dm(), shift_dm)
		parent_current   = C80_RecordFinstruct(self.ParentOid())

		parent_next      = C80_RecordFinstruct()
		parent_next.SwitchByName(dy_next, dm_next, parent_current.Name())

		record_next      = C80_RecordFinstruct()
		if not record_next.SwitchByName(dy_next, dm_next, self.Name()):
			record_next.GenerateOid()
			record_next.RegisterObject(CONTAINER_LOCAL)
			record_next.Name(self.Name())
			record_next.Dy(dy_next)
			record_next.Dm(dm_next)

		record_next.ParentOid(parent_next.Oid().text)

		for sub_oid in self.SubOids(): C80_RecordFinstruct(sub_oid).TransferToAnotherDm(shift_dm)


class C80_Finstruct(C70_Finstruct):
	""" Финструктура: Логика данных """

	# Выборки данных
	def OidsInDyDm(self, dy: int, dm: int) -> list[str]:
		""" Список OID всех записей финструктуры """
		filter_finstruct = C30_FilterLinear1D(self._oci)
		filter_finstruct.FilterPidCvlByEqual(self._pid_dy, dy)
		filter_finstruct.FilterPidCvlByEqual(self._pid_dm, dm)
		filter_finstruct.Capture(CONTAINER_LOCAL)

		return filter_finstruct.Oids(self._pid_name).items

	def NamesInDyDm(self, dy: int, dm: int) -> list[str]:
		""" Список наименований всех записей финструктуры """
		filter_finstruct = C30_FilterLinear1D(self._oci)
		filter_finstruct.FilterPidCvlByEqual(self._pid_dy, dy)
		filter_finstruct.FilterPidCvlByEqual(self._pid_dm, dm)
		filter_finstruct.Capture(CONTAINER_LOCAL)

		return filter_finstruct.ToStrings(self._pid_name, False, True).items

	def SubNamesInDyDm(self, dy: int, dm: int, parent_name: str = "") -> list[str]:
		""" Получить список наименований подчинённых записей финструктуры """
		record_finstruct = C80_RecordFinstruct()
		record_finstruct.SwitchByName(dy, dm, parent_name)

		filter_finstruct = C30_FilterLinear1D(self._oci)
		filter_finstruct.FilterPidCvlByEqual(self._pid_dy, dy)
		filter_finstruct.FilterPidCvlByEqual(self._pid_dm, dm)
		filter_finstruct.FilterPidCvlByEqual(self._pid_parent_oid, record_finstruct.Oid().text)

		filter_finstruct.Capture(CONTAINER_LOCAL)

		return filter_finstruct.ToStrings(self._pid_name, False, True).items

	def SubOids(self, dy: int, dm: int, oid: str = "") -> list[str]:
		""" Получить список OID подчинённых записей финструктуры """
		filter_finstruct = C30_FilterLinear1D(self._oci)
		filter_finstruct.FilterPidCvlByEqual(self._pid_dy, dy)
		filter_finstruct.FilterPidCvlByEqual(self._pid_dm, dm)
		filter_finstruct.FilterPidCvlByEqual(self._pid_parent_oid, oid)

		filter_finstruct.Capture(CONTAINER_LOCAL)

		return filter_finstruct.Oids(self._pid_name).items

	def OidsToNames(self, oids: list[str]) -> list[str]:
		""" Имена финструктуры по списку OID """
		result : list[str] = []

		for oid in oids:
			record_finstruct = C80_RecordFinstruct(oid)
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
		record_finstruct.GenerateOid()
		record_finstruct.RegisterObject(CONTAINER_LOCAL)

		record_finstruct.Name(name)
		record_finstruct.ParentOid(record_parent.Oid().text)
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

		parent_oid : str = record_finstruct.ParentOid()

		if delete_subrecords:
			for suboid in record_finstruct.SubOids(True) : C80_RecordFinstruct(suboid).DeleteObject(CONTAINER_LOCAL)
		else:
			for suboid in record_finstruct.SubOids(False):	C80_RecordFinstruct(suboid).ParentOid(parent_oid)

		record_finstruct.DeleteObject(CONTAINER_LOCAL)

		return True

	# Управление приоритетом записей
	def SetPriorityRecord(self, oid: str):
		""" Установка приоритетной записи """
		if not oid                                                       : return
		if     oid not in C80_RecordFinstruct.Oids(CONTAINER_LOCAL).items: return

		record_finstruct = C80_RecordFinstruct(oid)
		dy   : int       = record_finstruct.Dy()
		dm   : int       = record_finstruct.Dm()

		filter_finstruct = C30_FilterLinear1D(self._oci)
		filter_finstruct.FilterPidCvlByEqual(self._pid_dy, dy)
		filter_finstruct.FilterPidCvlByEqual(self._pid_dm, dm)
		filter_finstruct.FilterPidCvlByEqual(self._pid_priority, True)
		filter_finstruct.Capture(CONTAINER_LOCAL)

		priority_oids : list[str] = filter_finstruct.Oids().items
		for priority_oid in priority_oids:
			record_finstruct = C80_RecordFinstruct(priority_oid)
			record_finstruct.Priority(False)

		record_finstruct = C80_RecordFinstruct(oid)
		record_finstruct.Priority(True)

	def GetPriorityRecord(self, dy: int, dm: int) -> str:
		""" Получение OID приоритетной записи """
		filter_finstruct = C30_FilterLinear1D(self._oci)
		filter_finstruct.FilterPidCvlByEqual(self._pid_dy, dy)
		filter_finstruct.FilterPidCvlByEqual(self._pid_dm, dm)
		filter_finstruct.FilterPidCvlByEqual(self._pid_priority, True)
		filter_finstruct.Capture(CONTAINER_LOCAL)

		priority_oids : list[str] = filter_finstruct.Oids().items
		if not priority_oids: return ""

		return priority_oids[0]

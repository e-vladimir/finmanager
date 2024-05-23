# ФИНСОСТАВ: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL
from L70_findescription     import C70_RecordFindescription, C70_Findescription


class C80_RecordFindescription(C70_RecordFindescription):
	""" Запись финсостава: Логика данных """

	# Переключение
	def SwitchByName(self, name: str) -> bool:
		""" Смена OID по значению """
		filter_findescription = C30_FilterLinear1D(self.Oci().text)
		filter_findescription.FilterPidCvlByEqual(self.f_name.Pid().text, name)
		filter_findescription.Capture(CONTAINER_LOCAL)

		oids : list[str]      = filter_findescription.Oids().items
		if not oids: return False

		self.Oid(oids[0])
		return True

	# Выборки данных
	def SubOids(self, flag_all_suboids: bool = False) -> list[str]:
		""" Список OID """
		filter_findescription = C30_FilterLinear1D(self.Oci().text)
		filter_findescription.FilterPidCvlByEqual(self.f_parent_oid.Pid().text, self.Oid().text)
		filter_findescription.Capture(CONTAINER_LOCAL)

		result : list[str]    = filter_findescription.Oids(self.f_name.Pid().text).items

		if not flag_all_suboids: return result

		for suboid in result:
			subrecord = C80_RecordFindescription(suboid)

			result.extend(subrecord.SubOids(flag_all_suboids))

		return result

	# Категории финсостава
	def IncludeInCategory(self, category_name: str):
		""" Включение в категорию финсостава """
		categories : list[str] | set[str] = set(self.Categories())
		if category_name in categories: return

		categories.add(category_name)
		categories             = list(categories)

		self.Categories(categories)

	def ExcludeFromCategory(self, category_name: str):
		""" Исключение из группы финсостава """
		categories : list[str] | set[str] = set(self.Categories())
		if category_name not in categories: return

		categories.remove(category_name)
		categories             = list(categories)

		self.Categories(categories)


class C80_Findescription(C70_Findescription):
	""" Финсостав: Логика данных """

	# Выборки данных
	def Names(self, category: str = None) -> list[str]:
		""" Список наименований записей финсостава с фильтрацией по категории """
		filter_findescription = C30_FilterLinear1D(self._oci)

		if category: filter_findescription.FilterPidCvlByInclude(self._pid_categories, category)

		filter_findescription.Capture(CONTAINER_LOCAL)

		return filter_findescription.ToStrings(self._pid_name, False, True).items

	def SubNames(self, parent_name: str = "") -> list[str]:
		""" Получить список наименований подчинённых записей финсостава """
		record_findescription = C80_RecordFindescription()
		record_findescription.SwitchByName(parent_name)

		filter_findescription = C30_FilterLinear1D(self._oci)
		filter_findescription.FilterPidCvlByEqual(self._pid_parent_oid, record_findescription.Oid().text)

		filter_findescription.Capture(CONTAINER_LOCAL)

		return filter_findescription.ToStrings(self._pid_name, False, True).items

	def Oids(self) -> list[str]:
		""" Получить список OID значений финсостава """
		filter_findescription = C30_FilterLinear1D(self._oci)
		filter_findescription.Capture(CONTAINER_LOCAL)

		return filter_findescription.Oids(self._pid_name).items

	def SubOids(self, oid: str = "") -> list[str]:
		""" Получить список OID подчинённых значений финсостава """
		filter_findescription = C30_FilterLinear1D(self._oci)
		filter_findescription.FilterPidCvlByEqual(self._pid_parent_oid, oid)

		filter_findescription.Capture(CONTAINER_LOCAL)

		return filter_findescription.Oids(self._pid_name).items

	def OidsToNames(self, oids: list[str], category: str = None) -> list[str]:
		""" Имена финструктуры по списку OID """
		result : list[str] = []

		if category is None:
			for oid in oids:
				record_finstruct = C80_RecordFindescription(oid)
				result.append(record_finstruct.Name())

		else:
			oids_category : list[str] = self.OidsByCategory(category)

			for oid in list(set(oids_category).intersection(set(oids))):
				record_finstruct = C80_RecordFindescription(oid)
				result.append(record_finstruct.Name())

		return sorted(result)

	def OidsByCategory(self, category: str) -> list[str]:
		""" Получить список OID значений финсостава в указанной категории """
		filter_findescription = C30_FilterLinear1D(self._oci)
		filter_findescription.FilterPidCvlByInclude(self._pid_categories, category)

		filter_findescription.Capture(CONTAINER_LOCAL)

		return filter_findescription.Oids(self._pid_name).items

	def NamesToOids(self, names: list[str]) -> list[str]:
		""" Преобразование имён в OID """
		result : list[str] = []

		for name in names:
			record_findescription = C80_RecordFindescription()
			if not record_findescription.SwitchByName(name): continue

			result.append(record_findescription.Oid().text)

		return result

	# Управление значениями
	def CreateRecord(self, parent_name: str, name: str) -> bool:
		""" Создание значения записи финсостава """
		if not self.ValidateName(name): return False
		if     name in self.Names()   : return False

		record_parent    = C80_RecordFindescription()
		record_parent.SwitchByName(parent_name)

		parent_oid : str = record_parent.Oid().text

		record           = C80_RecordFindescription()
		record.GenerateOid()
		record.RegisterObject(CONTAINER_LOCAL)
		record.ParentOid(parent_oid)
		record.Name(name)
		record.Categories([])

		return True

	def RenameRecord(self, name_old: str, name_new: str) -> bool:
		""" Редактирование значения записи финсостава """
		if not self.ValidateName(name_new)                 : return False
		if     name_new in self.Names()                    : return False

		record_findescription = C80_RecordFindescription()
		if not record_findescription.SwitchByName(name_old): return False

		record_findescription.Name(name_new)

		return True

	def DeleteRecord(self, name: str, delete_subrecords: bool = False) -> bool:
		""" Удаление значения финсостава """
		record_findescription = C80_RecordFindescription()

		if not record_findescription.SwitchByName(name): return False

		parent_oid : str = record_findescription.ParentOid()

		if delete_subrecords:
			for suboid in record_findescription.SubOids(True) : C80_RecordFindescription(suboid).DeleteObject(CONTAINER_LOCAL)
		else:
			for suboid in record_findescription.SubOids(False):	C80_RecordFindescription(suboid).ParentOid(parent_oid)

		record_findescription.DeleteObject(CONTAINER_LOCAL)

		return True

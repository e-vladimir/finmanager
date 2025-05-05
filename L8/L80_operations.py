# ФИНАНСОВЫЕ ОПЕРАЦИИ: ЛОГИКА ДАННЫХ
# 11 мар 2025

from G11_convertor_data     import AmountToString
from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L00_months             import MONTHS_SHORT
from L00_operations         import OPERATIONS
from L20_finmanager_struct  import T20_RawOperation
from L70_operations         import C70_Operation, C70_Operations


class C80_Operation(C70_Operation):
	""" Финансовая операция: Логика данных """

	# Выборка данных
	def Descriptions(self) -> str:
		""" Пользовательское или исходное описание """
		return self.description or self.src_description


	# Управление операцией
	def Split(self, amount: int) -> str:
		""" Разделение операции """
		accounts        = self.account_idos
		color           = self.color
		dd              = self.dd
		description     = self.description
		destination     = self.destination
		dm              = self.dm
		dy              = self.dy
		parent_ido      = self.parent_ido
		skip            = self.skip
		src_description = self.src_description

		if not parent_ido:
			parent_ido = self.Ido().data
			self.skip  = True
			skip       = False

		else                  :
			self.amount -= amount

		operation       = C80_Operation()

		operation.GenerateIdo()
		operation.RegisterObject(CONTAINERS.DISK)
		operation.RegisterObject(CONTAINERS.CACHE)

		operation.account_idos    = accounts
		operation.amount          = amount
		operation.color           = color
		operation.dd              = dd
		operation.description     = description
		operation.destination     = destination
		operation.dm              = dm
		operation.dy              = dy
		operation.parent_ido      = parent_ido
		operation.skip            = skip
		operation.src_description = src_description

		return operation.Ido().data

	def Copy(self) -> str:
		""" Копирование операции """
		accounts        = self.account_idos
		amount          = self.amount
		color           = self.color
		dd              = self.dd
		description     = self.description
		destination     = self.destination
		dm              = self.dm
		dy              = self.dy
		parent_ido      = self.parent_ido
		skip            = self.skip
		src_description = self.src_description

		self.GenerateIdo()
		self.RegisterObject(CONTAINERS.DISK)
		self.RegisterObject(CONTAINERS.CACHE)

		self.account_idos    = accounts
		self.amount          = amount
		self.color           = color
		self.dd              = dd
		self.description     = description
		self.destination     = destination
		self.dm              = dm
		self.dy              = dy
		self.parent_ido      = parent_ido
		self.skip            = skip
		self.src_description = src_description

		return self.Ido().data


	# Кеширование
	def Caching(self):
		""" Кеширование операции """
		self.CopyToContainer(CONTAINERS.DISK, CONTAINERS.CACHE)


	# Конвертация
	def DdDmDyToString(self) -> str:
		""" Дата в строку """
		return f"{self.dd:02d} {MONTHS_SHORT[self.dm]} {self.dy:04d}"

	def ShortInformation(self) -> str:
		""" Краткая информация об операции """
		return f"{AmountToString(self.amount, flag_sign=True)} от {self.dd:02d} {self.DdDmDyToString()}"

	def Information(self, flag_flat: bool = False) -> str:
		""" Информация об операции """
		if flag_flat: return f"{AmountToString(self.amount, flag_sign=True)} от {self.DdDmDyToString()} ({self.Descriptions()})"
		else        : return f"{AmountToString(self.amount, flag_sign=True)} от {self.DdDmDyToString()}\n{self.Descriptions()}"

	def ToT20_RawOperation(self) -> T20_RawOperation:
		return T20_RawOperation(amount          = int(self.amount),
		                        src_description = self.src_description,
		                        description     = self.description,
		                        destination     = self.destination)


class C80_Operations(C70_Operations):
	""" Финансовые операции: Логика данных """

	# Выборки данных
	@classmethod
	def Idos(cls, dy: int, dm: int, dd: int = None, account_ido: str = None, use_cache: bool = False, type_operation: OPERATIONS=OPERATIONS.ALL) -> list[str]:
		""" Список IDO финансовых операций """
		operation         = C80_Operation()
		idc         : str = operation.Idc().data
		idp_account : str = operation.FAccountIdos.Idp().data
		idp_amount  : str = operation.FAmount.Idp().data
		idp_dd      : str = operation.FDd.Idp().data
		idp_dm      : str = operation.FDm.Idp().data
		idp_dy      : str = operation.FDy.Idp().data
		idp_parent  : str = operation.FParentIdo.Idp().data
		idp_skip    : str = operation.FSkip.Idp().data
		idp_virtual : str = operation.FVirtualIdos.Idp().data

		filter_data       = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dd, dd)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByInclude(idp_account, account_ido)

		match type_operation:
			case OPERATIONS.ALL     :
				pass

			case OPERATIONS.PHYSICAL:
				filter_data.FilterIdpVlpByEqual(idp_parent, "")

			case OPERATIONS.VIRTUAL:
				filter_data.FilterIdpVlpByEqual(idp_parent, "", flag_invert=True)

			case OPERATIONS.BASIC:
				filter_data.FilterIdpVlpByEqual(idp_parent, "")
				filter_data.FilterIdpVlpByEqual(idp_virtual,  "")

			case OPERATIONS.PARENT:
				filter_data.FilterIdpVlpByEqual(idp_virtual,  "", flag_invert=True)

			case OPERATIONS.ACCOUNTING:
				filter_data.FilterIdpVlpByEqual(idp_parent, "")

			case OPERATIONS.ANALYTICAL:
				filter_data.FilterIdpVlpByEqual(idp_skip, False)

		filter_data.Capture(CONTAINERS.CACHE if use_cache else CONTAINERS.DISK)

		return filter_data.Idos(idp_amount).data

	@classmethod
	def Amounts(cls, dy: int, dm: int, dd: int = None, account_ido: str = None, use_cache: bool = False, type_operation: OPERATIONS=OPERATIONS.ALL) -> list[float]:
		""" Список сумм финансовых операций """
		operation         = C80_Operation()
		idc         : str = operation.Idc().data
		idp_account : str = operation.FAccountIdos.Idp().data
		idp_amount  : str = operation.FAmount.Idp().data
		idp_dd      : str = operation.FDd.Idp().data
		idp_dm      : str = operation.FDm.Idp().data
		idp_dy      : str = operation.FDy.Idp().data
		idp_parent  : str = operation.FParentIdo.Idp().data
		idp_skip    : str = operation.FSkip.Idp().data
		idp_virtual : str = operation.FVirtualIdos.Idp().data

		filter_data       = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.FilterIdpVlpByEqual(idp_dd, dd)
		filter_data.FilterIdpVlpByInclude(idp_account, account_ido)

		match type_operation:
			case OPERATIONS.ALL     :
				pass

			case OPERATIONS.PHYSICAL:
				filter_data.FilterIdpVlpByEqual(idp_parent, "")

			case OPERATIONS.VIRTUAL:
				filter_data.FilterIdpVlpByEqual(idp_parent, "", flag_invert=True)

			case OPERATIONS.BASIC:
				filter_data.FilterIdpVlpByEqual(idp_parent, "")
				filter_data.FilterIdpVlpByEqual(idp_virtual,  "")

			case OPERATIONS.PARENT:
				filter_data.FilterIdpVlpByEqual(idp_virtual,  "", flag_invert=True)

			case OPERATIONS.ACCOUNTING:
				filter_data.FilterIdpVlpByEqual(idp_parent, "")

			case OPERATIONS.ANALYTICAL:
				filter_data.FilterIdpVlpByEqual(idp_skip, False)

		filter_data.Capture(CONTAINERS.CACHE if use_cache else CONTAINERS.DISK)

		return filter_data.ToFloats(idp_amount).data

	@classmethod
	def Dds(cls, dy: int, dm: int, include_skip: bool = True, use_cache: bool = False) -> list[float]:
		""" Список чисел месяца финансовых операций """
		operation         = C80_Operation()
		idc         : str = operation.Idc().data
		idp_dd      : str = operation.FDd.Idp().data
		idp_dm      : str = operation.FDm.Idp().data
		idp_dy      : str = operation.FDy.Idp().data
		idp_skip    : str = operation.FSkip.Idp().data

		filter_data       = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.FilterIdpVlpByEqual(idp_skip, None if include_skip else include_skip)
		filter_data.Capture(CONTAINERS.CACHE if use_cache else CONTAINERS.DISK)

		return filter_data.ToIntegers(idp_dd, flag_sort=True, flag_distinct=True).data

	@classmethod
	def SrcDescriptions(cls, dy: int = None, dm: int = None, use_cache: bool = False) -> list[str]:
		""" Список исходных описаний """
		operation                 = C80_Operation()
		idc                 : str = operation.Idc().data
		idp_dy              : str = operation.FDy.Idp().data
		idp_dm              : str = operation.FDm.Idp().data
		idp_src_description : str = operation.FSrcDescription.Idp().data

		filter_data               = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.Capture(CONTAINERS.CACHE if use_cache else CONTAINERS.DISK)

		return filter_data.ToStrings(idp_src_description, True, True).data

	@classmethod
	def Descriptions(cls, dy: int = None, dm: int = None, use_cache: bool = False) -> list[str]:
		""" Список описаний """
		operation             = C80_Operation()
		idc             : str = operation.Idc().data
		idp_dy          : str = operation.FDy.Idp().data
		idp_dm          : str = operation.FDm.Idp().data
		idp_description : str = operation.FDescription.Idp().data

		filter_data           = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.Capture(CONTAINERS.CACHE if use_cache else CONTAINERS.DISK)

		return filter_data.ToStrings(idp_description, True, True).data

	@classmethod
	def Destinations(cls, dy: int = None, dm: int = None, use_cache: bool = False) -> list[str]:
		""" Список описаний """
		operation             = C80_Operation()
		idc             : str = operation.Idc().data
		idp_dy          : str = operation.FDy.Idp().data
		idp_dm          : str = operation.FDm.Idp().data
		idp_destination : str = operation.FDestination.Idp().data

		filter_data           = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.Capture(CONTAINERS.CACHE if use_cache else CONTAINERS.DISK)

		destinations = set()

		for data in filter_data.ToStrings(idp_destination).data:
			destinations.update(set(data.split('\n')))

		return list(sorted(destinations))

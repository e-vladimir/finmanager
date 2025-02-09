# ФИНАНСОВЫЕ ОПЕРАЦИИ: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L00_fields             import FIELDS
from L00_months             import MONTHS

from L70_operations         import C70_Operation, C70_Operations


class C80_Operation(C70_Operation):
	""" Финансовая операция: Логика данных """

	# Обработка
	def Split(self, amount: int) -> str:
		""" Разделение операции """
		self.Amount(self.Amount() - amount)

		accounts        = self.AccountsIdos()
		color           = self.Color()
		dd              = self.Dd()
		det             = self.Detail()
		dm              = self.Dm()
		dst             = self.Destination()
		dy              = self.Dy()
		obj_ext         = self.ObjectExt()
		obj_int         = self.ObjectInt()

		self.GenerateIdo()
		self.RegisterObject(CONTAINERS.DISK)

		self.AccountsIdos(accounts)
		self.Amount(amount)
		self.Color(color)
		self.Dd(dd)
		self.Destination(dst)
		self.Detail(det)
		self.Dm(dm)
		self.Dy(dy)
		self.ObjectExt(obj_ext)
		self.ObjectInt(obj_int)

		return self.Ido().data

	def Clone(self) -> str:
		""" Клонирование операции """
		accounts        = self.AccountsIdos()
		amount          = self.Amount()
		color           = self.Color()
		dd              = self.Dd()
		det             = self.Detail()
		dm              = self.Dm()
		dst             = self.Destination()
		dy              = self.Dy()
		obj_ext         = self.ObjectExt()
		obj_int         = self.ObjectInt()

		self.GenerateIdo()
		self.RegisterObject(CONTAINERS.DISK)

		self.AccountsIdos(accounts)
		self.Amount(amount)
		self.Color(color)
		self.Dd(dd)
		self.Destination(dst)
		self.Detail(det)
		self.Dm(dm)
		self.Dy(dy)
		self.ObjectExt(obj_ext)
		self.ObjectInt(obj_int)

		return self.Ido().data

	# Преобразования
	def DdDmDyToString(self) -> str:
		""" ДД МЕС ГОД """
		dd : str = f"{self.Dd():02d}"
		dm : str = MONTHS(self.Dm()).name_short
		dy : str = f"{self.Dy():04d}"

		return f"{dd} {dm} {dy}"

	def Description(self) -> str:
		""" Формирование описания по шаблону """
		obj_ext     : str = self.ObjectExt()
		obj_int     : str = self.ObjectInt()
		destination : str = self.Destination()
		detail      : str = self.Detail()
		return (' '.join([f"{obj_ext}:" if obj_ext else "",
		                  destination,
		                  ' - ' if all([destination, detail]) else '',
		                  detail,
		                 f"({obj_int})" if obj_int else ""])
		           .replace('  ', ' ')
		           .strip()
		       )


class C80_Operations(C70_Operations):
	""" Финансовые операции: Логика данных """

	# Дни
	@classmethod
	def DdsInDyDm(self, dy: int, dm: int) -> list[int]:
		""" Список дней """
		operation    = C80_Operation()
		idc    : str = operation.Idc().data
		idp_dy : str = operation.f_dy.Idp().data
		idp_dm : str = operation.f_dm.Idp().data
		idp_dd : str = operation.f_dd.Idp().data

		filter_data = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.ToIntegers(idp_dd, True, True).data

	# Финансовые операции
	@classmethod
	def OperationsIdosInDyDmDd(self, dy: int = None, dm: int = None, dd: int = None) -> list[str]:
		""" Список IDO операций в указанном периоде """
		operation         = C80_Operation()
		idc        : str  = operation.Idc().data
		idp_dy     : str  = operation.f_dy.Idp().data
		idp_dm     : str  = operation.f_dm.Idp().data
		idp_dd     : str  = operation.f_dd.Idp().data
		idp_amount : str  = operation.f_amount.Idp().data

		filter_data       = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.FilterIdpVlpByEqual(idp_dd, dd)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.Idos(idp_amount).data

	# Импорт данных
	@classmethod
	def ImportOperation(self, dy: int, dm: int, dd: int, amount: float, account_ido: str, data: dict[str]) -> bool:
		""" Импорт финансовой операции """
		destination : str       = data.get(FIELDS.DESTINATION, "")
		detail      : str       = data.get(FIELDS.DETAIL, "")
		object_int  : str       = data.get(FIELDS.OBJECT_INT,  "")
		object_ext  : str       = data.get(FIELDS.OBJECT_EXT,  "")

		operation               = C80_Operation()
		operation.GenerateIdo()
		operation.RegisterObject(CONTAINERS.DISK)

		operation.AccountsIdos([account_ido])
		operation.Amount(amount)
		operation.Dd(dd)
		operation.Destination(destination)
		operation.Detail(detail)
		operation.Dm(dm)
		operation.Dy(dy)
		operation.ObjectExt(object_ext)
		operation.ObjectInt(object_int)

		return True

	# Периоды
	@classmethod
	def DyStart(self) -> int:
		""" Начало года операций """
		operation          = C80_Operation()
		idc    : str       = operation.Idc().data
		idp_dy : str       = operation.f_dy.Idp().data

		filter_data        = C30_FilterLinear1D(idc)
		filter_data.Capture(CONTAINERS.DISK)

		dys    : list[int] = filter_data.ToIntegers(idp_dy, True, True).data
		return 0 if not dys else min(dys)

	# Выборки данных
	@classmethod
	def Destinations(self, dy: int = None, dm: int = None) -> list[str]:
		""" Список назначений """
		operation             = C80_Operation()
		idc             : str = operation.Idc().data
		idp_destination : str = operation.f_destination.Idp().data
		idp_dy          : str = operation.f_dy.Idp().data
		idp_dm          : str = operation.f_dm.Idp().data

		filter_data           = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.ToStrings(idp_destination, True, True).data

	@classmethod
	def Details(self) -> list[str]:
		""" Список уточнений """
		operation        = C80_Operation()
		idc        : str = operation.Idc().data
		idp_detail : str = operation.f_detail.Idp().data

		filter_data      = C30_FilterLinear1D(idc)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.ToStrings(idp_detail, True, True).data

	@classmethod
	def ObjectsInt(self) -> list[str]:
		""" Список объектов внутренних """
		operation            = C80_Operation()
		idc            : str = operation.Idc().data
		idp_object_int : str = operation.f_object_int.Idp().data

		filter_data          = C30_FilterLinear1D(idc)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.ToStrings(idp_object_int, True, True).data

	@classmethod
	def ObjectsExt(self) -> list[str]:
		""" Список объектов внешних """
		operation            = C80_Operation()
		idc            : str = operation.Idc().data
		idp_object_ext : str = operation.f_object_ext.Idp().data

		filter_data           = C30_FilterLinear1D(idc)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.ToStrings(idp_object_ext, True, True).data

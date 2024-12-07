# ФИНАНСОВЫЕ ОПЕРАЦИИ: ЛОГИКА ДАННЫХ

from hashlib                import md5

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L00_months             import MONTHS
from L00_rules              import RULES

from L70_operations         import C70_Operation, C70_Operations
from L90_rules import C90_ProcessingRule, C90_ProcessingRules


class C80_Operation(C70_Operation):
	""" Финансовая операция: Логика данных """

	# Данные
	def DescriptionOrDestination(self) -> str:
		""" Запрос описания или назначения """
		destination : str = self.Destination()
		
		if not destination: return self.Description()

		return destination

	# Обработка
	def Split(self, amount: int) -> str:
		""" Разделение операции """
		self.Amount(self.Amount() - amount)

		dy              = self.Dy()
		dm              = self.Dm()
		dd              = self.Dd()
		description     = self.Description()
		destination     = self.Destination()
		crc             = self.Crc()
		color           = self.Color()
		labels          = self.Labels()
		accounts        = self.AccountsIdos()

		self.GenerateIdo()
		self.RegisterObject(CONTAINERS.DISK)

		self.Dy(dy)
		self.Dm(dm)
		self.Dd(dd)
		self.Amount(amount)
		self.Description(description)
		self.Destination(destination)
		self.Crc(crc)
		self.Labels(labels)
		self.Color(color)
		self.AccountsIdos(accounts)

		return self.Ido().data

	# Преобразования
	def DdDmDyToString(self) -> str:
		""" ДД МЕС ГОД """
		dd : str = f"{self.Dd():02d}"
		dm : str = MONTHS(self.Dm()).name_s
		dy : str = f"{self.Dy():04d}"

		return f"{dd} {dm} {dy}"

	# Обработка данных
	def ApplyAutoreplaceDescription(self):
		""" Применение правила автозамены описания """
		data_autoreplace : dict[str, str] = dict()
		rules                             = C90_ProcessingRules()

		for ido in rules.IdosByType(RULES.REPLACE_DESCRIPTION):
			rule                    = C90_ProcessingRule(ido)

			data_inputs : list[str] = rule.InputAsStrings()
			data_output : str       = rule.OutputAsString()

			for data_input in data_inputs:
				data_autoreplace[data_input] = data_output

		data_inputs      : list[str]      = sorted(data_autoreplace.keys(), key=len)
		description      : str            = self.Description()

		for data_input in data_inputs:
			description.replace(data_input, data_autoreplace[data_input])

		self.Description(description)


class C80_Operations(C70_Operations):
	""" Финансовые операции: Логика данных """

	# Дни
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
	def OperationsIdosInDyDmDd(self, dy: int, dm: int, dd: int = None) -> list[str]:
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
		if dd is not None: filter_data.FilterIdpVlpByEqual(idp_dd, dd)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.Idos(idp_amount).data

	# Проверки
	def CheckOperationByCrc(self, dy: int, dm: int, crc: str) -> bool:
		""" Проверка операции по CRC """
		operation      = C80_Operation()
		idc     : str  = operation.Idc().data
		idp_dy  : str  = operation.f_dy.Idp().data
		idp_dm  : str  = operation.f_dm.Idp().data
		idp_crc : str  = operation.f_crc.Idp().data

		filter_data    = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy,  dy)
		filter_data.FilterIdpVlpByEqual(idp_dm,  dm)
		filter_data.FilterIdpVlpByEqual(idp_crc, crc)
		filter_data.Capture(CONTAINERS.DISK)

		return bool(filter_data.Idos().data)

	# Импорт данных
	def ImportOperation(self, dy: int, dm: int, dd: int, amount: float, description: str, destination: str, labels: list[str], account_ido: str) -> bool:
		""" Импорт финансовой операции """
		crc = md5(f"{amount:0.2f}{dy:04d}{dm:02d}{dd:02d}{description}".encode("utf-8")).hexdigest()

		if self.CheckOperationByCrc(dy, dm, crc): return False

		operation = C80_Operation()
		operation.GenerateIdo()
		operation.RegisterObject(CONTAINERS.DISK)

		operation.Dy(dy)
		operation.Dm(dm)
		operation.Dd(dd)
		operation.Crc(crc)
		operation.Description(description)
		operation.Destination(destination)
		operation.Amount(amount)
		operation.AccountsIdos([account_ido])
		operation.Labels(labels)

		operation.ApplyAutoreplaceDescription()

		return True

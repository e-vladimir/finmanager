# СТРУКТУРЫ ДАННЫХ ПРОЕКТА

from dataclasses import dataclass, field


@dataclass
class T20_Day:
	""" Структура данных аналитики дня """
	is_weekend     : bool = False
	amount_income  : int  = 0
	amount_outcome : int  = 0


@dataclass
class T20_AmountItem:
	""" Структура данных аналитики """
	name          : str = ""
	amount_income : int = 0
	amount_outcome: int = 0


@dataclass
class T20_PredictDescriptionItem:
	""" Структура данных предиктивного определения описания """
	data : dict[str, float] = field(default_factory=dict)

	def Append(self, item: str):
		""" Добавление данных """
		self.data[item] = self.data.get(item, 0) + 1

	def CalcWeights(self):
		""" Расчёт весовых коэффициентов """
		count = sum(self.data.values())

		for item, subcount in self.data.items():
			self.data[item] = subcount / count


@dataclass
class T20_RawOperation:
	""" Структура данных операции """
	amount          : int       = 0
	src_description : str       = ""
	description     : str       = ""
	destination     : list[str] = field(default_factory=list)


@dataclass
class T20_StructItem:
	""" Структура структуры """
	name   : str  = ""
	ido    : str  = ""
	parent : str  = ""
	items  : list = field(default_factory=list)

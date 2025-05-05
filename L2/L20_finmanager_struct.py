# СТРУКТУРЫ ДАННЫХ ПРОЕКТА

from dataclasses import dataclass, field

from G10_list import ClearList


@dataclass
class T20_Day:
	is_weekend     : bool = False
	amount_income  : int  = 0
	amount_outcome : int  = 0


@dataclass
class T20_PredictDescriptionItem:
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
	amount          : int       = 0
	src_description : str       = ""
	description     : str       = ""
	destination     : list[str] = field(default_factory=list)
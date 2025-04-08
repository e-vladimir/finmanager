# СТРУКТУРЫ ДАННЫХ ПРОЕКТА

from dataclasses import dataclass, field


@dataclass
class T20_Day:
	is_weekend     : bool = False
	amount_income  : int  = 0
	amount_outcome : int  = 0


@dataclass
class T20_PredictItem:
	intput  : str = ""
	inputs  : dict[str, float] = field(default_factory=dict)

	output  : str = ""
	outputs : dict[str, float] = field(default_factory=dict)


@dataclass
class T20_RawOperation:
	amount      : int = 0
	description : str = ""
	destination : str = ""

	def __hash__(self): return hash(f"{self.description}-{self.destination}")

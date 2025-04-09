# СТРУКТУРЫ ДАННЫХ ПРОЕКТА

from dataclasses import dataclass, field

from G10_list    import ClearList


@dataclass
class T20_Day:
	is_weekend     : bool = False
	amount_income  : int  = 0
	amount_outcome : int  = 0


@dataclass
class T20_PredictItem:
	input   : str              = ""
	inputs  : dict[str, float] = field(default_factory=dict)

	output  : str              = ""
	outputs : dict[str, float] = field(default_factory=dict)

	def IncInputs(self, items: list[str]):
		""" Добавление значения во входные условия """
		for item in ClearList(items):
			self.inputs[item] = self.inputs.get(item, 0) + 1

	def CalcInputsWights(self):
		""" Расчёт весовых коэффициентов """
		count: int = sum([count for _, count in self.inputs.items()])

		for item, processing_count in self.inputs.items():
			self.inputs[item] = processing_count / count

	def CalcInput(self):
		""" Определение элемента с наибольшим весовым коэффициентом """
		processing_weight : float = 0.00

		for item, weight in self.inputs.items():
			if processing_weight > weight: continue

			processing_weight = weight

			self.input = item

	def IncOutputs(self, items: list[str], mode_raw: bool = False):
		""" Добавление значения в выходные условия """
		for item in ClearList(items, clear_short = not mode_raw, clear_numbers = not mode_raw, clear_simbols = not mode_raw):
			self.outputs[item] = self.outputs.get(item, 0) + 1

	def CalcOutputsWights(self):
		""" Расчёт весовых коэффициентов """
		count: int = sum([count for _, count in self.outputs.items()])

		for item, processing_count in self.outputs.items():
			self.outputs[item] = processing_count / count

	def CalcOutput(self):
		""" Определение элемента с наибольшим весовым коэффициентом """
		processing_weight : float = 0.00

		for item, weight in self.outputs.items():
			if processing_weight > weight: continue

			processing_weight = weight

			self.output = item


@dataclass
class T20_RawOperation:
	amount      : int       = 0
	description : str       = ""
	destination : str       = ""
	labels      : list[str] = field(default_factory=list)

	def __hash__(self): return hash(f"{self.description}-{self.destination}")

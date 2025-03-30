# ПРАВИЛА ОБРАБОТКИ ДАННЫХ: МЕХАНИКА ДАННЫХ
# 30 мар 2025

from L00_containers       import CONTAINERS
from L00_rules            import RULES
from L50_processing_rules import C50_ProcessingRule, C50_ProcessingRules


class C60_ProcessingRule(C50_ProcessingRule):
	""" Правило обработки данных: Механика данных """

	# Тип правил
	@property
	def rules_type(self) -> RULES:
		return RULES(self.FRulesType.ToString(CONTAINERS.DISK).data)

	@rules_type.setter
	def rules_type(self, value: RULES):
		self.FRulesType.FromString(CONTAINERS.DISK, value)


	# Вход
	@property
	def input(self) -> str:
		return self.FInput.ToString(CONTAINERS.DISK).data

	@input.setter
	def input(self, data: str):
		self.FInput.FromString(CONTAINERS.DISK, data)

	@property
	def inputs(self) -> list[str]:
		return self.FInput.ToStrings(CONTAINERS.DISK).data

	@inputs.setter
	def inputs(self, data: list[str]):
		self.FInput.FromStrings(CONTAINERS.DISK, data)


	# Блок
	@property
	def block(self) -> str:
		return self.FBlock.ToString(CONTAINERS.DISK).data

	@block.setter
	def block(self, data: str):
		self.FBlock.FromString(CONTAINERS.DISK, data)

	@property
	def blocks(self) -> list[str]:
		return self.FBlock.ToStrings(CONTAINERS.DISK).data

	@blocks.setter
	def blocks(self, data: list[str]):
		self.FBlock.FromStrings(CONTAINERS.DISK, data)


	# Выход
	@property
	def output(self) -> str:
		return self.FOutput.ToString(CONTAINERS.DISK).data

	@output.setter
	def output(self, data: str):
		self.FOutput.FromString(CONTAINERS.DISK, data)

	@property
	def outputs(self) -> list[str]:
		return self.FOutput.ToStrings(CONTAINERS.DISK).data

	@outputs.setter
	def outputs(self, data: list[str]):
		self.FOutput.FromStrings(CONTAINERS.DISK, data)



class C60_ProcessingRules(C50_ProcessingRules):
	""" Правила обработки данных: Механика данных """
	pass

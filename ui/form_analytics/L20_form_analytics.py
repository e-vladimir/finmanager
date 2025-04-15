# ФОРМА АНАЛИТИКА ДАННЫХ: СТРУКУРА ДАННЫХ

from dataclasses import dataclass, field


@dataclass
class T20_AnalyticItem:
	""" Структура данных аналитики """
	name    : str = ""
	income  : int = 0
	outcome : int = 0


@dataclass
class T20_Operation:
	""" Структура данных операции """
	dd     : int      = 0
	amount : float    = 0
	labels : set[str] = field(default_factory=set)

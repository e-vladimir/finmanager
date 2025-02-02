# СТРУКТУРА ДАННЫХ СТАТИСТИКА

from dataclasses import dataclass


@dataclass
class T20_StructStatistic:
	""" Структура данных статистики """
	name           : str = ""
	amount_income  : int = 0
	amount_outcome : int = 0

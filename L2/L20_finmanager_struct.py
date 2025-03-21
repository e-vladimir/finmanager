# СТРУКТУРЫ ДАННЫХ ПРОЕКТА

from dataclasses import dataclass


@dataclass
class T20_Day:
	is_weekend     : bool = False
	amount_income  : int  = 0
	amount_outcome : int  = 0

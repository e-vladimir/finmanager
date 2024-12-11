# ПРОЕКТ: СТРУКУРЫ ДАННЫХ

from dataclasses import dataclass


@dataclass
class T20_StatisticItem:
	""" Элемент статистики """
	label          : str = ""
	amount_income  : int = 0
	amount_outcome : int = 0

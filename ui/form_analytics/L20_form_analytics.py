# ФОРМА АНАЛИТИКИ ДАННЫХ: СТРУКТУРЫ ДАННЫХ

from dataclasses import dataclass


@dataclass
class T20_DynamicDyItem:
	""" Элемент аналитики динамики объёма за год """
	dm             : int = 0
	dy             : int = 0
	amount_income  : int = 0
	amount_outcome : int = 0

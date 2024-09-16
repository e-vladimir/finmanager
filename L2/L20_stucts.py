# СТРУКТУРЫ ПРОЕКТА

from dataclasses import dataclass


@dataclass
class T20_FinstatisticsItem:
	""" Элемент финстатистики """
	income  : int = 0
	outcome : int = 0

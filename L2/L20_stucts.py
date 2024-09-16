# СТРУКТУРЫ ПРОЕКТА

from dataclasses import dataclass


@dataclass
class T20_FinstatisticItem:
	""" Элемент финстатистики """
	income  : int = 0
	outcome : int = 0

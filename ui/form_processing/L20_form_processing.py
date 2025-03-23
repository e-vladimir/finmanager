# ФОРМА ОБРАБОТКА ДАННЫХ: СТРУКТУРА ДАННЫХ
# 22 мар 2025

from dataclasses import dataclass
from typing      import Any


@dataclass
class T20_ProcessingItem:
	""" Элемент обработки данных """
	enable : bool = False
	data   : Any  = None

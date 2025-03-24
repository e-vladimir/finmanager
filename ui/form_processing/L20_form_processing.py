# ФОРМА ОБРАБОТКА ДАННЫХ: СТРУКТУРА ДАННЫХ
# 22 мар 2025

import dataclasses

from   typing import Any


@dataclasses.dataclass
class T20_ProcessingItem:
	""" Элемент обработки данных """
	enable : bool = False
	data   : Any  = None

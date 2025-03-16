# СТРУКТУРА ДАННЫХ: ИМПОРТ ДАННЫХ

from dataclasses import dataclass

from L00_fields  import FIELDS


@dataclass
class T20_OperationsStruct:
	""" Структура данных импорта операций """
	name  : str    = ""
	field : FIELDS = FIELDS.NONE

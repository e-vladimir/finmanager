# СТРУКТУРА ДАННЫХ: ИМПОРТ ДАННЫХ

from dataclasses import dataclass

from L00_fields  import DATA_FIELDS


@dataclass
class T20_OperationsStruct:
	""" Структура данных импорта операций """
	name  : str    = ""
	field : DATA_FIELDS = DATA_FIELDS.NONE

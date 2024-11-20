# КАТАЛОГ ПРОЕКТА: СТРУКТУРЫ ДАННЫХ ЭКСПОРТА

import enum


class EXPORT_ID(enum.StrEnum):
	""" Каталог проекта: ИД """
	ACCOUNT   = "Счёт"
	DIRECTORY = "Директория"
	FILENAME  = "Имя файла"
	INPUT     = "Захват данных"
	MODE_DATE = "Режим периода данных"
	OUTPUT    = "Экспорт данных"


class EXPORT_MODE_DATE(enum.StrEnum):
	""" Каталог проекта: Период """
	ALL = "Все периоды"
	DY  = "Год"
	DM  = "Месяц"


class EXPORT_MODE_ACCOUNTS(enum.StrEnum):
	""" Каталог проекта: Счета """
	ALL    = "Все счета"
	GROUP  = "Группа счетов"
	SINGLE = "Один счёт"

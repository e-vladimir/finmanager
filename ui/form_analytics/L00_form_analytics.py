# ФОРМА АНАЛИТИКА ДАННЫХ: КАТАЛОГ

import enum


class ANALYTICS_FIELDS(enum.StrEnum):
	""" Каталог параметров элемента аналитики данных """
	NONE    = "Нет данных"

	INCLUDE = "Признаки+"
	EXCLUDE = "Признаки-"


class ANALYTICS_DATA(enum.StrEnum):
	""" Структура данных аналитики """
	NONE         = "Нет данных"

	DYNAMIC_DY   = "Динамика объёма за год"
	DYNAMIC_DM   = "Динамика объёма за месяц"
	INTERVAL     = "Интервал"
	DISTRIBUTION = "Распределение объёма"

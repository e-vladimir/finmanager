# ФОРМА АНАЛИТИКА ДАННЫХ: КАТАЛОГ

import enum


class ANALYTICS_FIELDS(enum.StrEnum):
	""" Каталог параметров элемента аналитики данных """
	NONE    = "Нет данных"

	INCLUDE = "Признаки+"
	EXCLUDE = "Признаки-"


class ANALYTICS_DATA(enum.StrEnum):
	""" Каталог структуры данных аналитики """
	NONE      = "Нет данных"

	DISTRIBUTION = "Распределение"

	VOLUME    = "Объём"
	VOLUME_25 = "Объём 25%"
	VOLUME_50 = "Объём 50%"
	VOLUME_75 = "Объём 75%"
	VOLUME_80 = "Объём 80%"

	DW_1      = "1 неделя"
	DW_2      = "2 неделя"
	DW_3      = "3 неделя"
	DW_4      = "4 неделя"

	VOLUME_AVG  = "Средний объём"
	VOLUME_MODA = "Базовый объём"

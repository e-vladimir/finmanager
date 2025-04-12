# ФОРМА АНАЛИТИКА ДАННЫХ: КАТАЛОГ

import enum


class ANALYTICS_FIELDS(enum.StrEnum):
	""" Каталог параметров элемента аналитики данных """
	NONE    = "Нет данных"

	INCLUDE = "Признаки+"
	EXCLUDE = "Признаки-"

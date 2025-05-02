# ФОРМА АНАЛИТИКА ДАННЫХ: КАТАЛОГ ДАНННЫХ

import enum


class GROUPS(enum.StrEnum):
	""" Каталог групп аналитики данных """
	NONE         = "Нет данных"

	DISTRIBUTION = "Распределение месяца"
	DYNAMIC_DM   = "Динамика месяца"
	DYNAMIC_DY   = "Динамика года"

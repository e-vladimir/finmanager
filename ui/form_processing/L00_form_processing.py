# КАТАЛОГ ПРОЕКТА: ФОРМА ОБРАБОТКИ ДАННЫХ

import enum


class OPERATIONS(enum.StrEnum):
	""" Каталог Обработка операций """
	INCLUDE     = "Фрагмент поиска"
	EXCLUDE     = "Фрагмент исключения"
	DESTINATION = "Назначение"
	DETAIL      = "Уточнение"
	OBJECT_INT  = "Объект внутренний"
	OBJECT_EXT  = "Объект внешний"
	COLOR       = "Цветовая метка"
	INTERVAL    = "Период обработки"


class INTERVALS(enum.StrEnum):
	""" Интервалы """
	DM  = "Месяц"
	ALL = "Все периоды"

# КАТАЛОГ: ПОЛЯ

import enum


class FIELDS(enum.StrEnum):
	""" Каталог полей """
	AMOUNT    = "Сумма",
	DATE_TIME = "Дата/время",
	NOTE      = "Описание",
	CONTROL   = "Контроль"

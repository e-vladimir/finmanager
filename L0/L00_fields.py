# КАТАЛОГ: ПОЛЯ

import enum


class FIELDS(enum.Enum):
	""" Каталог полей """
	AMOUNT    = "Сумма",

	DATE      = "Дата",
	TIME      = "Время",
	DATE_TIME = "Дата и время",

	NOTE      = "Описание",
	CONTROL   = "Контроль"

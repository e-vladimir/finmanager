# КАТАЛОГ ПРОЕКТА: ТИПЫ ПОЛЕЙ

import enum


class FIELDS(enum.StrEnum):
	""" Каталог проекта: Типы полей """

	NONE        = ""

	AMOUNT      = "Сумма"
	DATE        = "Дата"
	DESCRIPTION = "Описание"

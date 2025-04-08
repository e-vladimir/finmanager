# ФОРМА ИМПОРТ ДАННЫХ: КАТАЛОГИ

import enum


class FORMATS(enum.StrEnum):
	""" Каталог форматов """

	SBERBANK_2024_11 = "Сбербанк (с ноя 2024)"


class DATA_FIELDS(enum.StrEnum):
	""" Каталог проекта: Типы полей """

	NONE        = ""

	AMOUNT      = "Сумма"
	DATE        = "Дата"
	DESCRIPTION = "Описание"

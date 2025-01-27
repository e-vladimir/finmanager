# КАТАЛОГ ПРОЕКТА: ТИПЫ ПОЛЕЙ

import enum


class FIELDS(enum.StrEnum):
	""" Каталог проекта: Типы полей """
	AMOUNT      = "Сумма"
	DATE        = "Дата"
	DESTINATION = "Назначение"
	DETAIL     = "Уточнение"
	OBJECT_INT  = "Объект внутренний"
	OBJECT_EXT  = "Объект внешний"

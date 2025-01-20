# КАТАЛОГ ПРОЕКТА: ТИПЫ ПОЛЕЙ

import enum


class FIELDS(enum.StrEnum):
	""" Каталог проекта: Типы полей """
	AMOUNT      = "Сумма"
	DATE        = "Дата"
	DESCRIPTION = "Описание"
	DESTINATION = "Назначение"
	OBJECT_INT  = "Объект внутренний"
	OBJECT_EXT  = "Объект внешний"

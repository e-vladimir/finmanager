# КАТАЛОГ ПРОЕКТА: ТИП ОПЕРАЦИЙ

import enum


class OPERATIONS(enum.StrEnum):
	""" Тип операций """
	ALL        = "Все"

	PHYSICAL   = "Физические"
	VIRTUAL    = "Виртуальные"

	BASIC      = "Базовые"
	PARENT     = "Корневые"

	ACCOUNTING = "Учётные"
	ANALYTICAL = "Аналитические"

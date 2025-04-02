# ФОРМА ЭКСПОРТ ДАННЫХ: КАТАЛОГ ПРОЕКТА
# 22 мар 2025

import enum


class EXPORT(enum.StrEnum):
	""" Общий набор параметров экспорта """
	NONE      = "Нет данных"

	INTERVAL  = "Интервал"
	DIRECTORY = "Директория"
	ACCOUNTS  = "Счета"

	@classmethod
	def _missing_(cls, value): return cls.NONE


class ACCOUNTS(enum.StrEnum):
	""" Виды счетов """
	ALL     = "Все счета"
	GROUP   = "Группа счетов"
	ACCOUNT = "Счёт"

	@classmethod
	def _missing_(cls, value): return cls.ALL


class INTERVALS(enum.StrEnum):
	""" Виды интервалов """
	ALL = "Весь доступный период"
	DY  = "Год"
	DM  = "Месяц"

	@classmethod
	def _missing_(cls, value): return cls.ALL

# КАТАЛОГ ПРОЕКТА: ФИНАНАЛИТИКА

import enum


class FINANALITICS(enum.StrEnum):
	IDOS   = "Список IDO"
	LABELS = "Список меток"
	AMOUNTS = "Список сумм"
	DDS = "Список дат"

	INCOME_AMOUNT_SUM = "Общая сумма поступления"
	INCOME_AMOUNT_MIN = "Минимальная сумма поступления"
	INCOME_AMOUNT_MAX = "Максимальная сумма поступления"
	INCOME_AMOUNT_AVG = "Средняя сумма поступления"
	INCOME_COUNT = "Количество поступлений"

	OUTCOME_AMOUNT_SUM = "Общая сумма выбытия"
	OUTCOME_AMOUNT_MIN = "Минимальная сумма выбытия"
	OUTCOME_AMOUNT_MAX = "Максимальная сумма выбытия"
	OUTCOME_AMOUNT_AVG = "Средняя сумма выбытия"
	OUTCOME_COUNT = "Количество выбытий"

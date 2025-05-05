# ПРЕДИКТИВНЫЙ АНАЛИЗАТОР ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 08 апр 2025

import asyncio

from   L80_data_completer import C80_DataCompleter


class C90_DataCompleter(C80_DataCompleter):
	""" Предиктивный анализатор данных: Логика управления """

	# Модель предиктивного определения описания
	def on_RequestCalcDataDescriptions(self):
		""" Запрос на подготовку данных предиктивного определения описания """
		asyncio.run(self.CalcDataDescriptions())


	# Модель предиктивного определения назначения
	def on_RequestCalcDataDestinations(self):
		""" Запрос на подготовку данных предиктивного определения назначения """
		asyncio.run(self.CalcDataDestinations())

# ПРЕДИКТИВНЫЙ АНАЛИЗАТОР ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 08 апр 2025

import threading
import nltk

from   L80_data_completer import C80_DataCompleter


class C90_DataCompleter(C80_DataCompleter):
	""" Предиктивный анализатор данных: Логика управления """

	# Модуль
	def on_Started(self):
		""" Модуль запущен """
		nltk.download("stopwords")

		threading.Thread(target=self.ReadDataOperations, daemon=True).start()


	# Данные об операциях
	def on_DataOperationsLoaded(self):
		""" Данные об операциях загружены """
		self.on_RequestCalcDataDescriptions()
		self.on_RequestCalcDataDestinations()


	# Модель предиктивного определения описания
	def on_RequestCalcDataDescriptions(self):
		""" Запрос на подготовку данных предиктивного определения описания """
		threading.Thread(target=self.CalcDataDescriptions, daemon=True).start()


	# Модель предиктивного определения назначения
	def on_RequestCalcDataDestinations(self):
		""" Запрос на подготовку данных предиктивного определения назначения """
		threading.Thread(target=self.CalcDataDestinations, daemon=True).start()

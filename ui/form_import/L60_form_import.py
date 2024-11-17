# ФОРМА ИМПОРТ ДАННЫХ: МЕХАНИКА ДАННЫХ

import random

from   L50_form_import import C50_FormImport


class C60_FormImport(C50_FormImport):
	""" Форма Импорт данных: Механика данных """

	# Модель импорта операций
	def InitModelOperations(self):
		""" Инициализация модели данных Операций """
		self.model_operations.removeAll()

		self.model_operations.setHorizontalHeaderLabels(["Заголовок файла", "Сопоставление", "Данные"])

		for _ in self._operations_options: self.model_operations.fastAppendRow(["", "", ""])

	def LoadOperationsHeader(self):
		""" Загрузка заголовка импорта операций """
		for index_header in range(self.model_operations.rowCount()):
			item_header = self.model_operations.item(index_header, 0)

			try   :	item_header.setText(self._operations_options[index_header])
			except:	item_header.setText("")

	def LoadOperationsOptions(self):
		""" Загрузка параметров импорта операций """
		for index_options in range(self.model_operations.rowCount()):
			item_options = self.model_operations.item(index_options, 1)

			try   :	item_options.setText(self._operations_options[index_options])
			except:	item_options.setText("")

	def LoadOperationsData(self):
		""" Загрузка данных импорта операций """
		data : list = []

		try   : data = self._operations_data[random.randint(0, len(self._operations_data))]
		except: pass

		for index_data in range(self.model_operations.rowCount()):
			item_data = self.model_operations.item(index_data, 1)

			try   :	item_data.setText(data[index_data])
			except:	item_data.setText("")

# ФОРМА ИМПОРТ ДАННЫХ: МЕХАНИКА ДАННЫХ
# 14 мар 2025

from pathlib         import Path

from L00_fields      import DATA_FIELDS
from L20_PySide6     import C20_StandardItem
from L20_form_import import T20_OperationsStruct
from L50_form_import import C50_FormImport


class C60_FormImport(C50_FormImport):
	""" Форма Импорт данных: Механика данных """

	# Импорт операций: Данные
	@property
	def operations_data(self) -> list:
		return self._operations_data[:]
	@operations_data.setter
	def operations_data(self, data: list):
		self._operations_data = data[:]

	# Импорт операций: Путь к файлу
	@property
	def operations_filepath(self) -> Path | None:
		return self._operations_filepath
	@operations_filepath.setter
	def operations_filepath(self, path: Path):
		if not path.exists(): return
		if     path.is_dir(): return

		self._operations_filepath = path

	# Импорт операций: Структура данных
	@property
	def operations_struct_names(self) -> list[str]:
		return [item.name for item in self._operations_struct]
	@operations_struct_names.setter
	def operations_struct_names(self, names: list[str]):
		self._operations_struct = [T20_OperationsStruct(name=name) for name in names]

	def GetOperationsStructField(self, name_or_index: str | int) -> DATA_FIELDS:
		""" Получение типа поля для структуры данных операции """
		match type(name_or_index):
			case str():
				for item in self._operations_struct:
					if not item.name == name_or_index: continue

					return item.field
				else:
					return DATA_FIELDS.NONE

			case int():
				try   : return self._operations_struct[name_or_index].field
				except: pass

		return DATA_FIELDS.NONE

	def SetOperationsStructField(self, name_or_index: str | int, field: DATA_FIELDS):
		""" Установка типа поля для структуры данных операций """

		match name_or_index:
			case str():
				for item in self._operations_struct:
					if not item.name == name_or_index: continue

					item.field = field
					break

			case int():
				try   : self._operations_struct[name_or_index].field = field
				except: pass

	def IndexOperationsStructByField(self, field: DATA_FIELDS) -> int:
		""" Индекс поля структуры данных импорта операций """
		for idx, item in enumerate(self._operations_struct):
			if item.field == field: return idx
		else: return -1

	def AutodetectOperationsStructFields(self):
		""" Авто-определение типов полей структуры операций """
		for field in DATA_FIELDS:
			if field == DATA_FIELDS.NONE: continue

			for struct_item in self._operations_struct:
				flag_equal : bool = field.value      in struct_item.name
				flag_equal       |= struct_item.name in field.value

				if not flag_equal: continue

				struct_item.field = field
				break

	# Рабочий индекс строки
	@property
	def processing_row(self) -> int:
		return self._processing_row
	@processing_row.setter
	def processing_row(self, idx: int):
		self._processing_row = idx

	def ReadProcessingRowFromTableDataOperations(self):
		""" Чтение рабочей строки из таблицы данных импорта операций """
		self.processing_row = self.TableDataOperations.currentIndex().row()

	# Модель данных
	def InitModelDataOperations(self):
		""" Загрузка модели данных импорта операций """
		self.ModelDataOperations.removeAll()

		self.ModelDataOperations.setHorizontalHeaderLabels(["Заголовок", "Параметр", "Данные"])

		for struct_item in self.operations_struct_names:
			self.ModelDataOperations.appendRow([C20_StandardItem(struct_item),
			                                    C20_StandardItem(""),
			                                    C20_StandardItem("")])

	def LoadModelDataOperations(self):
		""" Загрузка данных в модель данных импорта операций """
		data = self.operations_data[0]

		for idx_row, subdata in enumerate(data):
			item_field = self.ModelDataOperations.item(idx_row, 1)
			item_field.setText(self._operations_struct[idx_row].field)

			item_data  = self.ModelDataOperations.item(idx_row, 2)
			item_data.setText(subdata)

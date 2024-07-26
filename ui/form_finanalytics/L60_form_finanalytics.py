# ФОРМА ФИНАНАЛИЗ: МЕХАНИКА ДАННЫХ

import statistics

from   PySide6.QtCore        import QModelIndex

from   L00_dict              import *
from   L00_months            import MONTHS_SHORT
from   L00_roles             import ROLE_TYPE

from   L10_converts          import AmountToString
from   L11_datetime          import CalcDyDmByShiftDm
from   L20_PySide6           import C20_StandardItem, ROLE_OID
from   L50_form_finanalytics import C50_FormFinanalytics
from   L90_findescription    import C90_RecordFindescription


class C60_FormFinanalytics(C50_FormFinanalytics):
	""" Форма Финанализ: Механика данных """

	# Параметры
	def ReadIdoProcessingFromTableFindescriptionDynamic(self):
		""" Чтение OID для обработки """
		self._oid_processing = ""

		index_data : QModelIndex | None = self.table_findescription_dynamic.currentIndex()
		if     index_data is None  : return
		if not index_data.isValid(): return

		data       : str | None         = index_data.data(ROLE_OID)
		if     data is None        : return

		self._oid_processing = data

	# Модель динамики финсостава
	def SetupModelFindescriptionDynamic(self):
		""" Настройка модели """
		self.model_findescription_dynamic.removeAll()
		self.model_findescription_dynamic.setHorizontalHeaderLabels(["Параметр"] + [""] * 16)

	def LoadModelFindescriptionDynamicSeparator(self):
		""" Загрузка разделителя в модель """
		index_row : int = self.model_findescription_dynamic.rowCount()
		for index_shift in range(17):
			self.model_findescription_dynamic.setItem(index_row, index_shift, C20_StandardItem("", SEPARATOR, ROLE_TYPE))

	def LoadModelFindescriptionDynamicIncome(self):
		""" Загрузка секции Поступило в модель """
		labels         : list[str] = []
		dy             : int       = self.workspace.Dy()
		dm             : int       = self.workspace.Dm()
		for index_shift in range(13):
			labels.append(f"{MONTHS_SHORT[dm]}\n{dy}")

			dy, dm = CalcDyDmByShiftDm(dy, dm, -1)
		labels.extend(["МИН", "МЕД", "МАКС"])

		index_row      : int       = self.model_findescription_dynamic.rowCount()
		self.model_findescription_dynamic.setItem(index_row, 0, C20_StandardItem("ПОСТУПИЛО", f"{HEADER}_{INCOME}", ROLE_TYPE))
		for index_shift, label in enumerate(labels):
			self.model_findescription_dynamic.setItem(index_row, 1 + index_shift, C20_StandardItem(label))

		findescription_names : list[str] = list(sorted(self._data_findescription_dynamic_income.keys()))
		for findescription_name in findescription_names:
			index_row      : int       = self.model_findescription_dynamic.rowCount()

			amounts_income : list[int] = self._data_findescription_dynamic_income.get(findescription_name, [0] * 13)

			amount_min     : int       = min(amounts_income)
			amount_med     : int       = int(statistics.median(amounts_income))
			amount_max     : int       = max(amounts_income)

			amounts_income.append(amount_min)
			amounts_income.append(amount_med)
			amounts_income.append(amount_max)

			record_findescription      = C90_RecordFindescription()
			record_findescription.SwitchByName(findescription_name)

			item_record                = C20_StandardItem(findescription_name)
			item_record.setData(FINDESCRIPTION, ROLE_TYPE)
			item_record.setData(record_findescription.Ido().data, ROLE_OID)

			self.model_findescription_dynamic.setItem(index_row, 0, item_record)

			for index_shift, amount in enumerate(amounts_income):
				self.model_findescription_dynamic.setItem(index_row, 1 + index_shift, C20_StandardItem(AmountToString(amount), record_findescription.Ido().data, ROLE_OID))

		index_row      : int       = self.model_findescription_dynamic.rowCount()
		self.model_findescription_dynamic.setItem(index_row, 0, C20_StandardItem("СУММА", f"{FOOTER}_{INCOME}", ROLE_TYPE))

		amounts_income : list[int] = [0] * 13

		for findescription_name, amounts in self._data_findescription_dynamic_income.items():
			for index_shift in range(13): amounts_income[index_shift] += amounts[index_shift]

		amount_min     : int       = min(amounts_income)
		amount_med     : int       = int(statistics.median(amounts_income))
		amount_max     : int       = max(amounts_income)

		amounts_income.append(amount_min)
		amounts_income.append(amount_med)
		amounts_income.append(amount_max)

		for index_shift, amount in enumerate(amounts_income):
			self.model_findescription_dynamic.setItem(index_row, 1 + index_shift, C20_StandardItem(AmountToString(amount)))

	def LoadModelFindescriptionDynamicOutcome(self):
		""" Загрузка секции Выбыло в модель """
		labels         : list[str] = []
		dy             : int       = self.workspace.Dy()
		dm             : int       = self.workspace.Dm()
		for index_shift in range(13):
			labels.append(f"{MONTHS_SHORT[dm]}\n{dy}")

			dy, dm = CalcDyDmByShiftDm(dy, dm, -1)
		labels.extend(["МИН", "МЕД", "МАКС"])

		index_row      : int       = self.model_findescription_dynamic.rowCount()
		self.model_findescription_dynamic.setItem(index_row, 0, C20_StandardItem("ВЫБЫЛО", f"{HEADER}_{OUTCOME}", ROLE_TYPE))
		for index_shift, label in enumerate(labels):
			self.model_findescription_dynamic.setItem(index_row, 1 + index_shift, C20_StandardItem(label))

		findescription_names : list[str] = list(sorted(self._data_findescription_dynamic_outcome.keys()))
		for findescription_name in findescription_names:
			index_row      : int       = self.model_findescription_dynamic.rowCount()

			amounts_outcome : list[int] = self._data_findescription_dynamic_outcome.get(findescription_name, [0] * 13)

			amount_min     : int       = min(amounts_outcome)
			amount_med     : int       = int(statistics.median(amounts_outcome))
			amount_max     : int       = max(amounts_outcome)

			amounts_outcome.append(amount_min)
			amounts_outcome.append(amount_med)
			amounts_outcome.append(amount_max)

			record_findescription      = C90_RecordFindescription()
			record_findescription.SwitchByName(findescription_name)

			item_record                = C20_StandardItem(findescription_name)
			item_record.setData(FINDESCRIPTION, ROLE_TYPE)
			item_record.setData(record_findescription.Ido().data, ROLE_OID)

			self.model_findescription_dynamic.setItem(index_row, 0, item_record)

			for index_shift, amount in enumerate(amounts_outcome):
				self.model_findescription_dynamic.setItem(index_row, 1 + index_shift, C20_StandardItem(AmountToString(amount), record_findescription.Ido().data, ROLE_OID))

		index_row      : int       = self.model_findescription_dynamic.rowCount()
		self.model_findescription_dynamic.setItem(index_row, 0, C20_StandardItem("СУММА", f"{FOOTER}_{OUTCOME}", ROLE_TYPE))

		amounts_outcome : list[int] = [0] * 13

		for findescription_name, amounts in self._data_findescription_dynamic_outcome.items():
			for index_shift in range(13): amounts_outcome[index_shift] += amounts[index_shift]

		amount_min     : int       = min(amounts_outcome)
		amount_med     : int       = int(statistics.median(amounts_outcome))
		amount_max     : int       = max(amounts_outcome)

		amounts_outcome.append(amount_min)
		amounts_outcome.append(amount_med)
		amounts_outcome.append(amount_max)

		for index_shift, amount in enumerate(amounts_outcome):
			self.model_findescription_dynamic.setItem(index_row, 1 + index_shift, C20_StandardItem(AmountToString(amount)))

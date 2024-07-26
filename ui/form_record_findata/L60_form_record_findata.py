# ФОРМА ЗАПИСИ ФИНДАННЫХ: МЕХАНИКА ДАННЫХ

from PySide6.QtCore          import QModelIndex, Qt

from L00_dict                import *

from L10_converts            import AmountToString
from L11_datetime            import DAYS_IN_MONTH
from L20_PySide6             import C20_StandardItem, ROLE_OID
from L50_form_record_findata import C50_FormRecordFindata
from L90_finactions          import C90_RecordFinactions
from L90_finstruct           import C90_RecordFinstruct


class C60_FormRecordFindata(C50_FormRecordFindata):
	""" Форма записи финданных: Механика данных """

	# Параметры
	def EnableLockReading(self):
		""" Включение доступа обработки """
		self._lock_reading = True

	def DisableLockReading(self):
		""" Отключение доступа обработки """
		self._lock_reading = False

	def ReadIdoProcessingFromTblData(self):
		""" Чтение текущего OID """
		self._ido_processing = ""

		index_selected : QModelIndex = self.table_data.currentIndex()
		if not index_selected.isValid(): return

		self._ido_processing = index_selected.data(ROLE_OID)

	def ReadRowProcessingFromTblData(self):
		""" Чтение текущей строки """
		self._row_processing = -1

		index_current : QModelIndex = self.table_data.currentIndex()
		if not index_current.isValid(): return

		self._row_processing = index_current.row()

	def SetupRecordFindata(self):
		""" Настройка записи финданных """
		self.record_findata.Ido(self.workspace.IdoRecordFindata())

	# Модель данных
	def SetupModelData(self):
		""" Подготовка модели данных """
		self.model_data.removeAll()
		self.model_data.setHorizontalHeaderLabels(["Параметр", "Значение"])

		self.model_data.setItem(0, 0, C20_StandardItem("ЗАПИСЬ ФИНДАННЫХ",            flag_bold=True))
		self.model_data.setItem(1, 0, C20_StandardItem("Дата записи",      DATE,      flag_align_right=True))
		self.model_data.setItem(2, 0, C20_StandardItem("Сумма",            AMOUNT,    flag_align_right=True))
		self.model_data.setItem(3, 0, C20_StandardItem("Счёт физический",  FINSTRUCT, flag_align_right=True))
		self.model_data.setItem(4, 0, C20_StandardItem("Примечание",       NOTE,      flag_align_right=True))
		self.model_data.setItem(5, 0, C20_StandardItem(""))

		self.model_data.setItem(6, 0, C20_StandardItem("ФИНДЕЙСТВИЯ",                 flag_bold=True))

	def LoadModelDataFromFindata(self):
		""" Отображение данных """
		record_finstruct = C90_RecordFinstruct(self.record_findata.FinstructIdo())

		item_date        = C20_StandardItem(f"{self.record_findata.DdDmDyToString()}",                      DATE)

		item_amount      = C20_StandardItem(f"{AmountToString(self.record_findata.Amount(), False, True)}", AMOUNT)
		item_finstruct   = C20_StandardItem(f"{record_finstruct.Name()}",                                   FINSTRUCT)
		item_note        = C20_StandardItem(f"{self.record_findata.Note()}",                                NOTE)

		self.model_data.setItem(1, 1, item_date)
		self.model_data.setItem(2, 1, item_amount)
		self.model_data.setItem(3, 1, item_finstruct)
		self.model_data.setItem(4, 1, item_note)

	def LoadModelDataFromFinactions(self):
		""" Отображение финдействий """
		finactions_idos : list[str]     = self.record_findata.LinkedFinactionsIdos()

		self.model_data.removeRows(7, self.model_data.rowCount() - 7)

		if not finactions_idos:
			self.model_data.setItem(7, 0, C20_StandardItem("Записей нет"))

		else:
			for index_record, ido in enumerate(finactions_idos):
				record_finactions = C90_RecordFinactions(ido)
				self.model_data.setItem(7 + index_record, 0, C20_StandardItem(AmountToString(record_finactions.Amount(), flag_sign=True), ido, True, True))
				self.model_data.setItem(7 + index_record, 1, C20_StandardItem(record_finactions.Note(), ido))

	# Модель допустимых значений
	def SetupValuesModel(self):
		self.model_values.removeAll()

	def LoadModelValues(self):
		""" Загрузка допустимых значений """
		if   self._ido_processing == DATE     : self.LoadModelValuesDd()
		elif self._ido_processing == FINSTRUCT: self.LoadModelValuesFinstruct()

	def LoadModelValuesDd(self):
		""" Загрузка списка допустимых дат """
		dy_dm : str = self.workspace.DmDyToString()
		dds   : int = DAYS_IN_MONTH[self.workspace.Dm()]
		if self.workspace.Dm() == 2: dds += 1 if self.workspace.Dy() % 4 == 0 else 0

		for index_dd in range(1, dds): self.model_values.appendRow(C20_StandardItem(f"{index_dd:02d} {dy_dm}", f"{index_dd}"))

	def LoadModelValuesFinstruct(self):
		""" Загрузка списка счетов физических """
		dy : int = self.workspace.Dy()
		dm : int = self.workspace.Dm()

		for finstruct_name in self.finstruct.SubNamesInDyDm(dy, dm): self.model_values.appendRow(C20_StandardItem(finstruct_name))

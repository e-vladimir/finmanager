# ФОРМА ЗАПИСИ ФИНДАННЫХ: ЛОГИКА ДАННЫХ

from PySide6.QtCore          import QModelIndex, Qt

from L00_dict                import *

from L20_PySide6             import RequestValue, RequestText
from L70_form_record_findata import C70_FormRecordFindata
from L90_finstruct           import C90_RecordFinstruct


class C80_FormRecordFindata(C70_FormRecordFindata):
	""" Форма записи финданных: Логика данных """

	# Служебные действия
	def PrepareUpdateDataPartial(self):
		""" Подготовка данных для обновления данных (частичного) """
		self.workspace.IdoRecordFindata(self.record_findata.Ido().data)
		self.workspace.IdoRecordFinactions("")

	# Параметры
	def ProcessingCurrentIdo(self):
		""" Обработка выбранного параметра """
		if   self._ido_processing == AMOUNT: self.RequestAmount()
		elif self._ido_processing == NOTE  : self.RequestNote()
		else                               : self.LoadModelValues()

	def RequestAmount(self):
		""" Запрос изменения суммы """
		if not self.record_findata.CheckRecordIsManual(): return

		amount : int | None = RequestValue("Запись финданных", self.record_findata.Note(), self.record_findata.Amount(), -999999.00, 999999.00)
		if amount is None: return

		self.record_findata.Amount(amount)

		self.on_DataChanged()

	def RequestNote(self):
		""" Запрос на изменение примечания """
		note : str | None = RequestText("Запись финданных", self.record_findata.Note(), self.record_findata.Note())
		if note is None: return

		self.record_findata.Note(note)

		self.on_DataChanged()

	def ProcessingTblDataClicked(self):
		"""  """
		if self._row_processing > 6: self.on_RequestOpenRecordFinactions()
		else                       : self.on_RequestShowValues()

	# Допустимые значения
	def RequestApplyValue(self):
		""" Запрос на применение значения """
		if   self._ido_processing == DATE     : self.ApplyValueDate()
		elif self._ido_processing == FINSTRUCT: self.ApplyFinstruct()

	def ApplyValueDate(self):
		""" Применение даты записи """
		index_current : QModelIndex = self.table_values.currentIndex()
		if not index_current.isValid(): return

		index_row     : int         = index_current.row() + 1

		self.record_findata.Dd(index_row)
		self.on_DataChanged()

	def ApplyFinstruct(self):
		""" Применение финструктуры """
		index_current  : QModelIndex = self.table_values.currentIndex()
		if not index_current.isValid(): return

		dy             : int         = self.workspace.Dy()
		dm             : int         = self.workspace.Dm()

		finstruct_name : str         = index_current.data(Qt.DisplayRole)
		record_finstruct             = C90_RecordFinstruct()
		if not record_finstruct.SwitchByName(dy,dm, finstruct_name): return

		self.record_findata.FinstructIdo(record_finstruct.Ido().data)

		self.on_DataChanged()

	# Переход в другие формы
	def OpenRecordFinactions(self):
		""" Открытие записи финдействий """
		if not self._ido_processing: return

		self.workspace.IdoRecordFinactions(self._ido_processing)
		self.application.form_record_finactions.Open()

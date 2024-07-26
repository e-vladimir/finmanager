# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: ЛОГИКА ДАННЫХ

from L00_findescription        import *
from L00_form_record_finactions import *

from L20_PySide6                import RequestValue, RequestText

from L70_form_record_finactions import C70_FormRecordFinactions


class C80_FormRecordFinactions(C70_FormRecordFinactions):
	""" Форма Запись финдействий: Логика данных """

	# Служебные действия
	def PrepareUpdateDataPartial(self):
		""" Подготовка данных для обновления данных (частичного) """
		self.workspace.IdoRecordFinactions(self.record_finactions.Ido().data)
		self.workspace.IdoRecordFindata("")

	# Запись финдействий
	def SetupRecordFinactions(self):
		""" Настройка записи финдействий """
		self.record_finactions.Ido(self.workspace.IdoRecordFinactions())

	def RequestAmount(self):
		""" Запрос изменения суммы """
		amount : int | None = RequestValue("Запись финданных", self.record_finactions.Note(), self.record_finactions.Amount(), -999999, 999999)
		if amount is None: return

		self.record_finactions.Amount(amount)

		self.on_DataChanged()

	def RequestNote(self):
		""" Запрос на изменение примечания """
		note : str | None = RequestText("Запись финданных", self.record_finactions.Note(), self.record_finactions.Note())
		if note is None: return

		self.record_finactions.Note(note)

		self.on_DataChanged()

	def EditDd(self):
		""" Редактирование числа месяца """
		if not self._value_processing: return

		self.record_finactions.Dd(int(self._value_processing))

		self.on_DataChanged()

	def IncludeFinstruct(self):
		""" Добавление финструктуры """
		self.record_finactions.IncludeFinstructByName(self._value_processing)
		self.on_DataChanged()

	def ExcludeFinstruct(self):
		""" Добавление финструктуры """
		self.record_finactions.ExcludeFinstructByName(self._value_processing)
		self.on_DataChanged()

	def IncludeFindescription(self):
		""" Добавление финсостава """
		self.record_finactions.IncludeFindescriptionByName(self._value_processing)
		self.on_DataChanged()

	def ExcludeFindescription(self):
		""" Исключение финсостава """
		self.record_finactions.ExcludeFindescriptionByName(self._value_processing)
		self.on_DataChanged()

	# Таблица данных
	def ProcessingTblDataDbClick(self):
		""" Обработка двойного клика по таблице данных """
		self.SetupModelValues()

		if   self._ido_processing == DATE      : self.LoadModelValuesFromDds()

		elif self._ido_processing == AMOUNT    : self.RequestAmount()
		elif self._ido_processing == NOTE      : self.RequestNote()

		elif self._ido_processing == FINSTRUCT :
			self._name_processing = ""
			self.LoadModelValuesFromFinstruct()

		elif self._ido_processing == OBJECT_INT: self.LoadModelValuesFromFindescription()
		elif self._ido_processing == FREQUENCY : self.LoadModelValuesFromFindescription()
		elif self._ido_processing == PRIORITY  : self.LoadModelValuesFromFindescription()
		elif self._ido_processing == PROCESS   : self.LoadModelValuesFromFindescription()
		elif self._ido_processing == CATEGORY  : self.LoadModelValuesFromFindescription()
		elif self._ido_processing == OBJECT_EXT: self.LoadModelValuesFromFindescription()

	# Дерево значений
	def ProcessingTreValuesDbClick(self):
		""" Обработка двойного клика по дереву значений """
		if self._ido_processing == DATE: self.EditDd()

	def ProcessingIncludeValue(self):
		""" Обработка добавления значения """
		if   self._ido_processing == FINSTRUCT : self.IncludeFinstruct()

		elif self._ido_processing == OBJECT_INT: self.IncludeFindescription()
		elif self._ido_processing == FREQUENCY : self.IncludeFindescription()
		elif self._ido_processing == PRIORITY  : self.IncludeFindescription()
		elif self._ido_processing == PROCESS   : self.IncludeFindescription()
		elif self._ido_processing == CATEGORY  : self.IncludeFindescription()
		elif self._ido_processing == OBJECT_EXT: self.IncludeFindescription()

	def ProcessingExcludeValue(self):
		""" Обработка исключения значения """
		if   self._ido_processing == FINSTRUCT : self.ExcludeFinstruct()

		elif self._ido_processing == OBJECT_INT: self.ExcludeFindescription()
		elif self._ido_processing == FREQUENCY : self.ExcludeFindescription()
		elif self._ido_processing == PRIORITY  : self.ExcludeFindescription()
		elif self._ido_processing == PROCESS   : self.ExcludeFindescription()
		elif self._ido_processing == CATEGORY  : self.ExcludeFindescription()
		elif self._ido_processing == OBJECT_EXT: self.ExcludeFindescription()

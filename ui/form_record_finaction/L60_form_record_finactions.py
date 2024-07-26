# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: МЕХАНИКА ДАННЫХ

from PySide6.QtCore             import QModelIndex
from PySide6.QtGui              import QStandardItem

from L00_findescription         import *
from L00_form_record_finactions import *

from L10_converts               import AmountToString
from L11_datetime               import DAYS_IN_MONTH

from L20_PySide6                import C20_StandardItem, ROLE_OID
from L50_form_record_finactions import C50_FormRecordFinactions
from L90_findata                import C90_RecordFindata
from L90_finstruct              import C90_RecordFinstruct


class C60_FormRecordFinactions(C50_FormRecordFinactions):
	""" Форма Запись финдействий: Механика данных """

	# Параметры
	def Reset(self):
		""" Сброс """
		self._oid_processing   = ""
		self._name_processing  = ""
		self._value_processing = ""

	def ReadIdoProcessingFromTblData(self):
		""" Считывание OID из таблицы данных """
		self._oid_processing = ""

		index_current : QModelIndex = self.tbl_data.currentIndex()
		if not index_current.isValid(): return

		self._oid_processing = index_current.data(ROLE_OID)

	def ReadValueProcessingFromTreValues(self):
		""" Чтение значения из дерева значений """
		self._value_processing = ""

		index_current : QModelIndex = self.tre_values.currentIndex()
		if not index_current.isValid(): return

		self._value_processing = index_current.data(ROLE_OID)

	def ReadValueProcessingFromModelValues(self):
		"""  """
		self._value_processing = ""

		index_current : QModelIndex = self.model_values.index_processing
		if not index_current.isValid(): return

		self._value_processing = index_current.data(ROLE_OID)

	# Модель данных
	def SetupModelData(self):
		""" Настройка модели данных """
		self.model_data.removeAll()

		self.model_data.setHorizontalHeaderLabels(["Параметр", "Значение"])

		index_row : int = 0
		self.model_data.setItem(index_row + 0, 0, C20_StandardItem("ЗАПИСЬ ФИНДАННЫХ",              flag_bold=True, flag_align_right=True))
		self.model_data.setItem(index_row + 0, 1, C20_StandardItem(""))
		self.model_data.setItem(index_row + 1, 0, C20_StandardItem("Дата записи",                                   flag_align_right=True))
		self.model_data.setItem(index_row + 2, 0, C20_StandardItem("Сумма",                                         flag_align_right=True))
		self.model_data.setItem(index_row + 3, 0, C20_StandardItem("Счёт физический",                               flag_align_right=True))
		self.model_data.setItem(index_row + 4, 0, C20_StandardItem("Примечание",                                    flag_align_right=True))
		self.model_data.setItem(index_row + 5, 0, C20_StandardItem(""))

		index_row : int = 6
		self.model_data.setItem(index_row + 0, 0, C20_StandardItem("ЗАПИСЬ ФИНДЕЙСТВИЙ",            flag_bold=True, flag_align_right=True))
		self.model_data.setItem(index_row + 0, 1, C20_StandardItem(""))
		self.model_data.setItem(index_row + 1, 0, C20_StandardItem("Дата записи",       DATE,                       flag_align_right=True))
		self.model_data.setItem(index_row + 2, 0, C20_StandardItem("Сумма",             AMOUNT,                     flag_align_right=True))
		self.model_data.setItem(index_row + 3, 0, C20_StandardItem("Счёта виртуальные", FINSTRUCT,                  flag_align_right=True))
		self.model_data.setItem(index_row + 4, 0, C20_StandardItem("Примечание",        NOTE,                       flag_align_right=True))
		self.model_data.setItem(index_row + 5, 0, C20_StandardItem(""))

		index_row : int = 12
		self.model_data.setItem(index_row + 0, 0, C20_StandardItem("КРИТЕРИИ УЧЁТА",                flag_bold=True, flag_align_right=True))
		self.model_data.setItem(index_row + 0, 1, C20_StandardItem(""))
		self.model_data.setItem(index_row + 1, 0, C20_StandardItem(OBJECT_INT,          OBJECT_INT,                 flag_align_right=True))
		self.model_data.setItem(index_row + 2, 0, C20_StandardItem(FREQUENCY,           FREQUENCY,                  flag_align_right=True))
		self.model_data.setItem(index_row + 3, 0, C20_StandardItem(PRIORITY,            PRIORITY,                   flag_align_right=True))
		self.model_data.setItem(index_row + 4, 0, C20_StandardItem(PROCESS,             PROCESS,                    flag_align_right=True))
		self.model_data.setItem(index_row + 5, 0, C20_StandardItem(CATEGORY,            CATEGORY,                   flag_align_right=True))
		self.model_data.setItem(index_row + 6, 0, C20_StandardItem(OBJECT_EXT,          OBJECT_EXT,                 flag_align_right=True))

	def LoadModelDataFromRecordFinactions(self):
		""" Загрузка модели данных из записи финдействий """
		finstruct_names : list[str] = self.finstruct.IdosToNames(self.record_finactions.FinstructIdos())
		categories      : list[str] = self.findescription.IdosToNames(self.record_finactions.FindescriptionIdos(), CATEGORY)
		frequencies     : list[str] = self.findescription.IdosToNames(self.record_finactions.FindescriptionIdos(), FREQUENCY)
		objects_int     : list[str] = self.findescription.IdosToNames(self.record_finactions.FindescriptionIdos(), OBJECT_INT)
		objects_ext     : list[str] = self.findescription.IdosToNames(self.record_finactions.FindescriptionIdos(), OBJECT_EXT)
		priorities      : list[str] = self.findescription.IdosToNames(self.record_finactions.FindescriptionIdos(), PRIORITY)
		processes       : list[str] = self.findescription.IdosToNames(self.record_finactions.FindescriptionIdos(), PROCESS)

		index_row : int = 6
		self.model_data.setItem(index_row + 1, 1, C20_StandardItem(self.record_finactions.DdDmDyToString(),         DATE))
		self.model_data.setItem(index_row + 2, 1, C20_StandardItem(AmountToString(self.record_finactions.Amount()), AMOUNT))
		self.model_data.setItem(index_row + 3, 1, C20_StandardItem('\n'.join(finstruct_names),                      FINSTRUCT))
		self.model_data.setItem(index_row + 4, 1, C20_StandardItem(self.record_finactions.Note(),                   NOTE))

		index_row : int = 12
		self.model_data.setItem(index_row + 1, 1, C20_StandardItem('\n'.join(objects_int),                          OBJECT_INT))
		self.model_data.setItem(index_row + 2, 1, C20_StandardItem('\n'.join(frequencies),                          FREQUENCY))
		self.model_data.setItem(index_row + 3, 1, C20_StandardItem('\n'.join(priorities),                           PRIORITY))
		self.model_data.setItem(index_row + 4, 1, C20_StandardItem('\n'.join(processes),                            PROCESS))
		self.model_data.setItem(index_row + 5, 1, C20_StandardItem('\n'.join(categories),                           CATEGORY))
		self.model_data.setItem(index_row + 6, 1, C20_StandardItem('\n'.join(objects_ext),                          OBJECT_EXT))

	def LoadModelDataFromRecordFindata(self):
		""" Загрузка модели данных из записи финдействий """
		record_findata              = C90_RecordFindata(self.record_finactions.FindataIdo())
		record_finstruct            = C90_RecordFinstruct(record_findata.FinstructIdo())

		index_row       : int       = 0
		self.model_data.setItem(index_row + 1, 1, C20_StandardItem(record_findata.DdDmDyToString()))
		self.model_data.setItem(index_row + 2, 1, C20_StandardItem(AmountToString(record_findata.Amount())))
		self.model_data.setItem(index_row + 3, 1, C20_StandardItem(record_finstruct.Name()))
		self.model_data.setItem(index_row + 4, 1, C20_StandardItem(record_findata.Note()))

	# Модель значений
	def SetupModelValues(self):
		""" Настройка модели значений """
		self.model_values.removeAll()
		self.model_values.setHorizontalHeaderLabels(["Значение"])

	def LoadModelValuesFromDds(self):
		""" Загрузка списка допустимых дат """
		dy_dm : str = self.workspace.DmDyToString()
		dds   : int = DAYS_IN_MONTH[self.workspace.Dm()]
		if self.workspace.Dm() == 2: dds += 1 if self.workspace.Dy() % 4 == 0 else 0

		for index_dd in range(1, dds): self.model_values.appendRow(C20_StandardItem(f"{index_dd:02d} {dy_dm}", f"{index_dd}"))

	def LoadModelValuesFromFinstruct(self):
		""" Загрузка списка финструктуры """
		dy : int = self.workspace.Dy()
		dm : int = self.workspace.Dm()

		item_root : QStandardItem | None = self.model_values.itemByData(self._name_processing)
		if item_root is None: item_root = self.model_values.invisibleRootItem()

		for self._name_processing in self.finstruct.SubNamesInDyDm(dy, dm, self._name_processing):
			item_root.appendRow(C20_StandardItem(self._name_processing, self._name_processing))

			self.LoadModelValuesFromFinstruct()

	def LoadModelValuesFromFindescription(self):
		""" Загрузка списка финсостава """
		for findescription_name in self.findescription.Names(self._oid_processing):
			self.model_values.appendRow(C20_StandardItem(findescription_name, findescription_name))

# ФОРМА ФИНДАННЫЕ: ЛОГИКА ДАННЫХ

from PySide6.QtCore   import QModelIndex, Qt
from PySide6.QtGui    import QStandardItem
from PySide6.QtWidgets import QProgressDialog

from G10_math_linear  import CalcBetween

from L00_containers   import CONTAINER_LOCAL

from L10_converts     import AmountToString
from L20_PySide6      import RequestValue, RequestText, RequestConfirm
from L70_form_findata import C70_FormFindata
from L90_finactions   import C90_RecordFinactions
from L90_findata      import C90_RecordFindata


class C80_FormFindata(C70_FormFindata):
	""" Форма Финданные: Логика данных """

	# Служебные
	def ProcessingUpdateDataPartial(self):
		""" Обработка частичного обновления данных """
		if self.workspace.OidRecordFinactions():
			record_finactions = C90_RecordFinactions(self.workspace.OidRecordFinactions())
			record_findata    = C90_RecordFindata(record_finactions.FindataOid())

			self._oid_processing_findata = record_finactions.FindataOid()
			self._dd_processing          = record_finactions.Dd()

			self.CleanRecordFindata()

			self.LoadRecordFindata()

			for self._oid_processing_finactions in record_findata.LinkedFinactionsOids(): self.LoadRecordFinactions()

		if self.workspace.OidRecordFindata():
			record_findata    = C90_RecordFindata(self.workspace.OidRecordFindata())
			self._dd_processing          = record_findata.Dd()

			self.ReloadDd()

	# Финданные
	def LoadDataByDds(self):
		""" Загрузка данных дней """
		dy  : int       = self.workspace.Dy()
		dm  : int       = self.workspace.Dm()

		dds : list[str] = self.findata.Dds(dy, dm)

		dialog_progress = QProgressDialog("Загрузка финданных", "Отмена", 0, len(dds))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.setMinimumHeight(120)
		dialog_progress.setWindowTitle("Загрузка данных")

		for index_oid, self._dd_processing in enumerate(dds):
			dialog_progress.setLabelText(f"{self._dd_processing:02d} {self.workspace.DmDyToString()}")
			dialog_progress.setValue(index_oid)
			dialog_progress.forceShow()
			self.application.processEvents()

			for self._oid_processing_findata in self.findata.OidsInDyDmDd(dy, dm, self._dd_processing):
				self.LoadRecordFindata()
				self.LoadRecordFinactions()

	def ReloadDd(self):
		""" Перезагрузка дня """
		self.CleanDd()

		dy : int       = self.workspace.Dy()
		dm : int       = self.workspace.Dm()
		dd : int       = self._dd_processing

		for self._oid_processing_findata in self.findata.OidsInDyDmDd(dy, dm, dd): self.ReloadRecordFindata()

	# Запись финданных
	def ReloadRecordFindata(self):
		""" Перезагрузка записи финданных """
		self.LoadRecordFindata()

		record_findata = C90_RecordFindata(self._oid_processing_findata)
		for self._oid_processing_finactions in record_findata.LinkedFinactionsOids(): self.LoadRecordFinactions()

	def CreateRecordFindata(self):
		""" Запрос на создание записи финданных """
		dd : int = CalcBetween(1, self._dd_processing, 31)

		amount : float | None = RequestValue("Создание записи финданных", f"Новая запись финданных от {dd:02d} {self.workspace.DmDyToString()}\n\nСумма записи финданных", 0.00, -9999999.99, 9999999.99)
		if amount is None: return

		record_findata = C90_RecordFindata()
		record_findata.GenerateOid()
		record_findata.RegisterObject(CONTAINER_LOCAL)

		record_findata.Dd(dd)
		record_findata.Dm(self.workspace.Dm())
		record_findata.Dy(self.workspace.Dy())
		record_findata.Amount(amount)
		record_findata.FinstructOid("")
		record_findata.Note("")

		self.workspace.OidRecordFindata(record_findata.Oid().text)

		self.on_RecordFindataCreated()

	def OpenRecordFindata(self):
		""" Открытие записи финданных """
		self.workspace.OidRecordFindata(self._oid_processing_findata)

		self.application.form_record_findata.Open()

	def DeleteRecordFindata(self):
		""" Удаление записи финданных """
		if not self._oid_processing_findata: return

		record_findata = C90_RecordFindata(self._oid_processing_findata)

		if not RequestConfirm("Удаление записи финданных", f"Удаление записи финданных {AmountToString(record_findata.Amount())} от {record_findata.DdDmDyToString()}\n\n{record_findata.Note()}"): return

		for oid_finactions in record_findata.LinkedFinactionsOids():
			record_finactions = C90_RecordFinactions(oid_finactions)
			record_finactions.DeleteObject(CONTAINER_LOCAL)

		record_findata.DeleteObject(CONTAINER_LOCAL)

		self.workspace.OidRecordFindata(self._oid_processing_findata)

		self.on_RecordFindataDeleted()

	def EditNoteRecordFindata(self):
		""" Редактирование примечания записи финданных """
		if not self._oid_processing_findata: return

		record_findata    = C90_RecordFindata(self._oid_processing_findata)

		note : str | None = RequestText("Редактирование записи финданных", f"{AmountToString(record_findata.Amount())} от {record_findata.DdDmDyToString()}\n{record_findata.Note()}", record_findata.Note())
		if note is None: return

		record_findata.Note(note)

		self.on_RecordFindataChanged()

	# Запись финдействий
	def CreateRecordsFinactions(self):
		""" Пакетное преобразование записей финданных """
		dialog_progress = QProgressDialog("Создание финдействий", "Отмена", 0, len(self._oids_processing_findata))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.setMinimumHeight(120)
		dialog_progress.setWindowTitle("Обработка данных")

		for index_oid, self._oid_processing_findata in enumerate(self._oids_processing_findata):
			dialog_progress.setValue(index_oid)
			dialog_progress.forceShow()
			self.application.processEvents()

			self.CreateRecordFinactions()

	def CreateRecordFinactions(self):
		""" Создание записи финдействий """
		if not self._oid_processing_findata: return

		record_findata = C90_RecordFindata(self._oid_processing_findata)
		remains : int  = record_findata.CalcAmountDeviationByLinks()

		if self._flag_processing_skip and record_findata.LinkedFinactionsOids(): return

		if self._flag_quick:
			amount : int        = remains

		else               :
			amount : int | None = RequestValue("Новая запись финдействий", f"{AmountToString(record_findata.Amount())} от {record_findata.DdDmDyToString()}\n{record_findata.Note()}", remains, -9999999, 999999)
			if amount is None: return

		dy      : int  = self.workspace.Dy()
		dm      : int  = self.workspace.Dm()

		record_finactions = C90_RecordFinactions()
		record_finactions.GenerateOid()
		record_finactions.RegisterObject(CONTAINER_LOCAL)

		record_finactions.FindataOid(record_findata.Oid().text)
		record_finactions.Dy(record_findata.Dy())
		record_finactions.Dm(record_findata.Dm())
		record_finactions.Dd(record_findata.Dd())
		record_finactions.Amount(amount)
		record_finactions.Note(record_findata.Note())
		record_finactions.FindescriptionOids([])
		record_finactions.FinstructOids([self.finstruct.GetPriorityRecord(dy, dm)])

		record_finactions.ApplyRulesDetectFindescription()

		self.workspace.OidRecordFinactions(record_finactions.Oid().text)

		if self._flag_quick: return

		self.application.form_record_finactions.Open()

	def OpenRecordFinactions(self):
		""" Открытие записи финдействий """
		self.workspace.OidRecordFinactions(self._oid_processing_finactions)

		self.application.form_record_finactions.Open()

	def DeleteRecordFinactions(self):
		""" Удаление записи финдействий """
		if not self._oid_processing_finactions: return

		record_finactions = C90_RecordFinactions(self._oid_processing_finactions)

		if not RequestConfirm("Удаление записи финдействий", f"Удаление записи финдействий {AmountToString(record_finactions.Amount())} от {record_finactions.DdDmDyToString()}\n\n{record_finactions.Note()}"): return

		record_finactions.DeleteObject(CONTAINER_LOCAL)

		self.workspace.OidRecordFindata(self._oid_processing_findata)

		self.on_UpdateDataPartial()

	def EditNoteRecordFinactions(self):
		""" Редактирование примечания записи финдействий """
		if not self._oid_processing_finactions: return

		record_finactions = C90_RecordFinactions(self._oid_processing_finactions)

		note : str | None = RequestText("Редактирование записи финдействий", f"{AmountToString(record_finactions.Amount())} от {record_finactions.DdDmDyToString()}\n{record_finactions.Note()}", record_finactions.Note())
		if note is None: return

		record_finactions.Note(note)

		self.on_RecordFinactionsChanged()

	# Выделение
	def ProcessingSelectionByText(self):
		""" Обработка выделение по текстовому фрагменту """
		record_findata               = C90_RecordFindata(self._oid_processing_findata)
		record_finactions            = C90_RecordFinactions(self._oid_processing_finactions)

		note_finactions : str        = record_finactions.Note()
		note_findata    : str        = record_findata.Note()

		text_src        : str        = note_findata if not note_finactions else note_finactions

		if self._oid_processing_findata: text_src = C90_RecordFindata(self._oid_processing_findata).Note()

		text_search     : str | None = RequestText("Расширение выборки", "Текстовый фрагмент для расширения выборки", text_src)
		if text_search is None: return

		text_search                  = text_search.lower()

		for index_record in self.model_data.indexes():
			index_parent   : QModelIndex   = index_record.parent()
			index_row      : int           = index_record.row()

			index_note     : QModelIndex   = index_parent.child(index_row, 8)

			data_note      : str           = index_note.data(Qt.DisplayRole)
			if data_note       is None     : continue

			data_note                      = data_note.lower()
			if text_search not in data_note: continue

			item_data      : QStandardItem = self.model_data.itemFromIndex(index_record)
			item_data.setCheckState(Qt.Unchecked if self._flag_processing_dec else Qt.Checked)

	def ProcessingSelectionByFindescription(self):
		""" Обработка выделения по финсоставу """
		text_search     : str | None = RequestText("Расширение выборки", "Текстовый фрагмент для расширения выборки по финсоставу")
		if text_search is None: return

		text_search                  = text_search.lower()

		for index_record in self.model_data.indexes():
			index_parent   : QModelIndex   = index_record.parent()
			index_row      : int           = index_record.row()

			text_data      : str           = ""

			for index_col in range(2, 8):
				index_data : QModelIndex | None = index_parent.child(index_row, index_col)
				if     index_data is None  : continue
				if not index_data.isValid(): continue

				text_data += index_data.data(Qt.DisplayRole)

			text_data = text_data.lower()

			if text_search not in text_data: continue

			item_data      : QStandardItem = self.model_data.itemFromIndex(index_record)
			item_data.setCheckState(Qt.Unchecked if self._flag_processing_dec else Qt.Checked)

	def CleanSelection(self):
		""" Сброс выделения """
		for index_data in self.model_data.indexes():
			item_data    : QStandardItem = self.model_data.itemFromIndex(index_data)

			index_parent : QModelIndex   = index_data.parent()
			if not index_parent.isValid(): continue

			item_data.setCheckState(Qt.Unchecked)

	# Утилиты
	def ReplaceText(self):
		"""  """
		record_findata               = C90_RecordFindata(self._oid_processing_findata)
		record_finactions            = C90_RecordFinactions(self._oid_processing_finactions)

		note_finactions : str        = record_finactions.Note()
		note_findata    : str        = record_findata.Note()

		text_src        : str        = note_findata if not note_finactions else note_finactions

		if self._oid_processing_findata: text_src = C90_RecordFindata(self._oid_processing_findata).Note()

		text_search     : str | None = RequestText("Поиск и замена текстового фрагмента", "Поиск", text_src)
		if text_search is None : return

		text_replace    : str | None = RequestText("Поиск и замена текстового фрагмента", f"Замена {text_search} на...", text_search)
		if text_replace is None: return

		dy              : int        = self.workspace.Dy()
		dm              : int        = self.workspace.Dm()

		oids_findata    : list[str]  = self.findata.OidsInDyDmDd(dy, dm)
		oids_finactions : list[str]  = self.finactions.OidsInDyDmDd(dy, dm)

		counter         : int        = 0

		dialog_progress = QProgressDialog("Поиск и замена текстового фрагмента", "Отмена", 0, len(oids_findata) + len(oids_finactions))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.setMinimumHeight(120)
		dialog_progress.setWindowTitle("Обработка данных")

		for self._oid_processing_findata in oids_findata:
			counter += 1

			dialog_progress.setValue(counter)
			dialog_progress.forceShow()
			self.application.processEvents()

			record_findata = C90_RecordFindata(self._oid_processing_findata)
			note_src : str = record_findata.Note()

			if text_search not in note_src: continue

			record_findata.Note(note_src.replace(text_search, text_replace))

			self.UpdateRecordFindata()

		for self._oid_processing_finactions in oids_finactions:
			counter += 1

			dialog_progress.setValue(counter)
			dialog_progress.forceShow()
			self.application.processEvents()

			record_finactions = C90_RecordFinactions(self._oid_processing_finactions)
			note_src : str = record_finactions.Note()

			if text_search not in note_src: continue

			record_finactions.Note(note_src.replace(text_search, text_replace))

			self.UpdateRecordFinactions()

	# Правила обработки данных
	def ApplyRulesReplaceText(self):
		""" Применение правил замены текстовых фрагментов """
		if self._oids_processing_findata:
			dialog_progress = QProgressDialog("Применение правил замены текстовых фрагментов", "Отмена", 0, len(self._oids_processing_findata))
			dialog_progress.setMinimumWidth(480)
			dialog_progress.setMinimumHeight(120)
			dialog_progress.setWindowTitle("Обработка данных")

			for index_oid, self._oid_processing_findata in enumerate(self._oids_processing_findata):
				dialog_progress.setValue(index_oid + 1)
				dialog_progress.forceShow()
				self.application.processEvents()

				record_findata = C90_RecordFindata(self._oid_processing_findata)
				record_findata.ApplyRulesReplaceText()

				self.on_RecordFindataChanged()

		elif self._oid_processing_findata:
			record_findata = C90_RecordFindata(self._oid_processing_findata)
			record_findata.ApplyRulesReplaceText()

			self.on_RecordFindataChanged()

	def ApplyRulesReplaceTextForAll(self):
		""" Применение правил замен текстовых фрагментов для всех записей финданных """
		dy : int        = self.workspace.Dy()
		dm : int        = self.workspace.Dm()

		dialog_progress = QProgressDialog("Применение правил замены текстовых фрагментов", "Отмена", 0, len(self._oids_processing_findata))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.setMinimumHeight(120)
		dialog_progress.setWindowTitle("Обработка данных")

		for index_oid, self._oid_processing_findata in enumerate(self.findata.OidsInDyDmDd(dy, dm)):
			dialog_progress.setValue(index_oid + 1)
			dialog_progress.forceShow()
			self.application.processEvents()

			record_findata = C90_RecordFindata(self._oid_processing_findata)
			record_findata.ApplyRulesReplaceText()

			self.on_RecordFindataChanged()

	def ApplyRulesDetectFindescriptionByText(self):
		""" Применение правил определения финсостава """
		if self._oids_processing_finactions:
			dialog_progress = QProgressDialog("Применение правил замены текстовых фрагментов", "Отмена", 0, len(self._oids_processing_findata))
			dialog_progress.setMinimumWidth(480)
			dialog_progress.setMinimumHeight(120)
			dialog_progress.setWindowTitle("Обработка данных")

			for index_oid, self._oid_processing_finactions in enumerate(self._oids_processing_finactions):
				dialog_progress.setValue(index_oid + 1)
				dialog_progress.forceShow()
				self.application.processEvents()

				record_finactions = C90_RecordFinactions(self._oid_processing_finactions)
				record_finactions.ApplyRulesDetectFindescription()

				self.on_RecordFinactionsChanged()

		elif self._oid_processing_finactions:
			record_finactions = C90_RecordFinactions(self._oid_processing_finactions)
			record_finactions.ApplyRulesDetectFindescription()

			self.on_RecordFinactionsChanged()

	def ApplyRulesDetectFindescriptionByTextForAll(self):
		""" Применение правил определения финструктуры по текстовым фрагментам для всех записей финданных """
		dy : int = self.workspace.Dy()
		dm : int = self.workspace.Dm()

		dialog_progress = QProgressDialog("Применение правил замены текстовых фрагментов", "Отмена", 0, len(self._oids_processing_findata))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.setMinimumHeight(120)
		dialog_progress.setWindowTitle("Обработка данных")

		for index_oid, self._oid_processing_finactions in enumerate(self.finactions.OidsInDyDmDd(dy, dm)):
			dialog_progress.setValue(index_oid + 1)
			dialog_progress.forceShow()
			self.application.processEvents()

			record_finactions = C90_RecordFinactions(self._oid_processing_finactions)
			record_finactions.ApplyRulesDetectFindescription()

			self.on_RecordFinactionsChanged()

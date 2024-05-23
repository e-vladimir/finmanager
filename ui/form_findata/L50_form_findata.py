# ФОРМА ФИНДАННЫЕ: МОДЕЛЬ СОБЫТИЙ

from L42_form_findata import C42_FormFindata


class C50_FormFindata(C42_FormFindata):
	""" Форма Финданные: Модель событий """

	# Меню данных
	def on_RequestShowMenuData(self): pass

	# Дерево данных
	def on_RequestProcessingDbClickOnTreeData(self): pass

	# Запись финданных
	def on_RequestCreateRecordFindata(self): pass
	def on_RequestOpenRecordFindata(self): pass
	def on_RequestDeleteRecordFindata(self): pass
	def on_RequestEditNoteRecordFindata(self): pass

	def on_RecordFindataCreated(self): pass
	def on_RecordFindataChanged(self): pass
	def on_RecordFindataDeleted(self): pass

	# Запись финдействий
	def on_RequestCreateRecordFinactions(self): pass
	def on_RequestQuickCreateRecordFinactions(self): pass
	def on_RequestQuickCreateRecordsFinactions(self): pass
	def on_RequestOpenRecordFinactions(self): pass
	def on_RequestDeleteRecordFinactions(self): pass
	def on_RequestEditNoteRecordFinactions(self): pass

	def on_RecordFinactionsChanged(self): pass

	# Управление выделением
	def on_RequestExpandSelectionByText(self): pass
	def on_RequestCollapseSelectionByText(self): pass
	def on_RequestExpandSelectionByFindescription(self): pass
	def on_RequestCollapseSelectionByFindescription(self): pass
	def on_RequestCleanSelection(self): pass

	# Правила обработки данных
	def on_RequestApplyRulesReplaceText(self): pass
	def on_RequestApplyRulesReplaceTextForAll(self): pass
	def on_RequestApplyRulesDetectFindescriptionByText(self): pass
	def on_RequestApplyRulesDetectFindescriptionByTextForAll(self): pass

	# Утилиты
	def on_RequestReplaceText(self): pass

	# Обмен данными
	def on_RequestImport(self): pass
	def on_RequestExport(self): pass

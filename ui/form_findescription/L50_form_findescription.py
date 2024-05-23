# ФОРМА ФИНСОСТАВА: МОДЕЛЬ СОБЫТИЙ

from L42_form_findescription import C42_FormFindescription


class C50_FormFindescription(C42_FormFindescription):
	""" Форма Финсостав: Модель событий """

	def on_RequestMenuFindescription(self): pass

	def on_RequestCreateRecord(self): pass
	def on_RequestCreateSubRecord(self): pass
	def on_RequestDeleteRecord(self): pass
	def on_RequestRenameRecord(self): pass

	def on_RequestPasteRecord(self): pass
	def on_RequestSubPasteRecord(self): pass
	def on_RequestMemoryRecord(self): pass
	def on_RequestMoveUp(self): pass

	def on_RecordCreated(self): pass
	def on_SubRecordCreated(self): pass
	def on_RecordDeleted(self): pass
	def on_RecordRenamed(self): pass
	def on_RecordMoved(self): pass

	def on_CategorySwitched(self): pass

	def on_ItemChanged(self): pass
	def on_ItemCheckStateChanged(self): pass

	def on_FindescriptionLoaded(self): pass

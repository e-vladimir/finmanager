# ФОРМА ФИНСТРУКТУРЫ: МОДЕЛЬ СОБЫТИЙ

from L42_form_finstruct import C42_FormFinstruct


class C50_FormFinstruct(C42_FormFinstruct):
	""" Форма Финструктуры: Модель событий """

	def on_RequestMenuFinstruct(self): pass

	def on_RequestCreateRecord(self): pass
	def on_RequestCreateSubRecord(self): pass
	def on_RequestRenameRecord(self): pass
	def on_RequestDeleteRecord(self): pass
	def on_RequestSetPriorityRecord(self): pass

	def on_RecordCreated(self): pass
	def on_SubRecordCreated(self): pass
	def on_RecordDeleted(self): pass
	def on_RecordRenamed(self): pass
	def on_RecordMoved(self): pass

	def on_FinstructLoaded(self): pass

	def on_RequestPasteRecord(self): pass
	def on_RequestSubPasteRecord(self): pass
	def on_RequestMemoryRecord(self): pass
	def on_RequestMoveUp(self): pass

	def on_RequestCopyRecordToNextDm(self): pass
	def on_RequestCopyRecordToPrevDm(self): pass

	def on_RequestEditRecord(self): pass

	def on_RequestEditRemainInitial(self): pass

	def on_RecordChanged(self): pass

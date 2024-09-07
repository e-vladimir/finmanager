# ФОРМА ФИНСТРУКТУРА: МОДЕЛЬ СОБЫТИЙ

from L42_form_finstruct import C42_FormFinstruct


class C50_FormFinstruct(C42_FormFinstruct):
	""" Форма Финструктура: Модель событий """

	# Меню финструктуры
	def on_RequestMenuFinstruct(self): pass

	# Дерево финструктуры
	def on_RequestProcessingTreeDataDbClick(self): pass

	# Финструктура
	def on_RequestCopyToPrevDmFinstruct(self): pass
	def on_RequestCopyToNextDmFinstruct(self): pass

	# Группа финструктуры
	def on_RequestCopyToPrevDmGroupFinstructRecords(self): pass
	def on_RequestCopyToNextDmGroupFinstructRecords(self): pass

	# Запись финструктуры
	def on_RequestCreateFinstructRecord(self): pass
	def on_RequestCreateFinstructRecordInGroup(self): pass
	def on_RequestRenameFinstructRecord(self): pass
	def on_RequestDeleteFinstructRecord(self): pass
	def on_RequestRegroupFinstructRecord(self): pass
	def on_RequestRenameGroupFinstruct(self): pass

	def on_RequestEditBalanceStartFinstructRecord(self): pass

	def on_RequestCopyToPrevDmFinstructRecord(self): pass
	def on_RequestCopyToNextDmFinstructRecord(self): pass

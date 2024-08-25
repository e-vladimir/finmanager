# ФОРМА ФИНСТРУКТУРА: МОДЕЛЬ СОБЫТИЙ

from L42_form_finstruct import C42_FormFinstruct


class C50_FormFinstruct(C42_FormFinstruct):
	""" Форма Финструктура: Модель событий """

	# Меню финструктуры
	def on_RequestMenuFinstruct(self): pass

	# Дерево финструктуры
	def on_RequestProcessingTreeDataDbClick(self): pass

	# Запись финструктуры
	def on_RequestCreateFinstructRecord(self): pass
	def on_RequestCreateFinstructRecordInGroup(self): pass
	def on_RequestRenameFinstructRecord(self): pass
	def on_RequestDeleteFinstructRecord(self): pass
	def on_RequestRegroupFinstructRecord(self): pass
	def on_RequestRenameGroupFinstruct(self): pass

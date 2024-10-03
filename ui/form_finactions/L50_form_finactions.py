# ФОРМА ФИНДЕЙСТВИЯ: МОДЕЛЬ СОБЫТИЙ

from L42_form_finactions import C42_FormFinactions


class C50_FormFinactions(C42_FormFinactions):
	""" Форма Финдействия: Модель событий """

	# Меню финдействий
	def on_RequestMenuFinactions(self): pass

	# Финдействия
	def on_RequestCreateFinactionsRecord(self): pass
	def on_RequestImportFinactions(self): pass
	def on_RequestExportFinactions(self): pass

	# Запись финдействий
	def on_RequestOpenFinactionsRecord(self): pass
	def on_RequestDeleteFinactionsRecord(self): pass
	def on_RequestSplitFinactionsRecord(self): pass
	def on_RequestEditNoteFinactionsRecord(self): pass

	# Дерево данных
	def on_RequestProcessingTreeDataDbClick(self): pass

	# Цветовая метка
	def on_RequestSetColorBlack(self): pass
	def on_RequestSetColorGray(self): pass
	def on_RequestSetColorBlue(self): pass
	def on_RequestSetColorGreen(self): pass
	def on_RequestSetColorRed(self): pass

	# Пакетный режим
	def on_RequestResetPack(self): pass
	def on_RequestExpandPackByText(self): pass
	def on_RequestReducePackByText(self): pass

	# Правила обработки данных
	def on_RequestApplyRulesToSelections(self): pass
	def on_RequestApplyRulesToAll(self): pass

	# Утилиты поиска и замены
	def on_RequestReplaceText(self): pass

	# Сброс данных
	def on_RequestResetLabels(self): pass
	def on_RequestResetFinactionsByDm(self): pass
	def on_RequestResetFinactionsByFinstruct(self): pass

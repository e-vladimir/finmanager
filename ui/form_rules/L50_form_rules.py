# ФОРМА ПРАВИЛ ОБРАБОТКИ: МОДЕЛЬ СОБЫТИЙ

from L42_form_rules import C42_FormRules


class C50_FormRules(C42_FormRules):
	""" Форма правил обработки: Модель событий """

	# Тип правил
	def on_TypeRulesChanged(self): pass

	# Меню правил
	def on_RequestMenu(self): pass

	# Правила замены текстового фрагмента
	def on_RequestCreateRecordReplaceText(self): pass
	def on_RequestEditInputForReplaceText(self): pass
	def on_RequestEditOutputForReplaceText(self): pass
	def on_RequestDeleteRecordReplaceText(self): pass

	def on_RecordReplaceTextCreated(self): pass
	def on_RecordReplaceTextChanged(self): pass
	def on_RecordReplaceTextDeleted(self): pass

	# Правила определения финсостава по текстовому фрагменту
	def on_RequestEditInputForDetectFindescription(self): pass
	def on_RequestDeleteRecordDetectFindescription(self): pass
	def on_RequestWrapSubRecordDetectFindescription(self): pass

	def on_RecordDetectFindescriptionChanged(self): pass
	def on_RecordDetectFindescriptionDeleted(self): pass

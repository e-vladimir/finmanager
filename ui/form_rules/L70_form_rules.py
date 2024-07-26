# ФОРМА ПРАВИЛ ОБРАБОТКИ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui        import QCursor

from L00_rules_types      import *

from L60_form_rules       import C60_FormRules
from L90_findescription import C90_RecordFindescription
from L90_processing_rules import C90_RecordProcessingRules


class C70_FormRules(C60_FormRules):
	""" Форма правил обработки: Механика управления """

	# Список типов правил
	def ShowRulesTypes(self):
		""" Отображение типов правил """
		self.cbbox_rules_types.clear()
		self.cbbox_rules_types.addItem(RULE_REPLACE_TEXT)
		self.cbbox_rules_types.addItem(RULE_DETECT_FINDESCRIPTION_BY_TEXT)

	# Дерево данных
	def AdjustTreeDataSizes(self):
		""" Настройка размера дерева данных """
		self.tree_data.resizeColumnToContents(0)

		col_size : int = self.tree_data.columnWidth(0)
		col_size       = max(col_size, 200)

		self.tree_data.setColumnWidth(0, col_size)

	def AdjustTreeExpand(self):
		""" Настройка раскрытия """
		self.tree_data.expandAll()

	# Меню правил
	def ShowMenu(self):
		""" Отображение меню """
		if   self._type_processing == RULE_REPLACE_TEXT                 : self.menu_replace_text.exec_(QCursor.pos())
		elif self._type_processing == RULE_DETECT_FINDESCRIPTION_BY_TEXT: self.menu_detect_findescription.exec_(QCursor.pos())

	def AdjustMenuText(self):
		""" Настройка элементов меню """
		self.menu_replace_text_record_header.setText("Запись правил замены текстового фрагмента")
		self.menu_detect_findescription_record_header.setText("Запись правил определения финсостава")

		if self._oid_processing:
			record_rule = C90_RecordProcessingRules(self._oid_processing)

			self.menu_replace_text_record_header.setText(record_rule.OptionsOutputAsString())

		if self._name_processing:
			self.menu_detect_findescription_record_header.setText(self._name_processing)

	def AdjustMenuEnable(self):
		""" Настройка доступности меню """
		flag_selected_record         : bool = bool(self._oid_processing)
		flag_selected_findescription : bool = bool(self._name_processing)

		self.menu_replace_text_record_delete.setEnabled(flag_selected_record)
		self.menu_replace_text_record_edit_input.setEnabled(flag_selected_record)
		self.menu_replace_text_record_edit_output.setEnabled(flag_selected_record)

		self.menu_detect_findescription_record_edit_input.setEnabled(flag_selected_findescription)
		self.menu_detect_findescription_record_delete.setEnabled(flag_selected_record)

		self.menu_detect_findescription_record_wrap.setEnabled(False)

		if not self._name_processing                                    : return

		record_findescription               = C90_RecordFindescription()
		if not record_findescription.SwitchByName(self._name_processing): return
		flag_suboids                 : bool = bool(record_findescription.SubIdos(True))

		self.menu_detect_findescription_record_wrap.setEnabled(flag_suboids)

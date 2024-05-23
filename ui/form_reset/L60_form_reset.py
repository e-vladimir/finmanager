# ФОРМА СБРОС ДАННЫХ: МЕХАНИКА ДАННЫХ

from PySide6.QtCore     import Qt
from PySide6.QtGui      import QStandardItem

from L00_containers     import CONTAINER_LOCAL
from L00_rules_types    import *

from L20_PySide6 import C20_StandardItem, ROLE_OID
from L50_form_reset     import C50_FormReset
from L90_finactions     import C90_RecordFinactions
from L90_findata        import C90_RecordFindata
from L90_findescription import C90_RecordFindescription
from L90_finstate       import C90_RecordFinstate
from L90_finstruct      import C90_RecordFinstruct


class C60_FormReset(C50_FormReset):
	""" Форма Сброс данных: Механика данных """

	# Параметры
	def ReadFlagAllPeriods(self):
		""" Чтение параметра Удалить на все периоды """
		self._flag_all_periods = self.chb_all_periods.isChecked()

	def ReadFlagObjects(self):
		""" Чтение состояние отметок сброса """
		item_finstruct                                 = self.model_objects.itemByData("finstruct", ROLE_OID)
		item_finactions                                = self.model_objects.itemByData("finactions", ROLE_OID)
		item_finstate_in_finactions                    = self.model_objects.itemByData("finactions_findescription", ROLE_OID)
		item_findescription                            = self.model_objects.itemByData("findescription", ROLE_OID)
		item_finstate                                  = self.model_objects.itemByData("finstate", ROLE_OID)
		item_findata                                   = self.model_objects.itemByData("findata", ROLE_OID)
		item_rule_replace_text                         = self.model_objects.itemByData("rule_replace_text", ROLE_OID)
		item_rule_detect_findescription_by_text        = self.model_objects.itemByData("rule_detect_findescription_by_text", ROLE_OID)

		self._flag_finstruct                           = item_finstruct.checkState()                          == Qt.Checked
		self._flag_finaction                           = item_finactions.checkState()                         == Qt.Checked
		self._flag_findescription_in_finactions        = item_finstate_in_finactions.checkState()             == Qt.Checked
		self._flag_findescription                      = item_findescription.checkState()                     == Qt.Checked
		self._flag_finstate                            = item_finstate.checkState()                           == Qt.Checked
		self._flag_findata                             = item_findata.checkState()                            == Qt.Checked
		self._flag_rules_replace_text                  = item_rule_replace_text.checkState()                  == Qt.Checked
		self._flag_rules_detect_findescription_by_text = item_rule_detect_findescription_by_text.checkState() == Qt.Checked

	def ReadOidsFinstruct(self):
		""" Сбор OID финструктуры """
		self._oids_finstruct.clear()

		if not self._flag_finstruct: return

		if self._flag_all_periods:
			self._oids_finstruct = C90_RecordFinstruct.Oids(CONTAINER_LOCAL).items

		else:
			dy : int = self.workspace.Dy()
			dm : int = self.workspace.Dm()

			self._oids_finstruct = self.finstruct.OidsInDyDm(dy, dm)

	def ReadOidsFinactions(self):
		""" Сбор OID финдействий """
		self._oids_finactions.clear()

		if not (self._flag_finaction or self._flag_findata): return

		if self._flag_all_periods:
			self._oids_finactions = C90_RecordFinactions.Oids(CONTAINER_LOCAL).items

		else:
			dy : int = self.workspace.Dy()
			dm : int = self.workspace.Dm()

			self._oids_finactions = self.finactions.OidsInDyDmDd(dy, dm)

	def ReadOidsFindescription(self):
		""" Сбор OID финсостава """
		self._oids_findescription.clear()

		if not self._flag_findescription: return

		self._oids_findescription = C90_RecordFindescription.Oids(CONTAINER_LOCAL).items

	def ReadOidsFindescriptionInFinactions(self):
		""" Сбор OID финсостава """
		self._oids_findescription_in_finactions.clear()

		if not self._flag_findescription_in_finactions: return

		self._oids_findescription_in_finactions = C90_RecordFinactions.Oids(CONTAINER_LOCAL).items

	def ReadOidsFinstate(self):
		""" Сбор OID финсостояния """
		self._oids_finstate.clear()

		if not (self._flag_finstate or self._flag_finstruct): return

		if   self._flag_finstruct:
			oids_finstruct : list[str] = self._oids_finstruct

		elif self._flag_all_periods:
			oids_finstruct : list[str] = C90_RecordFinstruct.Oids(CONTAINER_LOCAL).items

		else                       :
			dy             : int       = self.workspace.Dy()
			dm             : int       = self.workspace.Dm()

			oids_finstruct : list[str] = self.finstruct.OidsInDyDm(dy, dm)

		record_finstate = C90_RecordFinstate()

		for oid_finstruct in oids_finstruct:
			if not record_finstate.SwitchByFinstructOid(oid_finstruct): continue

			self._oids_finstate.append(record_finstate.Oid().text)

	def ReadOidsFindata(self):
		""" Сбор OID финданных """
		self._oids_findata.clear()

		if not self._flag_findata: return

		if self._flag_all_periods:
			self._oids_findata = C90_RecordFindata.Oids(CONTAINER_LOCAL).items

		else:
			dy : int = self.workspace.Dy()
			dm : int = self.workspace.Dm()

			self._oids_findata = self.findata.OidsInDyDmDd(dy, dm)

	def ReadOidsRules(self):
		""" Сбор OID правил обработки данных """
		self._oids_rules.clear()

		if self._flag_rules_replace_text                 : self._oids_rules.extend(self.rules.OidsByType(RULE_REPLACE_TEXT))
		if self._flag_rules_detect_findescription_by_text: self._oids_rules.extend(self.rules.OidsByType(RULE_DETECT_FINDESCRIPTION_BY_TEXT))

	# Модель объектов
	def SetupModelObjects(self):
		""" Настройка модели объектов """
		self.model_objects.removeAll()

	def LoadModelObjects(self):
		""" Загрузка данных в модель объектов """
		item_finstruct                          = C20_StandardItem("Финструктура",                                           "finstruct")
		item_finactions                         = C20_StandardItem("Финдействия",                                            "finactions")
		item_findescription                     = C20_StandardItem("Финсостав",                                              "findescription")
		item_finstate                           = C20_StandardItem("Финсостояние",                                           "finstate")
		item_findata                            = C20_StandardItem("Финданные",                                              "findata")
		item_finactions_findescription          = C20_StandardItem("Финсостав в финдействиях",                               "finactions_findescription")
		item_rule_replace_text                  = C20_StandardItem("Правила замены текстовых фрагментов",                    "rule_replace_text")
		item_rule_detect_findescription_by_text = C20_StandardItem("Правила определения финсостава по текстовым фрагментам", "rule_detect_findescription_by_text")

		item_finactions.appendRow(item_finactions_findescription)
		item_findata.appendRow(item_finactions)

		item_finstruct.appendRow(item_finstate)

		self.model_objects.appendRow(item_finstruct)
		self.model_objects.appendRow(item_findata)
		self.model_objects.appendRow(item_findescription)
		self.model_objects.appendRow(item_rule_replace_text)
		self.model_objects.appendRow(item_rule_detect_findescription_by_text)

	def SetupCheckedModelObjects(self):
		""" Настройка отметок модели объектов """
		for index_object in self.model_objects.indexes():
			item_object : QStandardItem = self.model_objects.itemFromIndex(index_object)
			item_object.setCheckable(True)
			item_object.setCheckState(Qt.Unchecked)

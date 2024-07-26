# ФОРМА ФИНАНАЛИЗ: ЛОГИКА ДАННЫХ
from PySide6.QtWidgets import QProgressDialog

from L11_datetime          import CalcDyDmByShiftDm
from L20_PySide6           import RequestItems
from L70_form_finanalytics import C70_FormFinanalytics
from L90_findescription    import C90_RecordFindescription


class C80_FormFinanalytics(C70_FormFinanalytics):
	""" Форма Финанализ: Логика данных """

	# Модель динамики финсостава
	def CalcDataFindescriptionDynamic(self):
		""" Расчёт данных модели финсостава """
		self._data_findescription_dynamic_income.clear()
		self._data_findescription_dynamic_outcome.clear()

		dialog_progress = QProgressDialog("Динамика финсостава", "Отмена", 0, len(self._oids_findescription_dynamic))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.setMinimumHeight(120)
		dialog_progress.setWindowTitle("Динамика финсостава")

		for findescription_oid in self._oids_findescription_dynamic:
			record_findescription       = C90_RecordFindescription(findescription_oid)

			dialog_progress.setLabelText(record_findescription.Name())
			dialog_progress.setValue(dialog_progress.data() + 1)
			dialog_progress.forceShow()
			self.application.processEvents()

			amounts_income  : list[int] = [0] * 13
			amounts_outcome : list[int] = [0] * 13

			dy              : int       = self.workspace.Dy()
			dm              : int       = self.workspace.Dm()

			for index_shift in range(13):
				amounts_income[index_shift]  = self.finstatistic.CalcIncomeByFindescription(findescription_oid, dy, dm)
				amounts_outcome[index_shift] = self.finstatistic.CalcOutcomeByFindescription(findescription_oid, dy, dm)

				dy, dm = CalcDyDmByShiftDm(dy, dm, -1)

			self._data_findescription_dynamic_income[record_findescription.Name()]  = amounts_income
			self._data_findescription_dynamic_outcome[record_findescription.Name()] = amounts_outcome

	def IncFindescriptionDynamic(self):
		""" Расширение анализа динамики финсостава """
		findescription_names : list[str] | None = RequestItems("Динамика финсостава", "Расширение анализа финсостава", self.findescription.Names())
		if findescription_names is None: return

		findescription_oids  : list[str]        = self.findescription.NamesToIdos(findescription_names)

		self._oids_findescription_dynamic = list(set(self._oids_findescription_dynamic).union(findescription_oids))

		self.on_RequestShowFindescriptionDynamic()

	def DecFindescriptionDynamic(self):
		""" Сокращение анализа динамики финсостава """
		if not self._oid_processing                                         : return
		if     self._oid_processing not in self._oids_findescription_dynamic: return

		self._oids_findescription_dynamic.remove(self._oid_processing)

		self.on_RequestShowFindescriptionDynamic()

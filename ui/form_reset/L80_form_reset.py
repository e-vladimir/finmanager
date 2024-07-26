# ФОРМА СБРОС ДАННЫХ: ЛОГИКА ДАННЫХ

from PySide6.QtWidgets    import QProgressDialog

from L00_containers       import CONTAINER_LOCAL

from L70_form_reset       import C70_FormReset
from L90_finactions       import C90_RecordFinactions
from L90_findata          import C90_RecordFindata
from L90_findescription   import C90_RecordFindescription
from L90_finstate         import C90_RecordFinstate
from L90_finstruct        import C90_RecordFinstruct
from L90_processing_rules import C90_RecordProcessingRules


class C80_FormReset(C70_FormReset):
	""" Форма Сброс данных: Логика данных """

	# Обработка данных
	def ProcessingReset(self):
		"""  """
		count_total : int = 0
		count_total      += len(self._idos_finstruct)
		count_total      += len(self._idos_finactions)
		count_total      += len(self._idos_findescription)
		count_total      += len(self._idos_findescription_in_finactions)
		count_total      += len(self._idos_finstate)
		count_total      += len(self._idos_findata)
		count_total      += len(self._idos_rules)

		counter     : int = 0

		dialog_progress   = QProgressDialog(f"Сброс данных", "Отменить", 0, count_total, self)
		dialog_progress.setMinimumSize(480, 120)
		dialog_progress.setWindowTitle("Сброс данных")

		record_finstruct      = C90_RecordFinstruct()
		record_finstate       = C90_RecordFinstate()
		record_findata        = C90_RecordFindata()
		record_finactions     = C90_RecordFinactions()
		record_findescription = C90_RecordFindescription()
		record_rule           = C90_RecordProcessingRules()

		for ido in self._idos_finstruct:
			if dialog_progress.wasCanceled(): break

			counter += 1
			dialog_progress.setLabelText(f"{counter + 1} из {count_total}, осталось {count_total - counter}")
			dialog_progress.setValue(counter)
			dialog_progress.forceShow()

			self.application.processEvents()

			record_finstruct.Ido(ido)
			record_finstruct.DeleteObject(CONTAINER_LOCAL)

		for ido in self._idos_finstate:
			if dialog_progress.wasCanceled(): break

			counter += 1
			dialog_progress.setLabelText(f"{counter + 1} из {count_total}, осталось {count_total - counter}")
			dialog_progress.setValue(counter)
			dialog_progress.forceShow()

			self.application.processEvents()

			record_finstate.Ido(ido)
			record_finstate.DeleteObject(CONTAINER_LOCAL)

		for ido in self._idos_findata:
			if dialog_progress.wasCanceled(): break

			counter += 1
			dialog_progress.setLabelText(f"{counter + 1} из {count_total}, осталось {count_total - counter}")
			dialog_progress.setValue(counter)
			dialog_progress.forceShow()

			self.application.processEvents()

			record_findata.Ido(ido)
			record_findata.DeleteObject(CONTAINER_LOCAL)

		for ido in self._idos_finactions:
			if dialog_progress.wasCanceled(): break

			counter += 1
			dialog_progress.setLabelText(f"{counter + 1} из {count_total}, осталось {count_total - counter}")
			dialog_progress.setValue(counter)
			dialog_progress.forceShow()

			self.application.processEvents()

			record_finactions.Ido(ido)
			record_finactions.DeleteObject(CONTAINER_LOCAL)

		for ido in self._idos_findescription:
			if dialog_progress.wasCanceled(): break

			counter += 1
			dialog_progress.setLabelText(f"{counter + 1} из {count_total}, осталось {count_total - counter}")
			dialog_progress.setValue(counter)
			dialog_progress.forceShow()

			self.application.processEvents()

			record_findescription.Ido(ido)
			record_findescription.DeleteObject(CONTAINER_LOCAL)

		for ido in self._idos_rules:
			if dialog_progress.wasCanceled(): break

			counter += 1
			dialog_progress.setLabelText(f"{counter + 1} из {count_total}, осталось {count_total - counter}")
			dialog_progress.setValue(counter)
			dialog_progress.forceShow()

			self.application.processEvents()

			record_rule.Ido(ido)
			record_rule.DeleteObject(CONTAINER_LOCAL)

		for ido in self._idos_findescription_in_finactions:
			if dialog_progress.wasCanceled(): break

			counter += 1
			dialog_progress.setLabelText(f"{counter + 1} из {count_total}, осталось {count_total - counter}")
			dialog_progress.setValue(counter)
			dialog_progress.forceShow()

			self.application.processEvents()

			record_finactions.Ido(ido)
			record_finactions.FindescriptionIdos([])

		dialog_progress.setValue(count_total)

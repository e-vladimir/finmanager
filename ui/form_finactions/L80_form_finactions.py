# ФОРМА ФИНДЕЙСТВИЯ: ЛОГИКА ДАННЫХ

from PySide6.QtCore      import Qt
from PySide6.QtWidgets   import QProgressDialog

from G10_math_linear     import CalcBetween
from G11_convertor_data  import AmountToString

from L00_containers      import CONTAINER_LOCAL
from L00_months          import MONTHS_SHORT
from L20_PySide6         import RequestConfirm, RequestValue, RequestText, QFindReplaceTextDialog, ROLE_IDO, C20_StandardItem
from L70_form_finactions import C70_FormFinactions
from L90_finactions      import C90_FinactionsRecord


class C80_FormFinactions(C70_FormFinactions):
	""" Форма Финдействия: Логика данных """

	# Финдействия
	def LoadFinactions(self):
		""" Загрузка финдействий """
		dy, dm = self.workspace.DyDm()

		for self._processing_dd in self.finactions.DdsInDyDm(dy, dm):
			self.LoadDd()

			for self._processing_ido in self.finactions.IdosInDyDmDd(dy, dm, self._processing_dd): self.LoadFinactionsRecord()

	# Запись финдействий
	def CreateFinactionsRecord(self):
		""" Создание записи финдействий """
		dy, dm = self.workspace.DyDm()
		dd     = CalcBetween(1, self._processing_dd, 31)

		amount  : int | None = RequestValue("Создание записи финдействий", f"Запись финдействий от {dd:02d} {MONTHS_SHORT[dm]} {dy:04d}", 0.00, -99999999.00, 99999999.00)
		if amount is None: return

		self._processing_dd  = dd
		self._processing_ido = self.finactions.CreateRecord(dy, dm, dd, amount)

	def OpenFinactionsRecord(self):
		""" Открытие записи финдействий """
		self.SendProcessingIdoToWorkspace()

		self.application.form_finactions_record.Open()

	def DeleteFinactionsRecord(self):
		""" Удаление записи финдействий """
		record       = C90_FinactionsRecord(self._processing_ido)
		amount : str = AmountToString(record.Amount(), False, True)

		if not RequestConfirm("Финдействия", f"Удаление записи финдействий\n{amount} от {record.DdDmDyToString()}"): return

		record.DeleteObject(CONTAINER_LOCAL)

		self.CleanFinactionsRecord()

	def SplitFinactionsRecord(self):
		""" Разделение записи финдействий """
		record               = C90_FinactionsRecord(self._processing_ido)
		amount  : int | None = RequestValue("Разделение записи финдействий", f"{AmountToString(record.Amount(), False, True)} от {record.DdDmDyToString()}", int(record.Amount()), -99999999, 99999999)
		if amount is None: return

		ido_new : str        = record.SplitAmount(amount)

		self.LoadFinactionsRecord()

		self._processing_ido = ido_new
		self.LoadFinactionsRecord()

	def EditNoteFinactionsRecord(self):
		""" Редактирование примечания записи финдействия """
		record            = C90_FinactionsRecord(self._processing_ido)

		note : str | None = RequestText("Запись финдействий", f"Запись {AmountToString(record.Amount(), False, True)} от {record.DdDmDyToString()}", record.Note())
		if note is None: return

		record.Note(note)

	# Утилиты поиска и замены
	def ReplaceText(self):
		""" Замена текстового фрагмента """
		record           = C90_FinactionsRecord(self._processing_ido)

		dialog_replace   = QFindReplaceTextDialog("Утилиты поиска и замены", "Фрагмент поиска -> Фрагмент замены", record.Note(), record.Note(), self)
		if not dialog_replace.exec_(): return

		dy, dm           = self.workspace.DyDm()
		idos : list[str] = self.finactions.IdosInDyDmDd(dy, dm)

		dialog_progress  = QProgressDialog(self)
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setMaximum(len(idos))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.setWindowTitle("Замена текстового фрагмента")

		for index_ido, self._processing_ido in enumerate(idos):
			dialog_progress.setLabelText(f"Ожидает обработки: {dialog_progress.maximum() - dialog_progress.value()}")
			dialog_progress.setValue(index_ido + 1)

			record     = C90_FinactionsRecord(self._processing_ido)
			note : str = record.Note()

			if dialog_replace.textFind() not in note: continue

			note       = note.replace(dialog_replace.textFind(), dialog_replace.textReplace())
			record.Note(note)

			self.LoadFinactionsRecord()

		dialog_progress.setValue(dialog_progress.maximum())

	# Цветовая метка
	def SetColor(self):
		""" Установка цветовой метки """
		if self._processing_idos:
			dialog_progress = QProgressDialog(self)
			dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
			dialog_progress.setMaximum(len(self._processing_idos))
			dialog_progress.setMinimumWidth(480)
			dialog_progress.setWindowTitle("Установка цветовой метки")

			for index_ido, self._processing_ido in enumerate(self._processing_idos):
				dialog_progress.setLabelText(f"Ожидает обработки: {dialog_progress.maximum() - dialog_progress.value()}")
				dialog_progress.setValue(index_ido + 1)

				record = C90_FinactionsRecord(self._processing_ido)
				record.Color(self._processing_color)

				self.LoadFinactionsRecord()

			dialog_progress.setValue(dialog_progress.maximum())

		elif self._processing_ido:
			record = C90_FinactionsRecord(self._processing_ido)
			record.Color(self._processing_color)

	# Пакетный режим
	def ResetPack(self):
		""" Сброс пакетного режима """
		for ido in self._processing_idos:
			item_record : C20_StandardItem | None = self.model_data.itemByData(ido, ROLE_IDO)
			if item_record is None: continue

			item_record.setCheckState(Qt.CheckState.Unchecked)

	def ExpandPackByText(self):
		""" Расширение пакета по текстовому фрагменту """
		record            = C90_FinactionsRecord(self._processing_ido)

		text : str | None = RequestText("Пакетный режим", "Расширение пакета", record.Note())
		if text is None: return

		text              = text.lower()

		item_root  = self.model_data.invisibleRootItem()

		for index_row_dd in range(self.model_data.rowCount()):
			item_dd = item_root.child(index_row_dd, 0)

			for index_row_record in range(item_dd.rowCount()):
				item_amount = item_dd.child(index_row_record, 0)
				item_note   = item_dd.child(index_row_record, 2)

				if text not in item_note.text().lower(): continue

				item_amount.setCheckState(Qt.CheckState.Checked)

	def ReducePackByText(self):
		""" Сокращение пакета по текстовому фрагменту """
		record            = C90_FinactionsRecord(self._processing_ido)

		text : str | None = RequestText("Пакетный режим", "Сокращение пакета", record.Note())
		if text is None: return

		text              = text.lower()

		item_root  = self.model_data.invisibleRootItem()

		for index_row_dd in range(self.model_data.rowCount()):
			item_dd = item_root.child(index_row_dd, 0)

			for index_row_record in range(item_dd.rowCount()):
				item_amount = item_dd.child(index_row_record, 0)
				item_note   = item_dd.child(index_row_record, 2)

				if text not in item_note.text().lower(): continue

				item_amount.setCheckState(Qt.CheckState.Unchecked)

	# Правила обработки данных
	def ApplyRulesToSelection(self):
		""" Применение правил обработки данных к выбранным записям """
		if self._processing_idos:
			dialog_progress = QProgressDialog(self)
			dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
			dialog_progress.setMaximum(len(self._processing_idos))
			dialog_progress.setMinimumWidth(480)
			dialog_progress.setWindowTitle("Применение правил обрабоки данных")

			for index_ido, self._processing_ido in enumerate(self._processing_idos):
				dialog_progress.setLabelText(f"Ожидает обработки: {dialog_progress.maximum() - dialog_progress.value()}")
				dialog_progress.setValue(index_ido + 1)

				record = C90_FinactionsRecord(self._processing_ido)
				record.ApplyProcessingRulesReplaceText()
				record.ApplyProcessingRulesDetectLabel()

				self.LoadFinactionsRecord()

			dialog_progress.setValue(dialog_progress.maximum())

		elif self._processing_ido:
			record = C90_FinactionsRecord(self._processing_ido)
			record.ApplyProcessingRulesReplaceText()
			record.ApplyProcessingRulesDetectLabel()

	def ApplyRulesToAll(self):
		""" Применение правил обработки данных ко всем записям """
		dy, dm           = self.workspace.DyDm()
		idos : list[str] = self.finactions.IdosInDyDmDd(dy, dm)

		dialog_progress = QProgressDialog(self)
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setMaximum(len(idos))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.setWindowTitle("Применение правил обрабоки данных")

		for index_ido, self._processing_ido in enumerate(idos):
			dialog_progress.setLabelText(f"Ожидает обработки: {dialog_progress.maximum() - dialog_progress.value()}")
			dialog_progress.setValue(index_ido + 1)

			record = C90_FinactionsRecord(self._processing_ido)
			record.ApplyProcessingRulesReplaceText()
			record.ApplyProcessingRulesDetectLabel()

			self.LoadFinactionsRecord()

		dialog_progress.setValue(dialog_progress.maximum())

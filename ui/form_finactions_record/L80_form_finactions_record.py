# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: ЛОГИКА ДАННЫХ

from L20_PySide6                import ROLE_IDO
from L70_form_finactions_record import C70_FormFinactionsRecord


class C80_FormFinactionsRecord(C70_FormFinactionsRecord):
	""" Форма Запись финдействий: Логика данных """

	# Финструктура
	def LoadFinstruct(self):
		""" Загрузка финструктуры """
		dy, dm = self.workspace.DyDm()
		
		for self._processing_name in self.finstruct.GroupsInDyDm(dy, dm): self.LoadFinstructGroup()
		for self._processing_ido  in self.finstruct.IdosInDyDm(dy, dm)  : self.LoadFinstructRecord()

	# Запись финдействий
	def SaveFinactionsRecord(self):
		""" Сохранение записи финдействий """
		self.finactions_record.Dy(int(self.cbbox_dy.currentText()))
		self.finactions_record.Dm(self.cbbox_dm.currentIndex() + 1)
		self.finactions_record.Dd(self.edit_dd.value())

		self.finactions_record.Amount(self.edit_amount.value())

		self.finactions_record.Note(self.edit_note.text())
		self.finactions_record.FinstructIdos(self.model_finstruct.dataByCheckState(ROLE_IDO))
		self.finactions_record.Labels(self.edit_labels.toPlainText().split('\n'))

# ФОРМА ЭКСПОРТ ДАННЫХ: ЛОГИКА ДАННЫХ

from G11_convertor_data import AmountToString

from L00_months         import MONTHS_SHORT
from L00_options        import OPTIONS
from L20_PySide6        import ShowMessage
from L70_form_export    import C70_FormExport
from L90_finactions     import C90_FinactionsRecord
from L90_finstruct      import C90_FinstructRecord


class C80_FormExport(C70_FormExport):
	""" Форма Экспорт данных: Логика данных """

	# Экспорт финдействий
	def ProcessingExportFinactions(self):
		""" Выполнение экспорта финдействий """
		finstruct_names : list[str] = []
		dy, dm                      = self.workspace.DyDm()

		match self._options_finactions_finstruct_mode:
			case OPTIONS.MODE_SELECT:
				finstruct_names.extend(self._options_finactions_finstruct_names)

			case OPTIONS.MODE_ALL:
				match self._options_finactions_period_mode:
					case OPTIONS.MODE_ALL: finstruct_names.extend(self.finstruct.Names())
					case OPTIONS.MODE_DY : finstruct_names.extend(self.finstruct.NamesInDyDm(dy))
					case OPTIONS.MODE_DM : finstruct_names.extend(self.finstruct.NamesInDyDm(dy, dm))

		prefix          : str       = ""
		postfix         : str       = ".csv"

		match self._options_finactions_period_mode:
			case OPTIONS.MODE_DM: prefix = f"{self._options_finactions_period_dy} {MONTHS_SHORT[self._options_finactions_period_dm]} - "
			case OPTIONS.MODE_DY: prefix = f"{self._options_finactions_period_dy} - "

		for finstruct_name in finstruct_names:
			idos : list[str] = []

			match self._options_finactions_period_mode:
				case OPTIONS.MODE_ALL:
					finstruct_record = C90_FinstructRecord()

					for dy in self.finactions.AvailableDys():
						for dm in range(1, 13):
							if not finstruct_record.SwitchByName(dy, dm, finstruct_name): continue

							idos.extend(self.finactions.IdosInDyDmDd(dy, dm, finstruct_ido=finstruct_record.Ido().data))

				case OPTIONS.MODE_DY :
					finstruct_record = C90_FinstructRecord()

					dy : int = self._options_finactions_period_dy

					for dm in range(1, 13):
						if not finstruct_record.SwitchByName(dy, dm, finstruct_name): continue

						idos.extend(self.finactions.IdosInDyDmDd(dy, dm, finstruct_ido=finstruct_record.Ido().data))

				case OPTIONS.MODE_DM :
					finstruct_record = C90_FinstructRecord()

					dy : int = self._options_finactions_period_dy
					dm : int = self._options_finactions_period_dm

					if not finstruct_record.SwitchByName(dy, dm, finstruct_name): continue

					idos.extend(self.finactions.IdosInDyDmDd(dy, dm, finstruct_ido=finstruct_record.Ido().data))

			data : list[list[str]] = []
			data.append(["Дата", "Счёт", "Сумма", "Примечание", "Метки"])

			for ido in idos:
				record_finactions = C90_FinactionsRecord(ido)

				subdata_date    : str = f"{record_finactions.DdDmDyToString()}"
				subdata_account : str = f"{finstruct_name}"
				subdata_amount  : str = f"{record_finactions.Amount():.02f}"
				subdata_note    : str = f"{record_finactions.Note()}"
				subdata_labels  : str = ', '.join(record_finactions.Labels())

				data.append([subdata_date, subdata_account, subdata_amount, subdata_note, subdata_labels])

			file_name = f"{prefix}{finstruct_name}{postfix}"
			file_path = self._options_finactions_folder.joinpath(file_name)

			if len(data) < 2: continue

			with open(f"{file_path.absolute()}", "w", encoding="utf-8") as csv_file:
				for subdata in data:
					csv_file.write(';'.join(subdata) + ';' + '\n')

		ShowMessage("Экспорт финдействий", "Экспорт финдействий завершен")

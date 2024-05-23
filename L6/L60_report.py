# ГЕНЕТАОР ОТЧЁТОВ: МЕХАНИКА ДАННЫХ

from L00_findescription  import FINDESCRIPTION_CATEGORIES
from L00_months          import MONTHS_SHORT

from L10_converts        import AmountToString
from L11_datetime        import CalcDyDmByShiftDm
from L50_report          import C50_Report
from L90_finactions      import C90_RecordFinactions
from L90_findata         import C90_RecordFindata
from L90_findescription  import C90_RecordFindescription
from L90_finstate        import C90_RecordFinstate
from L90_finstruct       import C90_RecordFinstruct


class C60_Report(C50_Report):
	""" Генератор отчётов: Механика данных """

	# Параметры
	def ReportType(self, text : str = None) -> str:
		""" Тип отчёта """
		if text is None: return self._report_type
		else           :        self._report_type = text

	def ReportDy(self, dy : int = None) -> int:
		""" Год отчёта """
		if dy is None: return self._report_dy
		else         :        self._report_dy = dy

	def ReportDm(self, dm : int = None) -> int:
		""" Месяц отчёта """
		if dm is None: return self._report_dm
		else         :        self._report_dm = dm

	# Сбор данных
	def CalcNamesProcessingFromFinstruct(self):
		""" Сбор списка OID финструктуры """
		dy     : int      = self.ReportDy()
		dm     : int      = self.ReportDm()

		result : set[str] = set()

		for index_shift in range(12 * 10):
			oids  : list[str] = self.finstruct.OidsInDyDm(dy, dm)
			names : list[str] = self.finstruct.OidsToNames(list(oids))
			result            = result.union(set(names))

			dy, dm            = CalcDyDmByShiftDm(dy, dm, -1)

		self._names_processing = list(result)

	# Фрагменты отчёта
	def InitReport(self):
		""" Оформление заголовка отчёта """
		self._report_data.clear()

		subdata : list[str] = self._report_patterns[:53]

		self._report_data.extend(subdata)

	def AppendHeader(self):
		""" Добавление заголовка отчёта """
		index_start : int       = 53
		subdata     : list[str] = self._report_patterns[index_start : index_start + 6]

		self._report_data.extend(subdata[:2])
		self._report_data.append(subdata[2].replace("{report_type}", f"{self.ReportType().upper()}"))
		self._report_data.append(subdata[3].replace("{dmdy}",        f"{self.workspace.DmDyToString().upper()}"))
		self._report_data.extend(subdata[4:])

	def AppendSeparator(self):
		""" Добавление разделителя """
		index_start : int       = 60
		subdata     : list[str] = [self._report_patterns[index_start]]

		self._report_data.extend(subdata)

	def AppendFinstate(self):
		""" Добавление фрагмента Финсостояние """
		index_start : int       = 62
		subdata     : list[str] = self._report_patterns[index_start : index_start + 23]

		dy          : int = self.workspace.Dy()
		dm          : int = self.workspace.Dm()

		self._report_data.extend(subdata[:14])

		for finstruct_name in self.finstruct.StructuredNamesInDyDm(dy, dm):
			record_finstruct       = C90_RecordFinstruct()
			record_finstruct.SwitchByName(dy, dm, finstruct_name.strip())

			record_finstate        = C90_RecordFinstate()
			record_finstate.SwitchByFinstructOid(record_finstruct.Oid().text)

			amount_income    : int = record_finstate.CalcIncome()
			amount_outcome   : int = record_finstate.CalcOutcome()

			amount_initial   : int = record_finstate.RemainsInitial()
			amount_final     : int = record_finstate.CalcRemainFinal()
			amount_delta     : int = amount_final - amount_initial

			line_15          : str = subdata[15]
			line_15                = line_15.replace("{finstruct}", finstruct_name.strip())
			line_15                = line_15.replace("{padding}", f"{5 + finstruct_name[:5].count(' ') * 5}")

			self._report_data.append(subdata[13])
			self._report_data.append(subdata[14])
			self._report_data.append(line_15)
			self._report_data.append(subdata[16].replace("{remain_initial}", AmountToString(amount_initial, False, False)))
			self._report_data.append(subdata[17].replace("{remain_delta}",   AmountToString(amount_delta,   False, True)))
			self._report_data.append(subdata[18].replace("{remain_final}",   AmountToString(amount_final,   False, False)))
			self._report_data.append(subdata[19].replace("{amount_income}",  AmountToString(amount_income,  False, True)))
			self._report_data.append(subdata[20].replace("{amount_outcome}", AmountToString(amount_outcome, False, True)))
			self._report_data.append(subdata[21])

		self._report_data.append(subdata[22])

	def AppendFinstatistic(self):
		""" Добавление фрагмента Финсостояние """
		index_start : int       = 88
		subdata     : list[str] = self._report_patterns[index_start : index_start + 43]

		dy          : int = self.workspace.Dy()
		dm          : int = self.workspace.Dm()

		self._report_data.extend(subdata[:4])

		for index_row, findescription_category in enumerate(sorted(FINDESCRIPTION_CATEGORIES)):
			if index_row > 0:
				self._report_data.append(subdata[16])
				self._report_data.append(subdata[17])

			self._report_data.append(subdata[ 4])
			self._report_data.append(subdata[ 5])
			self._report_data.append(subdata[ 6].replace("{findescription}", findescription_category.upper()))
			self._report_data.append(subdata[ 7])
			self._report_data.append(subdata[ 8])
			self._report_data.append(subdata[ 9])
			self._report_data.append(subdata[10])

			for findescription_oid in self.findescription.OidsByCategory(findescription_category):
				record_findescription = C90_RecordFindescription(findescription_oid)
				amount_income  : int  = self.finstatistic.CalcIncomeByFindescription(findescription_oid, dy, dm)
				amount_outcome : int  = self.finstatistic.CalcOutcomeByFindescription(findescription_oid, dy, dm)

				if (not amount_income) and (not amount_outcome): continue

				line_12 : str = subdata[12]
				line_12       = line_12.replace("{padding}", "5")
				line_12       = line_12.replace("{findescription}", record_findescription.Name())

				self._report_data.append(subdata[10])
				self._report_data.append(subdata[11])
				self._report_data.append(line_12)
				self._report_data.append(subdata[13].replace("{amount_income}", AmountToString(amount_income, False, True)))
				self._report_data.append(subdata[14].replace("{amount_outcome}", AmountToString(amount_outcome, False, True)))
				self._report_data.append(subdata[15])

		self._report_data.append(subdata[42])

	def AppendFindata(self):
		""" Добавление фрагмента Финданные """
		index_start : int       = 134
		subdata     : list[str] = self._report_patterns[index_start : index_start + 19]

		dy          : int = self.workspace.Dy()
		dm          : int = self.workspace.Dm()

		self._report_data.extend(self._report_patterns[index_start : index_start + 4])

		for index_row, dd in enumerate(self.findata.Dds(dy, dm)):
			if index_row > 0:
				self._report_data.append(subdata[16])
				self._report_data.append(subdata[17])

			dddmdy : str = f"{dd:02d} {MONTHS_SHORT[dm]} {dy}".upper()

			self._report_data.append(subdata[ 4])
			self._report_data.append(subdata[ 5])
			self._report_data.append(subdata[ 6].replace("{dddmdy}", dddmdy))
			self._report_data.append(subdata[ 7])
			self._report_data.append(subdata[ 8])
			self._report_data.append(subdata[ 9])

			for findata_oid in self.findata.OidsInDyDmDd(dy, dm, dd):
				record_findata   = C90_RecordFindata(findata_oid)
				record_finstruct = C90_RecordFinstruct(record_findata.FinstructOid())

				self._report_data.append(subdata[10])
				self._report_data.append(subdata[11])
				self._report_data.append(subdata[12].replace("{amount}", AmountToString(record_findata.Amount(), False, True)))
				self._report_data.append(subdata[13].replace("{finstruct}", record_finstruct.Name()))
				self._report_data.append(subdata[14].replace("{note}", record_findata.Note()))
				self._report_data.append(subdata[15])

		self._report_data.append(subdata[18])

	def AppendFinactions(self):
		""" Добавление фрагмента Финдействия """
		index_start : int       = 156
		subdata     : list[str] = self._report_patterns[index_start : index_start + 21]

		dy          : int = self.workspace.Dy()
		dm          : int = self.workspace.Dm()

		self._report_data.extend(self._report_patterns[index_start : index_start + 4])

		for index_row, dd in enumerate(self.finactions.Dds(dy, dm)):
			if index_row > 0:
				self._report_data.append(subdata[18])
				self._report_data.append(subdata[19])

			dddmdy : str = f"{dd:02d} {MONTHS_SHORT[dm]} {dy}".upper()

			self._report_data.append(subdata[ 4])
			self._report_data.append(subdata[ 5])
			self._report_data.append(subdata[ 6].replace("{dddmdy}", dddmdy))
			self._report_data.append(subdata[ 7])
			self._report_data.append(subdata[ 8])
			self._report_data.append(subdata[ 9])
			self._report_data.append(subdata[10])

			for finactions_oid in self.finactions.OidsInDyDmDd(dy, dm, dd):
				record_finactions                = C90_RecordFinactions(finactions_oid)
				finstruct_names      : list[str] = self.finstruct.OidsToNames(record_finactions.FinstructOids())
				findescription_names : list[str] = self.findescription.OidsToNames(record_finactions.FindescriptionOids())

				self._report_data.append(subdata[11])
				self._report_data.append(subdata[12])
				self._report_data.append(subdata[13].replace("{amount}", AmountToString(record_finactions.Amount(), False, True)))
				self._report_data.append(subdata[14].replace("{finstruct}", '<br>'.join(finstruct_names)))
				self._report_data.append(subdata[15].replace("{findescription}", '<br>'.join(findescription_names)))
				self._report_data.append(subdata[16].replace("{note}", record_finactions.Note()))
				self._report_data.append(subdata[17])

		self._report_data.append(subdata[20])

	def CloseReport(self):
		""" Закрытие отчёта """
		index_start : int       = 205
		subdata     : list[str] = self._report_patterns[index_start:]

		self._report_data.extend(subdata)

	def AppendRecordFinstructHistoryRemains(self):
		""" Добавление блока хронологии финсостояния по финструктуре """
		dy          : int       = self.ReportDy()
		dm          : int       = self.ReportDm()

		index_start : int       = 180
		subdata     : list[str] = self._report_patterns[index_start : index_start + 23]

		self._report_data.append(subdata[ 0])
		self._report_data.append(subdata[ 1])
		self._report_data.append(subdata[ 2].replace("{finstruct}", self._name_processing.upper()))
		self._report_data.append(subdata[ 3])

		self._report_data.extend(subdata[ 4:13])

		record_finstruct        = C90_RecordFinstruct()
		record_finstate         = C90_RecordFinstate()

		for index_shift in range(12 * 10):
			dy, dm               = CalcDyDmByShiftDm(dy, dm, -1 if index_shift > 0 else 0)

			if not record_finstruct.SwitchByName(dy, dm, self._name_processing)     : continue
			if not record_finstate.SwitchByFinstructOid(record_finstruct.Oid().text): continue

			dm_dy          : str = f"{MONTHS_SHORT[dm]} {dy}"

			amount_income  : int = record_finstate.CalcIncome()
			amount_outcome : int = record_finstate.CalcOutcome()

			amount_initial : int = record_finstate.RemainsInitial()
			amount_final   : int = record_finstate.CalcRemainFinal()
			amount_delta   : int = amount_final - amount_initial

			self._report_data.append(subdata[14])
			self._report_data.append(subdata[15].replace("{dydm}", f"{dm_dy}"))
			self._report_data.append(subdata[16].replace("{remain_initial}", f"{AmountToString(amount_initial, flag_sign=True)}"))
			self._report_data.append(subdata[17].replace("{remain_delta}",   f"{AmountToString(amount_delta,   flag_sign=True)}"))
			self._report_data.append(subdata[18].replace("{remain_final}",   f"{AmountToString(amount_final,   flag_sign=True)}"))
			self._report_data.append(subdata[19].replace("{amount_income}",  f"{AmountToString(amount_income,  flag_sign=True)}"))
			self._report_data.append(subdata[20].replace("{amount_outcome}", f"{AmountToString(amount_outcome, flag_sign=True)}"))
			self._report_data.append(subdata[21])

		self._report_data.append(subdata[22])

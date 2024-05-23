# ФИНСОСТОЯНИЕ: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL

from L11_datetime           import CalcDyDmByShiftDm
from L40_finactions         import C40_RecordFinactions
from L40_findata            import C40_RecordFindata

from L70_finstate           import C70_RecordFinstate, C70_Finstate
from L90_finstruct          import C90_RecordFinstruct


class C80_RecordFinstate(C70_RecordFinstate):
	""" Запись финсостояния: Логика данных """

	# Управление записью
	def SwitchByFinstructOid(self, oid: str) -> bool:
		""" Переключение записи по OID финструктуры """
		filter_finstate = C30_FilterLinear1D(self.Oci().text)
		filter_finstate.FilterPidCvlByEqual(self.f_finstruct_oid.Pid().text, oid)
		filter_finstate.Capture(CONTAINER_LOCAL)

		oids : list[str] = filter_finstate.Oids().items
		if not oids: return False

		self.Oid(oids[0])
		return True

	# Калькуляция данных
	def CalcIncomeOrOutcome(self, flag_income: bool = False) -> int:
		""" Расчёт дохода/расхода """
		record_finstruct      = C90_RecordFinstruct(self.FinstructOid())
		flag_account_v : bool = bool(record_finstruct.ParentOid())

		findata               = C40_RecordFindata()
		finactions            = C40_RecordFinactions()

		oci_findata    : str  = findata.Oci().text
		oci_finactions : str  = finactions.Oci().text

		filter_findata        = C30_FilterLinear1D(oci_finactions if flag_account_v else oci_findata)

		if flag_account_v:
			pid_amount    = finactions.f_amount.Pid().text
			pid_finstruct = finactions.f_finstruct_oids.Pid().text

			filter_findata.FilterPidCvlByInclude(pid_finstruct, record_finstruct.Oid().text)
		else             :
			pid_amount    = findata.f_amount.Pid().text
			pid_finstruct = findata.f_finstruct_oid.Pid().text

			filter_findata.FilterPidCvlByEqual(pid_finstruct, record_finstruct.Oid().text)

		if flag_income:	filter_findata.FilterPidCvlByMore(pid_amount, 0)
		else          : filter_findata.FilterPidCvlByLess(pid_amount, 0)

		filter_findata.Capture(CONTAINER_LOCAL)

		return sum(filter_findata.ToFloats(pid_amount).items)

	def CalcIncome(self) -> int:
		""" Расчёт дохода """
		return self.CalcIncomeOrOutcome(True)

	def CalcOutcome(self) -> int:
		""" Расчёт расхода """
		return self.CalcIncomeOrOutcome(False)

	def CalcRemainFinal(self) -> int:
		""" Расчёт остатка конечного с учётом финданных - финструктуры """
		record_finstruct      = C90_RecordFinstruct(self.FinstructOid())
		flag_account_v : bool = bool(record_finstruct.ParentOid())

		findata               = C40_RecordFindata()
		finactions            = C40_RecordFinactions()

		oci_findata    : str  = findata.Oci().text
		oci_finactions : str  = finactions.Oci().text

		filter_findata        = C30_FilterLinear1D(oci_finactions if flag_account_v else oci_findata)

		if flag_account_v:
			pid_amount    = finactions.f_amount.Pid().text
			pid_finstruct = finactions.f_finstruct_oids.Pid().text

			filter_findata.FilterPidCvlByInclude(pid_finstruct, record_finstruct.Oid().text)
		else             :
			pid_amount    = findata.f_amount.Pid().text
			pid_finstruct = findata.f_finstruct_oid.Pid().text

			filter_findata.FilterPidCvlByEqual(pid_finstruct, record_finstruct.Oid().text)

		filter_findata.Capture(CONTAINER_LOCAL)

		return int(self.RemainsInitial() + sum(filter_findata.ToFloats(pid_amount).items))

	def TransferToNextDm(self):
		""" Перенос остатка итогового в следующий финпериод """
		if not self.FinstructOid(): return

		record_finstruct = C90_RecordFinstruct(self.FinstructOid())
		name   : str     = record_finstruct.Name()
		dy     : int     = record_finstruct.Dy()
		dm     : int     = record_finstruct.Dm()
		amount : int     = self.CalcRemainFinal()

		dy, dm           = CalcDyDmByShiftDm(dy, dm, 1)

		if not record_finstruct.SwitchByName(dy, dm, name): return

		record_finstate = C80_RecordFinstate()

		if not record_finstate.SwitchByFinstructOid(record_finstruct.Oid().text):
			record_finstate.GenerateOid()
			record_finstate.RegisterObject(CONTAINER_LOCAL)

		record_finstate.FinstructOid(record_finstruct.Oid().text)
		record_finstate.RemainsInitial(amount)


class C80_Finstate(C70_Finstate):
	""" Финсостояние: Логика данных """
	pass

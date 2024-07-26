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
	def SwitchByFinstructIdo(self, ido: str) -> bool:
		""" Переключение записи по OID финструктуры """
		filter_finstate = C30_FilterLinear1D(self.Idc().data)
		filter_finstate.FilterIdpVlpByEqual(self.f_finstruct_ido.Idp().data, ido)
		filter_finstate.Capture(CONTAINER_LOCAL)

		idos : list[str] = filter_finstate.Idos().data
		if not idos: return False

		self.Ido(idos[0])
		return True

	# Калькуляция данных
	def CalcIncomeOrOutcome(self, flag_income: bool = False) -> int:
		""" Расчёт дохода/расхода """
		record_finstruct      = C90_RecordFinstruct(self.FinstructIdo())
		flag_account_v : bool = bool(record_finstruct.ParentIdo())

		findata               = C40_RecordFindata()
		finactions            = C40_RecordFinactions()

		oci_findata    : str  = findata.Idc().data
		oci_finactions : str  = finactions.Idc().data

		filter_findata        = C30_FilterLinear1D(oci_finactions if flag_account_v else oci_findata)

		if flag_account_v:
			idp_amount    = finactions.f_amount.Idp().data
			idp_finstruct = finactions.f_finstruct_idos.Idp().data

			filter_findata.FilterIdpVlpByInclude(idp_finstruct, record_finstruct.Ido().data)
		else             :
			idp_amount    = findata.f_amount.Idp().data
			idp_finstruct = findata.f_finstruct_ido.Idp().data

			filter_findata.FilterIdpVlpByEqual(idp_finstruct, record_finstruct.Ido().data)

		if flag_income:	filter_findata.FilterIdpVlpByMore(idp_amount, 0)
		else          : filter_findata.FilterIdpVlpByLess(idp_amount, 0)

		filter_findata.Capture(CONTAINER_LOCAL)

		return sum(filter_findata.ToFloats(idp_amount).data)

	def CalcIncome(self) -> int:
		""" Расчёт дохода """
		return self.CalcIncomeOrOutcome(True)

	def CalcOutcome(self) -> int:
		""" Расчёт расхода """
		return self.CalcIncomeOrOutcome(False)

	def CalcRemainFinal(self) -> int:
		""" Расчёт остатка конечного с учётом финданных - финструктуры """
		record_finstruct      = C90_RecordFinstruct(self.FinstructIdo())
		flag_account_v : bool = bool(record_finstruct.ParentIdo())

		findata               = C40_RecordFindata()
		finactions            = C40_RecordFinactions()

		oci_findata    : str  = findata.Idc().data
		oci_finactions : str  = finactions.Idc().data

		filter_findata        = C30_FilterLinear1D(oci_finactions if flag_account_v else oci_findata)

		if flag_account_v:
			idp_amount    = finactions.f_amount.Idp().data
			idp_finstruct = finactions.f_finstruct_idos.Idp().data

			filter_findata.FilterIdpVlpByInclude(idp_finstruct, record_finstruct.Ido().data)
		else             :
			idp_amount    = findata.f_amount.Idp().data
			idp_finstruct = findata.f_finstruct_ido.Idp().data

			filter_findata.FilterIdpVlpByEqual(idp_finstruct, record_finstruct.Ido().data)

		filter_findata.Capture(CONTAINER_LOCAL)

		return int(self.RemainsInitial() + sum(filter_findata.ToFloats(idp_amount).data))

	def TransferToNextDm(self):
		""" Перенос остатка итогового в следующий финпериод """
		if not self.FinstructIdo(): return

		record_finstruct = C90_RecordFinstruct(self.FinstructIdo())
		name   : str     = record_finstruct.Name()
		dy     : int     = record_finstruct.Dy()
		dm     : int     = record_finstruct.Dm()
		amount : int     = self.CalcRemainFinal()

		dy, dm           = CalcDyDmByShiftDm(dy, dm, 1)

		if not record_finstruct.SwitchByName(dy, dm, name): return

		record_finstate = C80_RecordFinstate()

		if not record_finstate.SwitchByFinstructIdo(record_finstruct.Ido().data):
			record_finstate.GenerateIdo()
			record_finstate.RegisterObject(CONTAINER_LOCAL)

		record_finstate.FinstructIdo(record_finstruct.Ido().data)
		record_finstate.RemainsInitial(amount)


class C80_Finstate(C70_Finstate):
	""" Финсостояние: Логика данных """
	pass

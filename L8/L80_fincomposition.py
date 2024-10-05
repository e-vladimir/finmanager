# ФИНСОСТАВ: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL
from L00_fincomposition     import FINCOMPOSITION
from L70_fincomposition     import C70_Fincomposition, C70_FincompositionRecord


class C80_FincompositionRecord(C70_FincompositionRecord):
	""" Запись финсостава: Логика данных """

	# Выборки данных
	def SubNames(self) -> list[str]:
		""" Наименования вложенных записей """
		filter_data = C30_FilterLinear1D(self.Idc().data)
		filter_data.FilterIdpVlpByEqual(self.f_parent_ido.Idp().data, self.Ido().data)
		filter_data.Capture(CONTAINER_LOCAL)

		return filter_data.ToStrings(self.f_name.Idp().data, flag_sort=True).data

	def SubIdos(self, flag_include_struct: bool = False) -> list[str]:
		""" IDO вложенных записей """
		filter_data = C30_FilterLinear1D(self.Idc().data)
		filter_data.FilterIdpVlpByEqual(self.f_parent_ido.Idp().data, self.Ido().data)
		filter_data.Capture(CONTAINER_LOCAL)

		idos : list[str] = filter_data.Idos(self.f_name.Idp().data).data

		if not flag_include_struct: return idos

		for ido in idos.copy():
			subrecord = C80_FincompositionRecord(ido)

			idos.extend(subrecord.SubIdos(flag_include_struct))

		return idos

	def MoveUp(self):
		""" Перемещение вверх """
		if not self.ParentIdo(): return

		parent = C80_FincompositionRecord(self.ParentIdo())
		self.ParentIdo(parent.ParentIdo())


class C80_Fincomposition(C70_Fincomposition):
	""" Финсостав: Логика данных """

	pass

# АНАЛИТИКА ДАННЫХ: МЕХАНИКА ДАННЫХ
# 27 апр 2025

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L50_analytics          import C50_Analytics, C50_AnalyticsItem


class C60_AnalyticsItem(C50_AnalyticsItem):
	""" Элемент аналитики данных: Механика данных """

	# Название
	@property
	def name(self) -> str:
		return self.FName.ToString(CONTAINERS.DISK).data

	@name.setter
	def name(self, ido: str):
		self.FName.FromString(CONTAINERS.DISK, ido)


	# Корневой элемент
	@property
	def parent_ido(self) -> str:
		return self.FParentIdo.ToString(CONTAINERS.DISK).data

	@parent_ido.setter
	def parent_ido(self, ido: str):
		self.FParentIdo.FromString(CONTAINERS.DISK, ido)


	# IDO
	def SwitchByName(self, name: str) -> bool:
		""" Переключение по названию счёта """
		if not name: return False

		idc      : str = self.Idc().data
		idp_name : str = self.FName.Idp().data

		filter_data    = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_name, name)
		filter_data.Capture(CONTAINERS.DISK)

		try   : self.Ido(filter_data.Idos().data[0])
		except: return False

		return True


class C60_Analytics(C50_Analytics):
	""" Аналитика данных: Механика данных """
	pass

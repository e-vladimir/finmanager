# ФОРМА ФИНСТРУКТУРА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_finstruct import C80_FormFinstruct


class C90_FormFinstruct(C80_FormFinstruct):
	""" Форма Финструктура: Логика управления """

	# Форма
	def on_Show(self):
		super().on_Show()

		self.ShowTitle()

		self.InitModel()
		self.LoadFinstruct()

		self.AdjustTreeDataSort()
		self.AdjustTreeDataExpand()
		self.AdjustTreeDataColors()

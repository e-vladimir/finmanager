# ФОРМА ЭКСПОРТ ДАННЫХ: ЛОГИКА ДАННЫХ
# 01 апр 2025

from L00_form_export import EXPORT_FIELDS
from L70_form_export import C70_FormExport


class C80_FormExport(C70_FormExport):
	""" Форма экспорт данных: Логика данных """

	# Параметры экспорта операций
	def EditOptionsOperations(self):
		""" Редактирование параметров экспорта операций """

		match self.processing_field:
			case EXPORT_FIELDS.INTERVAL:
				self.SetOperationsIntervalMode()
				self.SetOperationsIntervalDy()
				self.SetOperationsIntervalDm()

			case EXPORT_FIELDS.ACCOUNTS:
				self.SetOperationsAccountsMode()
				self.SetOperationsAccountsGroup()
				self.SetOperationsAccountsAccount()

			case EXPORT_FIELDS.DIRECTORY:
				self.SetOperationsDirectory()

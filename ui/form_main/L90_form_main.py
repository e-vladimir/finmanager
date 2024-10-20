# ФОРМА ОСНОВНАЯ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_main import C80_FormMain


class C90_FormMain(C80_FormMain):
	""" Форма Основная: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Панель Утилиты
		self.btn_backups.clicked.connect(self.on_RequestOpenFormBackups)

	# Переход в другие формы
	def on_RequestOpenFormBackups(self):
		""" Запрос на открытие формы Архив данных """
		self.application.form_backups.Open()

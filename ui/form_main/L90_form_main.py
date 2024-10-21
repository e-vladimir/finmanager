# ФОРМА ОСНОВНАЯ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_main import C80_FormMain


class C90_FormMain(C80_FormMain):
	""" Форма Основная: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Панель Утилиты
		self.btn_archives.clicked.connect(self.on_RequestOpenFormArchives)

	# Переход в другие формы
	def on_RequestOpenFormArchives(self):
		""" Запрос на открытие формы Архив данных """
		self.application.form_archives.Open()

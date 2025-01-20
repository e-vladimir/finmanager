# УТИЛИТЫ
# Конвертор из выписки Сбербанк PDF в CSV
# 26 ноя 2024
# Формат данных в PDF - ноя 2024+

import PyPDF2

from G10_convertor_format import StringToDateTime

data : list[str] = []

with open('sber_input.pdf', 'rb') as file_input:
	raw       : list[str] = []
	reader                = PyPDF2.PdfReader(file_input)

	for page in reader.pages:
		text : str = page.extract_text()
		text       = text.replace('\xa0', '')
		raw.extend(text.split('\n'))

	blacklist : list[str] = []
	blacklist.append("Продолжение на следующей странице")
	blacklist.append("Для проверки подлинности")
	blacklist.append("1. Зайдите в приложение")
	blacklist.append("2. Нажмите кнопку")
	blacklist.append("3. Получите документ")
	blacklist.append("* Предоставляя QR-код")
	blacklist.append("Выписка по счёту")
	blacklist.append("ДАТА ОПЕРАЦИИ")
	blacklist.append("Дата обработки")
	blacklist.append("Описание операции")
	blacklist.append("Сумма в валюте")
	blacklist.append("операции²ОСТАТОК СРЕДСТВ")
	blacklist.append("В ВАЛЮТЕ")

	operation : str       = ""

	for raw_line in raw[19:-12]:
		flag_block   : bool = False

		for blacklist_item in blacklist:
			if blacklist_item in raw_line: flag_block = True

		if flag_block: continue

		header_dtime : str  = raw_line[ 0:16]
		header_id    : str  = raw_line[17:23]

		flag_header  : bool = header_id.isnumeric()
		flag_header        &= StringToDateTime(header_dtime) is not None

		if flag_header:
			if operation: data.append(operation.strip())
			operation  = ""

		operation += f" {raw_line}"


with open("sber_outup.csv", "w") as file_output:
	file_output.write(';'.join(["Дата", "Время", "Сумма", "Тип операции", "Описание"]) + ';\n')

	for data_item in data:
		data_items            = data_item.split(' ')
		if not data_items: continue

		operation_date        = data_items[0]
		operation_time        = data_items[1]
		operation_id          = data_items[2]
		operation_type        = ""
		operation_amount      = ""
		operation_description = ""

		for index_subdata, subdata in enumerate(data_items[3:], 3):
			if StringToDateTime(subdata) is None: continue

			operation_amount = '-' + data_items[index_subdata - 2]
			operation_amount = operation_amount.replace('-+', '+')
			operation_type   = ' '.join(data_items[3:index_subdata - 2])
			operation_description = ' '.join(data_items[index_subdata + 1:])

			break

		file_output.write(';'.join([operation_date, operation_time, operation_amount, operation_type, operation_description]) + ';\n')

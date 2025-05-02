class clss:
	def __init__(self):
		self.item = ""

def update_dict(key, value, defaults = clss()):
	value_from = defaults.item
	defaults.item = value

	print(value_from + '->' + defaults.item)


update_dict(key='fruit', value='apple', defaults=clss())
update_dict(key='car', value='ferrari')
update_dict(key='car', value='ferrari2')

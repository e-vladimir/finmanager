def update_dict(key, value, defaults=[]):
	defaults.append(value)
	print(defaults)


update_dict(key='fruit', value='apple')
update_dict(key='vegetable', value='tomato', defaults=['tree'])
update_dict(key='car', value='ferrari')

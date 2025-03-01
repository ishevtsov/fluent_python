def dump(**kwargs):
	return kwargs

result = dump(**{'x': 1}, **{'z': 3}, y=2)
print(result)
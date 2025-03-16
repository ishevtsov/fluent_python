def tag(name, *content, class_=None, **attrs):
	"""Generate one or more HTML tags"""
	if class_ is not None:
		attrs['class'] = class_
	attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
	attr_str = ''.join(attr_pairs)
	if content:
		elements = (f'<{name}{attr_str}>{c}</{name}>' for c in content)
		return '\n'.join(elements)
	else:
		return f'<{name}{attr_str} />'

result = tag('br')
print(result)
print()

result = tag('p', 'hello')
print(result)
print()

result = tag('p', 'hello', 'world')
print(result)
print()

result = tag('p', 'hello', id=33)
print(result)
print()

result = tag('p', 'hello', 'world', class_='sidebar')
print(result)
print()

result = tag(content='testing', name='img')
print(result)
print()

my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'class': 'framed'}
result = tag(**my_tag)
print(result)
print()
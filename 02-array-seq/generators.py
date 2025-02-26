import array

symbols = '$¢£¥€¤'
print(tuple(ord(s) for s in symbols))
print(array.array('I', (ord(s) for s in symbols)))

colors = ['black', 'white']
sizes = ['S', 'L']
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
	print(tshirt)
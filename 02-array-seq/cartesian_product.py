colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# This generates a list of tuples arranged by color, then size.
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# This generates a list of tuples arranged by size, then color.
tshirts = [(color, size) for size in sizes
							for color in colors]
print(tshirts)
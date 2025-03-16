def factorial(n):
	"""returns n!"""
	return 1 if n < 2 else n * factorial(n - 1)

def main():
	result = factorial(42)
	print(result)
	print(factorial.__doc__)
	print(type(factorial))

if __name__ == '__main__':
	main()
def factorial(n):
	'''returns n!'''
	return 1 if n < 2 else n * factorial(n - 1)

def main():
	print(factorial(42))
	print(factorial.__doc__)

if __name__ == '__main__':
	main()
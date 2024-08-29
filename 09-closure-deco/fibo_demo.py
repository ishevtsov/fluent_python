from clockdeco import clock

@clock
def fibonacci(n):
	if n < 2:
		return n
	return fibonacci(n - 2) + fibonacci(n - 1)


def main():
	print(fibonacci(30))


if __name__ == '__main__':
	main()
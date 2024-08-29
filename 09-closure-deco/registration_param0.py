registry = []

def register(func):
	print(f'running register({func})')
	registry.append(func)
	return func

@register
def f1():
	print('running f1()')

def main():
	print('running main()')
	print('registry ->', registry)
	f1()

if __name__ == '__main__':
	main()
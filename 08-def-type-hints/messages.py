from typing import Optional

def show_count(count: int, singular: str, plural: Optional[str] = None) -> str:
	if count == 1:
		return f'1 {singular}'
	count_str = str(count) if count else 'no'
	if not plural:
		plural = singular + 's'
	return f'{count_str} {plural}'

def main():
	print(show_count(99, 'bird'))
	print(show_count(1, 'bird'))
	print(show_count(0, 'bird'))

if __name__ == '__main__':
	main()
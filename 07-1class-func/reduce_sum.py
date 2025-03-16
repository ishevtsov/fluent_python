from functools import reduce
from operator import add

result = reduce(add, range(100))
print(result)

result = sum(range(100))
print(result)
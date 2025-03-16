from factorial import factorial

# map
result = map(factorial, range(6))
print(list(result))
# same result with list comprehension
result = [factorial(n) for n in range(6)]
print(result)

# map + filter
result = map(factorial, filter(lambda n: n % 2, range(6)))
print(list(result))
# same result with list comprehension
result = [factorial(n) for n in range(6) if n % 2]
print(result)

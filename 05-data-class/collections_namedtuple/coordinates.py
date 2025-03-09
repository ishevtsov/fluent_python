from collections import namedtuple

Coordinate = namedtuple('Coordinate', 'lat lon')

print(issubclass(Coordinate, tuple))

moscow = Coordinate(55.76, 37.617)
print(moscow)


print(moscow == Coordinate(55.76, 37.617))
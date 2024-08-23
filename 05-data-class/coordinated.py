class Coordinate:
	def __init__(self, lat, lon):
		self.lat = lat
		self.lon = lon

moscow = Coordinate(55.76, 37.62)
print(moscow)

location = Coordinate(55.76, 37.62)
print(location == moscow)

print((location.lat, location.lon) == (moscow.lat, moscow.lon))
print()


from collections import namedtuple
Coordinate = namedtuple('Coordinate', 'lat lon')
print(issubclass(Coordinate, tuple))

moscow = Coordinate(55.76, 37.62)
print(moscow)

print(moscow == Coordinate(55.76, 37.62))
print()


import typing
Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])
print(issubclass(Coordinate, tuple))

print(typing.get_type_hints(Coordinate))


from typing import NamedTuple
class Coordinate(NamedTuple):
	lat: float
	lon: float

	def __str__(self):
		ns = 'N' if self.lat >= 0 else 'S'
		we = 'E' if self.lon >= 0 else 'W'
		return f'{abs(self.lat):.1f}{ns}, {abs(self.lon):.1f}{we}'


from dataclasses import dataclass
@dataclass(frozen=True)
class Coordinate:
	lat: float
	lon: float

	def __str__(self):
		ns = 'N' if self.lat >= 0 else 'S'
		we = 'E' if self.lon >= 0 else 'W'
		return f'{abs(self.lat):.1f}{ns}, {abs(self.lon):.1f}{we}'
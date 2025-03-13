from collections import namedtuple
Coordinate = namedtuple('Coordinate', 'lat lon')
print(issubclass(Coordinate, tuple))
moscow = Coordinate(55.7558, 37.6173)
print(moscow)
print(moscow==Coordinate(55.7558, 37.6173))



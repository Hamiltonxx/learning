matro_areas = [
    ('Tokyo', 'JP', 36.933, (35.681236, 139.770366)),
    ('Delhi NCR', 'IN', 21.935, (28.613939, 77.209021)),
    ('Mexico City', 'MX', 20.142, (19.432607, -99.133209)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.5475, -46.635898)),
]

print(f"{'':15} | {'latitude':>9} | {'longitude':>9}")
for record in matro_areas:
    match record:
        case [name, _, _, (lat, lon)] if lon <= 0:
            print(f"{name:15} | {lat:9.4f} | {lon:9.4f}")

def check_status(status):
    match status:
        case 200:
            return "OK"
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case _:
            return "Unknown"
print(check_status(200))
print(check_status(400))
print(check_status(404))
print(check_status(500))

def analyze_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"Y-axis: {y}"
        case (x, 0):
            return f"X-axis: {x}"
        case (x, y):
            return f"({x}, {y})"
        case _:
            raise ValueError(f"Invalid point: {point}")

print(analyze_point((0, 0)))
print(analyze_point((0, 5)))
print(analyze_point((3, 0)))
print(analyze_point((3, 5)))
# print(analyze_point((0, 5, 8)))


def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}. 'author' is required")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f"Invalid record: {record!r}")

print(get_creators({'type': 'book', 'api': 2, 'authors': ['Raymond Hettinger', 'Ned Batchelder']}))
print(get_creators({'type': 'book', 'api': 1, 'author': 'Lerdorf'}))

b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Gödel, Escher, Bach')
b2 = dict(api=2, type='book', title='Python in a Nutshell', authors=['Alex Martelli', 'Anna Ravenscroft', 'Steve Holden'])
m1 = dict(api=1, type='movie', title='The Game', director='David Fincher')

from collections import OrderedDict
b4 = OrderedDict(api=2, type='book', title='Python in a Nutshell', authors=['Alex Martelli', 'Anna Ravenscroft', 'Steve Holden'])

for b in (b1, b2, m1, b4):
    print(get_creators(b))
    
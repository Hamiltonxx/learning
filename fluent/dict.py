dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

country_dial = {country: code for code, country in dial_codes}
print(country_dial)

country_code = {code: country.upper() for country, code in sorted(country_dial.items()) if code < 70}
print(country_code)

print({'a':0, **{'x':1}, 'y':2, **{'z':3, 'x':4, 'y':5}})

d1 = {'a':1, 'b':3}
d2 = {'a':2, 'b':4, 'c':6}
print({**d1, **d2})
print(d1 | d2)
print(d1)
d1 |= d2
print(d1)


import collections
ct = collections.Counter('abracadabra')
print(ct)
ct.update('aaaaazzz')
print(ct)
print(ct.most_common(3))









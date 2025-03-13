s = 'café'
print(len(s))
b = s.encode('utf-8')
print(b)
print(len(b))
print(b.decode('utf-8'))


cafe = bytes('café', encoding='utf-8')
print(cafe)
print(cafe[0])
print(cafe[:1])



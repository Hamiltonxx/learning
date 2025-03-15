def factorial(n):
    '''返回n!'''
    return 1 if n<2 else n * factorial(n-1)

print(factorial(10))
print(factorial.__doc__)
print(type(factorial))

fact = factorial
print(fact(5))
l = list(map(fact, range(11)))
print(l)
l2 = [fact(i) for i in range(11)]
print(l2)
l3 = [fact(i) for i in range(6) if i%2]
print(l3)

fruits = ["strawberry", "fig", "apple", "cherry", "raspberry", "banana"]
l4 = sorted(fruits, key=lambda word: word[::-1])
print(l4)

# func args
def tag(name, *contents, class_=None, **attrs):
    """生成一个或多个HTML标签"""
    if class_:
        attrs["class"] = class_
    attr_pairs = (f' {k}="{v}"' for k, v in sorted(attrs.items()))
    attr_str = ''.join(attr_pairs)
    if contents:
        return '\n'.join(f'<{name}{attr_str}>{c}</{name}>' for c in contents)
    else:
        return f'<{name}{attr_str} />'

print(tag('br'))
print(tag('p', 'hello'))


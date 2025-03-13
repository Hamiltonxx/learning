# 集合的基本作用是去重
l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
print(set(l))

# 去重的同时保留顺序
l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
print(dict.fromkeys(l).keys())

# & 交集, | 并集, - 差集, ^ 对称差集
# 子集, 超集 <=, <, >=, >
# 字典视图的集合运算
dict(a=1,b=2,c=3,d=4).keys() & dict(b=20,d=40,e=50).keys()

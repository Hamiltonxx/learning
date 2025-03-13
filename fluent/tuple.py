# count()
(1,2,3,2,4,2).count(2)
# index()
(1,2,3,4,5).index(3)
(1,2,3,2,4,5).index(2,2,5) # 从索引2到索引5之间查找2，=>3
# len()
len(1,2,3,4,5) # 5
# max() min()
max(1,2,3,4,5) # 5
min(1,2,3,4,5) # 1
str_tuple = ('apple', 'banana', 'orange', 'kiwi')
print(max(str_tuple, key=len))  # 按长度，结果: 'banana' 或 'orange'
print(min(str_tuple, key=len))  # 按长度，结果: 'kiwi'
# sorted()
sorted(str_tuple) # 按字母排序，结果: ['apple', 'banana', 'kiwi', 'orange']
sorted(str_tuple, key=len) # 按长度排序，结果: ['kiwi', 'apple', 'banana', 'orange']
# sum()
sum(1,2,3,4,5) # 15
# any() all()
any([1,2,3,4,5]) # True
all([1,2,3,4,5]) # True
all([1,2,3,4,0]) # False
# enumerate()
for index, value in enumerate(str_tuple, 1):
    print(f"索引 {index}: {value}") # 索引 1: apple 索引 2: banana 索引 3: orange 索引 4: kiwi
# zip()
tuple(zip((1,2,3),('a','b','c'))) # ((1, 'a'), (2, 'b'), (3, 'c'))

# 元组创建
t1 = (1, 2, 3)
t2 = 1, 2, 3
t3 = (1,)
t4 = () # 空元组
t5 = tuple('hello') # ('h', 'e', 'l', 'l', 'o')
t6 = tuple([1,2,3,4,5]) # (1, 2, 3, 4, 5)
t7 = tuple(range(5)) # (0, 1, 2, 3, 4)
# 连接元组
t8 = t1 + t2 + (4,5,6) # (1, 2, 3, 1, 2, 3, 4, 5, 6)
# 重复元组
t9 = t1 * 3 # (1, 2, 3, 1, 2, 3, 1, 2, 3)
# 成员检查
print(3 in t1) # True
print(3 not in t1) # False
# 切片操作
t10 = t1[1:3] # (2, 3)
t11 = t1[::-1] # (3, 2, 1)
# 元组解包
a, b, c = t1
print(a, b, c) # 1 2 3
first, *middle, last = t8 # first=1, middle=[2, 3, 4, 5], last=6
a,b = b,a # 交换a和b的值
# 类型转换
list((1,2,3,4,5)) # [1, 2, 3, 4, 5]
set((1,2,3,4,5)) # {1, 2, 3, 4, 5}
dict(('a',1),('b',2),('c',3)) # {'a': 1, 'b': 2, 'c': 3}

# 具名元组
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y) # 1 2


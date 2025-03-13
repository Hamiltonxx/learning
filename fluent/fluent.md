# 嵌套列表
```python
board = [['_'] * 3 for _ in range(3)]
print(board)
board[1][2] = 'X'
print(board)
```

# 增量赋值
乘法运算之后，列表还是同一个对象，只是追加了几项； 而对元组，则是创建了一个新元组。

# list.sort 与 sorted
list.sort 会就地排序，会修改原来的列表，返回值为 None； sorted 会返回一个新的列表，原来的列表不变。

# 用 bisect 来管理已排序的序列
bisect 模块包含两个主要函数，bisect 和 insort，两个函数都利用二分查找算法来在有序序列中查找或插入元素。

# queue, multiprocessing
queue 提供几个线程安全队列类，它们不像deque那样为了腾出空间而把项丢弃，而是在队列填满后阻塞插入新项，等待其他线程从队列中取出一项。利用这种行为可以限制活动线程的数量。  
multiprocessing 提供的队列类和queue包中的队列类很相似，只是专门针对进程间通信。

# dict
dict.setdefault(key, []).append(new_value)  
dict = collections.defaultdict(list)



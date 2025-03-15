# 装饰器通常会把一个函数替换成另一个函数
def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

target() # running inner()
print(target) # <function deco.<locals>.inner at 0x1006a80d0> 

# 装饰器在背后做的事:
# 1. 把被装饰的函数作为参数传给装饰器函数
# 2. 把装饰器函数的返回值赋值给被装饰的函数
# 3. 返回的函数会替代原来的函数，装饰器函数的返回值是inner函数
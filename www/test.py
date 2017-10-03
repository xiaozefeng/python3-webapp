# 解决闭包引用循环变量的问题
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j

            return g

        r = f(i)
        fs.append(r)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print('[%s] %s() ...' % (prefix, f.__name__))
            return f(*args, **kw)

        return wrapper

    return log_decorator


@log('info')
def test():
    pass


print(test())


def echo(value=None):
    while 1:
        value = (yield value)
        print('the values is %s' % value)
        if value:
            value += 1


g = echo(1)
print(g)
print(next(g))
print(g.send(2))
print(g.send(5))
print(next(g))


def reader():
    for i in range(4):
        yield '<< %s' % i


def reader_wrapper(g):
    for v in g:
        yield v


def reader_wrapper1(g):
    yield from g


wrap = reader_wrapper1(reader())
for i in wrap:
    print(i)



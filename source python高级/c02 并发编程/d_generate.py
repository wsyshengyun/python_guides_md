# coding:utf8


def coro():
    hello = yield "hello"
    yield hello


c = coro()
print(next(c))
print(c.send("World"))

import asyncio
import datetime
import random
import types


@types.coroutine
def my_sleep_func():
    yield from asyncio.sleep(random.randint(0, 5))


async def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await my_sleep_func()


def test_1():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(display_date(1, loop))
    asyncio.ensure_future(display_date(2, loop))
    loop.run_forever()


# test_1()


# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        count += 1
        total += new_num
        average = total/count


# 委托生成器
def proxy_gen():
    while True:
        yield from average_gen()


# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)
    print(calc_average.send(10))
    print(calc_average.send(20))
    print(calc_average.send(30))


if __name__ == '__main__':
    main()



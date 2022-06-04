# coding:utf8


from parse import parse
from parse import compile


flow = 'cookie=0x98, duration=2985, table=0, n_packets=480, n_bytes=2016'
reslut = parse('cookie={cookie}, duration={duration}, table={table}, n_packets={n_packets}, n_bytes={n_bytes}', flow)

print(reslut)
print(reslut["cookie"])
print(reslut["duration"])
print(reslut["table"])
print(reslut["n_packets"])
print(reslut["n_bytes"])


# 未命名
profile = parse("I am {}, {} year old, {}", "I am Jack, 27 year old, male")


# 重复使用pattern
pattern = compile("I am {}, {} year old, {}")
profile1 = pattern.parse("I am Jack, 27 year old, male")
profile2 = pattern.parse("I am Tom, 28 year old, male")

# 类型转化
profile3 = parse("I am {name:<}, {age:d} year old, {gender}", "I am Jack   , 27 year old, male")
print(profile3)
print(type(profile3['name']))
print(type(profile3['age']))

# 匹配时间
profile4 = parse("Meet at {time:tg}", "Meet at 1/2/2011 11:00 PM")
print(profile4)
print(profile4['time'])
print(type(profile4['time']))

# 精确匹配：指定最大字符数  :.num  字符最多为num个
parse('{:.2}{:2}', 'hello')
# 精确匹配：指定最小字符数  :num  字符最少为num个
parse('{:2}{:2}', 'hello')


# Parse 里有三个非常重要的属性
# fixed：利用位置提取的匿名字段的元组
# named：存放有命名的字段的字典
# spans：存放匹配到字段的位置
# 下面这段代码，带你了解他们之间有什么不同
profile6 = parse("I am {name}, {age:d} years old, {}", "I am Jack, 27 years old, male")
print(profile.fixed)
print(profile.named)
print(profile.spans)
# ('male',)
# {'age': 27, 'name': 'Jack'}
# {0: (25, 29), 'age': (11, 13), 'name': (5, 9)}


# . 自定义类型的转换
def myint(string):
    return int(string)


profile5 = parse("I am {:myint}", "I am 27", dict(myint=myint))

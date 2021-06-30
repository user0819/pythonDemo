# 无入参、无出参
def say_hello():
    print("hello")


# 有入参、无出参
def say_hello2(name):
    print("hello, " + name)


# 有入参、有出参
def add(num1, num2):
    return num1 + num2


# 出参为空
def add2(num1, num2):
    return None


if __name__ == '__main__':
    say_hello()
    say_hello2("test")
    print(add(1, 2))
    print(add2(1, 2))
    print('test', 'test1', sep=',', end=' (end)')

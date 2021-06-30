if __name__ == '__main__':
    # 简单if判断
    if 5 >= 3:
        print("True")

    # 完整if else 判断
    score = 80
    if score >= 80:
        print("good")
    elif score >= 60:
        print("normal")
    else:
        print("bad")

    # while判断
    num = 0
    name = 'ming'
    while num < 100:
        num = num + 1
        if num % 5 == 0:
            continue
        if num == 88 and name == 'ming':
            break
        print(num)

    # for循环：默认从0开始，不包含10
    for i in range(10):
        print(i)

    # for循环：限定从3开始
    for i in range(3, 10):
        print(i)

    # for循环：从1开始，步长为2
    for i in range(1, 10, 2):
        if i % 5 == 0:
            continue
        print(i)

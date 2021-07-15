if __name__ == '__main__':
    myDict = {True: 'Mike', False: 'liu'}
    print(myDict[True])

    # 定义一个dict
    myMap = {'name': 'Mike', 'age': 23, 'job': 'software engineer', 'salary': 20000}

    # 打印
    print(myMap['salary'])
    print(myMap)

    # 获取键列表
    myKeys = myMap.keys()
    print("keys: ")
    print(myKeys)

    # 获取值列表
    values = myMap.values()
    print("values: ")
    print(values)

    # 获取元素列表
    items = myMap.items()
    print('items: ')
    print(items)
    for k, v in items:
        print(str(k) + '->' + str(v))

    # 键不存在时，返回默认值
    salary = myMap.get('salary', 20000)
    print('salary: ' + str(salary))

    # 键不存在时，才赋值
    myMap.setdefault('salary', 30000)
    salary = myMap.get('salary', 20000)
    print('salary: ' + str(salary))

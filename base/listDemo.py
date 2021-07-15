if __name__ == '__main__':
    # 定义一个list
    myList = ['apple', 'banana', 'pear']

    # 打印输出
    print(myList)

    # 遍历打印
    for i in myList:
        print(i)

    # 获取长度
    length = len(myList)
    print(length)

    # 获取其中一个元素
    print(myList[2])
    print(myList[-1])

    # 查找其中一个元素位置
    index = myList.index('apple')
    print(index)

    # 增加一个元素
    myList.append('orange')

    # 增加一个元素 指定位置
    myList.insert(0, 'peach')

    # 修改一个元素
    myList[1] = myList[0]
    myList[0] = 'apple'
    print(myList)

    # 删除一个元素 通过索引
    del myList[0]
    print(myList)

    # 删除一个元素 通过值
    myList.remove('peach')
    print(myList)

    # 拼接list
    myList = myList + myList
    print(myList)

    # 复制list
    myList = myList * 2
    print(myList)

    subList = myList[2:4]
    print(subList)
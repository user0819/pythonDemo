import pyperclip

if __name__ == '__main__':
    str1 = 'hello'
    print(str1)

    # 双引号
    str2 = "hello"
    print(str2)

    # 转义符
    str3 = "this is Joe's Dog"
    str4 = "this is Joe\"s Dog"
    print(str3)
    print(str4)

    # 三重引号
    '''
     听说这个适合做注释
    '''
    str5 = '''
        三重引号里我想输入啥就输入啥：
        前提是不能再输给三重引号
        苏打粉''、s、' \s \str5
    '''
    print(str5)

    # 字符串下标和切片
    str6 = 'Hello world'
    str7 = str6[0:5]
    print(str7)

    # 字符串的in 和 not in
    str8 = 'hello world'
    judge = 'hello' in str8
    print(judge)

    judge = 'Hello' not in str8
    print(judge)

    #  upper() lower() isupper() islower()
    str9 = 'hello world'
    str10 = str9.upper()
    print(str10)
    print(str10.isupper())

    # 几个isX常用方法
    str11 = 'abc'
    str12 = '123'
    print(str11.isalpha())
    print(str11.isspace())
    print(str12.isdigit())
    print(str12.isnumeric())

    # startWith() endWith()
    str13 = 'hello world'
    print(str13.startswith('hello'))
    print(str13.endswith('world'))

    # join() split()
    str14 = ','.join(['a', 'b', 'c'])
    print(str14)
    myList = str14.split(',')
    print(myList)

    # rjust()、ljust() center()
    str15 = 'hello'
    str16 = str15.ljust(15, '*')
    str17 = str15.rjust(15, '*')
    str18 = str15.center(15, '*')
    print(str16)
    print(str17)
    print(str18)


    # strip() lstrip() rstrip()
    str19 = '  hello   '
    str20 = str19.lstrip()
    str21 = str19.rstrip()
    str22 = str19.strip()
    print(str20)
    print(str21)
    print(str22)

    # pyperclip() 复制粘贴至系统剪切板
    pyperclip.copy("myName is Joe")
    name = pyperclip.paste()
    print(name)


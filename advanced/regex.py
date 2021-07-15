import re

if __name__ == '__main__':
    # 创建regex
    regex = re.compile(r'\d')
    # 查询匹配  search返回第一条匹配的结果
    match = regex.search("23 jsa")
    # 打印结果
    print(match.group())

    # 使用（）分组
    regex2 = re.compile(r'(\d\d\d)-(\d\d\d\d)')
    match2 = regex2.search('333-4444- 333-6666')
    print(match2.group(0))

    # 使用管道符｜匹配多个分组
    regex3 = re.compile(r'Man|Woman')
    match3 = regex3.search('Wo are Man')
    print(match3.group())

    # 使用 ? 表示可选匹配 零次或一次
    regex4 = re.compile(r'bat(wo)?man')
    match4 = regex4.search('who is batwoman')
    print(match4.group())

    # 使用 * 号匹配零次或多次
    regex5 = re.compile(r'\d*')
    match5 = regex5.search('245251 sdf ')
    print(match5.group())


    # 使用 + 号匹配一次或多次
    regex6 = re.compile(r'\w+')
    match6 = regex6.search('sfa 24')
    print(match6.group())

    # 使用{} 匹配限定次数
    regex7 = re.compile(r'\w{5}')
    match7 = regex7.search('software soft 24')
    print(match7.group())

    regex8 = re.compile(r'\w{5,8}')
    match8 = regex8.search('software soft 24')
    print(match8.group())

    # 贪心匹配和非贪心匹配
    regex9 = re.compile(r'\w{5,8}?')
    match9 = regex9.search('software soft 24')
    print(match9.group())

    # findall方法
    regex10 = re.compile(r'\w{5,8}')
    list10 = regex10.findall('software television 24')
    print(list10)

    # 字符分类
    regex11 = re.compile(r'\d\w\s\D\W\S')
    match11 = regex11.search('4l w 2')
    print(match11.group())


    # 建立自己的字符分类
    regex12 = re.compile(r'[0-9a-zA-Z]*')
    match12 = regex12.search('test2353765dt ,kji')
    print(match12.group())


    # 插入字符和美元字符
    regex13 = re.compile(r'^a\w*')
    match13 = regex13.search('adt ,kji')
    print(match13.group())

    regex14 = re.compile(r'\w*i$')
    match14 = regex14.search('adt ,kji')
    print(match14.group())

    # 通配字符.
    regex15 = re.compile(r'.{5}')
    match15 = regex15.search('test2353   [][')
    print(match15.group())

    # 用.* 匹配所有字符
    regex16 = re.compile(r'.*')
    match16 = regex16.search('test2353   [][')
    print(match16.group())

    # 用.匹配换行
    regex17 = re.compile(r'.*', re.DOTALL)
    match17 = regex17.search('test2353   [][\n te')
    print(match17.group())

    # 不区分大小写的匹配
    regex18 = re.compile(r'test', re.IGNORECASE)
    match18 = regex18.search('TEST   []')
    print(match18.group())

    # 使用sub()方法替换匹配的字符串
    regex19 = re.compile(r'test', re.IGNORECASE)
    replace = regex19.sub('replace', 'TEST   soft')
    print(replace)
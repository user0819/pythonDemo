import webbrowser
import requests
import bs4

if __name__ == '__main__':
    # 打开新的网页
    #webbrowser.open('https://www.baidu.com')

    # 获取网页内容
    res = requests.get('https://www.baidu.com/')
    # 若请求失败直接抛出异常
    res.raise_for_status()
    print(type(res))
    print(res.status_code)
    print(res.text)
    # 保存网页内容到文件
    contentFile = open('contentFile.html', 'wb')
    for content in res.iter_content(100000):
        contentFile.write(content)
    contentFile.close()

    # 打开html文件
    htmlFile = open('contentFile.html')
    exampleSoup = bs4.BeautifulSoup(htmlFile.read(), features="html.parser")
    print(type(exampleSoup))
    suIdList = exampleSoup.select('div')
    print(type(suIdList))
    print(len(suIdList))
    for divElement in suIdList:
        print(divElement.getText())
        print(divElement.attrs)
        print('--------')

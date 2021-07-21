import os
import zipfile

if __name__ == '__main__':

    # 用zipfile压缩文件
    myZip = zipfile.ZipFile('myZip.zip')
    fileList = myZip.namelist()
    print(fileList)


    # 读取zip文件
    helloFile = myZip.getinfo('myZip/hello.txt')
    size = helloFile.file_size
    print(size)

    # 从zip文件中解压缩
    myZip = zipfile.ZipFile('myZip.zip')
    myZip.extractall()
    myZip.close()


    # 创建和添加文件到zip中
    newZip = zipfile.ZipFile('newZip.zip', 'w')
    newZip.write('fileDemo.py', compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()

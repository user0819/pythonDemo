import os

if __name__ == '__main__':
    # 当前路径
    # /Users/xiang/software/workspaceForOthers/pythonProject/advanced
    cwd = os.getcwd()
    print(cwd)

    # 更换当前工作目录
    os.chdir('/Users/xiang/software/workspaceForOthers')
    cwd = os.getcwd()
    print(cwd)

    # 根据操作系统拼接路径
    myPath = os.path.join('Users', 'xiang', 'software')
    print(myPath)

    # 创建目录
    existFlag = os.path.exists('/Users/xiang/software/workspaceForOthers/addDir')
    if not existFlag:
        os.makedirs('/Users/xiang/software/workspaceForOthers/addDir')

    # 移除目录
    existFlag = os.path.exists('/Users/xiang/software/workspaceForOthers/addDir')
    if existFlag:
        os.removedirs('/Users/xiang/software/workspaceForOthers/addDir')


    # 获取绝对路径
    absPath = os.path.abspath('..')
    print(absPath)

    # 获取相对路径
    relPath = os.path.relpath('/Users/xiang/software/workspaceForOthers/addDir/addDir2')
    print(relPath)

    # 路径拆分成目录和文件名
    cwdPath = '/Users/xiang/software/workspaceForOthers'
    dirName = os.path.dirname(cwdPath)
    baseName = os.path.basename(cwdPath)
    print('dirName: ' + dirName)
    print('baseName:' + baseName)

    splitList = os.path.split(cwdPath)
    print('dirName: ' + dirName)
    print('baseName:' + baseName)    # 查看文件大小

    # 查看文件夹内容
    cwdPath = '/Users/xiang/software/workspaceForOthers'
    dirList = os.listdir(cwdPath)
    print('文件夹内容：' + str(dirList))

    size = os.path.getsize(cwdPath)
    print('文件大小：' + str(size))

    # 校验是否是文件或文件夹
    cwdPath = '/Users/xiang/software/workspaceForOthers'
    isDir = os.path.isdir(cwdPath)
    isFile = os.path.isfile(cwdPath)
    print('是目录吗：' + str(isDir))
    print('是文件吗：' + str(isFile))


    # 文件读
    cwdFilePath = '/Users/xiang/software/workspaceForOthers/hello.c'
    cwdFile = open(cwdFilePath)
    fileContext = cwdFile.read()
    print(fileContext)
    cwdFile.close()

    cwdFile2 = open(cwdFilePath)
    fileLinesList = cwdFile2.readlines()
    for line in fileLinesList:
        print(line)
    cwdFile2.close()

    # 文件写
    writeFilePath = '/Users/xiang/software/workspaceForOthers/test.txt'
    writeFile = open(writeFilePath, 'w')
    writeFile.write('this is test')
    cwdFile.close()

    # 文件追加
    writeFilePath = '/Users/xiang/software/workspaceForOthers/test.txt'
    writeFile = open(writeFilePath, 'a')
    writeFile.write('\nthis is test append')
    cwdFile.close()

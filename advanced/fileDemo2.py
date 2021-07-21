import os
import shutil

if __name__ == '__main__':
    myPath = '/Users/xiang/software/workspaceForOthers/pythonProject/advanced/fileDemo2.py'
    print(myPath)

    # 复制文件
    myPath = '/Users/xiang/software/workspaceForOthers/pythonProject/advanced/fileDemo2.py'
    dest = '/Users/xiang/software/workspaceForOthers/pythonProject/advanced/fileDemo3.py'
    shutil.copy(myPath, dest)

    # 复制文件夹
    myDir = '/Users/xiang/software/workspaceForOthers/pythonProject/advanced'
    destDir = '/Users/xiang/software/workspaceForOthers/pythonProject/advanced2'
    shutil.copytree(myDir, destDir)

    # 文件移动、文件改名
    myFilePath = '/Users/xiang/software/workspaceForOthers/pythonProject/advanced/fileDemo3.py'
    myFileDest = '/Users/xiang/software/workspaceForOthers/pythonProject/advanced2/fileDemo4.py'
    shutil.move(myFilePath, myFileDest)


    # 永久删除文件和文件夹
    deleteFile = '/Users/xiang/software/workspaceForOthers/pythonProject/advanced2/fileDemo4.py'
    os.unlink(deleteFile)

    deleteDir = '/Users/xiang/software/workspaceForOthers/pythonProject/advanced2'
    # os.rmdir(deleteDir)
    shutil.rmtree(deleteDir)

    # 遍历目录树
    for folderName, subFolders, filenames in os.walk('/Users/xiang/software/workspaceForOthers/pythonProject'):
        print('The current folder is ' + folderName)

        for subFolder in subFolders:
            print('SUB_FOLDER OF ' + folderName + ': ' + subFolder)


        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': ' + filename)

        print('')




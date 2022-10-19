# -*- coding:utf8 -

#上边这个其实目前环境不加也行
import os
import sys
import tool


def unfullPath(x):
    try:
        luJing=input("输入文件所在相对路径:")
        wrd2search = input("输入要查询的东西:")
        inputList = os.listdir('./'+luJing)
        for day in inputList:
            (name, suffix) = os.path.splitext(day)#分离文件名与类型 文件名 .类型
            if( suffix == ".md"):
                dayPath = './'+luJing+'/'+day
                with open(dayPath,"r",encoding="utf-8") as file:
                    for line in file:
                        #比对是否含有匹配字符 存在则返回相对地址 不存在返回-1
                        if(line.find(wrd2search) != -1):
                            print(day)
                        pass
    except:
        print("路径或者文件有点问题吧？")

def fullPath(x):
    try:
        luJing = input("输入文件所在绝对路径:")
        wrd2search = input("输入要查询的东西:")
        inputList = os.listdir('./' + luJing)
        for day in inputList:
            (name, suffix) = os.path.splitext(day)  # 分离文件名与类型 文件名 .类型
            if (suffix == ".md"):
                dayPath = './' + luJing + '/' + day
                with open(dayPath, "r", encoding="utf-8") as file:
                    for line in file:
                        # 比对是否含有匹配字符 存在则返回相对地址 不存在返回-1
                        if (line.find(wrd2search) != -1):
                            print(day)
                        pass
    except:
        print("路径或者文件有点问题吧？")

def select_num(x,sign):
    print("reached")
    case = {
        "1" : unfullPath,
        "2" : fullPath
    }
    # case.get(x)
    ls_box = case.get(x)
    if ls_box:
        ls_box(x)

if __name__ == '__main__':
    # choice = dict()
    # choice["0"] = sys.exit()
    # choice["1"] = unfullPath()
    # choice["2"] = fullPath()
    while(True):
        currentPath = os.getcwd().replace('\\', '/')  # 获取当前路径
        print(currentPath)
        c = input("选择模式 0关闭 1相对路径 2绝对路径")
        x  = "useless"
        select_num(c,x)

# -*- coding:utf8 -
import os


def test():
    luJing=input("输入具体日期路径:")
    # path = './'
    inputList = os.listdir('./'+luJing)
    # print(inputList)
    for day in inputList:
        (name, suffix) = os.path.splitext(day)#分离文件名与类型 文件名 .类型
        # print(suffix)
        c = '.md'
        if suffix == c: #疑问 Python3可以用==比较字符串 但是必须基于两个变量？直接用值就不行？
            #解答 其实可以直接比较 估计是当时没加括号
            dayPath = './'+luJing+'/'+day
        # print(dayPath)
            with open(dayPath,"r",encoding="utf-8") as file:
                for line in file:
                    # print(line)

                    # cline = line.decode("GB2312").encode("utf-8")
                    # print(cline.strip())
                    #str1 = line#.decode("GB2312").encode("utf-8")
                    #str2 = wrd2search#.decode("GB2312").encode("utf-8")
                    # print(str1.find(str2))
                    # 不知道是不是Python3的原因 用不着费这么大劲↑

                    # print(line.find(wrd2search))
                    if(line.find(wrd2search) != -1):
                        print(day)

                    pass

if __name__ == '__main__':
    wrd2search = input("输入要查询的东西:")
    test()

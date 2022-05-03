# 扔出三粒骰子，三粒骰子得到的点数全不相同的概率是多少
'''
hhh蠢之又蠢的办法(主要想练习以下三维张量)
正常办法：6x5x4/6^3
'''
import numpy as np

def allNUmbers():
    allnumbers = np.zeros([6,6,6])
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                allnumbers[i-1][j-1][k-1] = i*100 + j*10 + k
    return allnumbers

def function(allnumbers):
    count = 0
    for i in range(0, 6):
        for j in range(0, 6):
            for k in range(0, 6):
                value = int(allnumbers[i][j][k])
                list = []
                while value:
                    list.append(value % 10)
                    value = value // 10
                print(list)
                if list[0] != list[1] and list[0] != list[2] and list[1] != list[2]:
                    count += 1
    return count / allnumbers.size

print(function(allNUmbers()))
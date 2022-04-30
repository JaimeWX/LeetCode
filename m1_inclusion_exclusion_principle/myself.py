# 某次考试，全班32人中，数学及格者20人，英语及格者有22人，两科皆及格者12人，两科皆不及格者有多少人

import numpy as np

def function(n,m,e,b):
    X = np.zeros((n, 2))
    X[0:m:, 0] += 1
    k = m-b # 数学及格但是英语不及格
    count = 0
    for i in range(e):
        if b == 0:
            X[i+k,1] += 1
        else:
            X[i,1] += 1
            b -=1
    for i in X:
        if i[0] + i[1] == 0:
            count += 1
    return count

n = 32
m = 20
e = 22
b = 12
function(n,m,e,b)

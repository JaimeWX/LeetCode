# 把一个整数减去1，再和原整数做与运算，会把该整数最右边的1变成0。
# 那么一个整数的二进制表示中有多少个1，就可以进行多少次这样的操作

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n = (n-1) & n
        return count

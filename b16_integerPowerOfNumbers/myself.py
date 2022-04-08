# 291/304 超时

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return x
        integer_power = 1
        abs_n = abs(n)
        while abs_n > 0 :
            integer_power = integer_power * x
            abs_n -= 1
        if n > 0:
            return integer_power
        else:
            return 1/integer_power

x = 2.00000
n = 0
ans = Solution()
print(ans.myPow(x,n))


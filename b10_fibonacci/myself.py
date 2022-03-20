# 从下往上计算
# f(2) = f(1) + f(0)
# f(3) = f(2) + f(1)
# f(4) = f(3) + F(2)
# ...

class Solution:
    def fib(self, n: int) -> int:
        f_nSubtract1 = 1
        f_nSubtract2 = 0
        fib = 0
        if n == 0:
            fib = 0
        elif n == 1:
            fib = 1
        else:
            f = 2
            while(f <= n):
                fib = f_nSubtract1 + f_nSubtract2
                f_nSubtract2 = f_nSubtract1
                f_nSubtract1 = fib
                f += 1
        return fib % 1000000007

n = 45
ans = Solution()
print(ans.fib(n))

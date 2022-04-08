class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = - n
        return self.Pow(x, n)
    def Pow(self, x, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            return (self.myPow(x, n // 2)) ** 2
        else:
            return (self.myPow(x, n // 2)) ** 2 * x


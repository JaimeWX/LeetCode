class Solution:
    def cuttingRope(self, n: int) -> int:
        # 解决绳子长度为2或3时的情况
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        timesOf3 = n//3
        if n - timesOf3 * 3 == 1:
            timesOf3 -= 1
        timesOf2 = (n - timesOf3 * 3) / 2
        return int(pow(3,timesOf3) * pow(2,timesOf2))

n = 8
ans = Solution()
print(ans.cuttingRope(n))


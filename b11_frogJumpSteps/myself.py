'''
求解思路
    把n级台阶时的跳法看成n的函数，记为f(n)
        当n>2时，第一次跳的时候有两种不同的选择：
            第一次跳一级，此时跳法数目等于后面剩下的n-1级台阶的跳法数目
            第一次跳二级，此时跳法数目等于后面剩下的n-2级台阶的跳法数目
        所以n级台阶的跳法数目为 f(n) = f(n-1) + f(n-2)
    总结：实际上就是斐波那契数列
'''

class Solution:
    def numWays(self, n: int) -> int:
        f_nSubtract1 = 1 # 1级台阶 2种跳法
        f_nSubtract2 = 1 # 0级台阶 1种跳法
        ways = 0
        if n == 0:
            ways = 1
        elif n == 1:
            ways = 1
        else:
            f = 2
            while (f <= n):
                ways = f_nSubtract1 + f_nSubtract2
                f_nSubtract2 = f_nSubtract1
                f_nSubtract1 = ways
                f += 1
        return ways % 1000000007

n = 7
ans = Solution()
print(ans.numWays(n))
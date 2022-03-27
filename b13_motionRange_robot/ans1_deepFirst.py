'''
有 个地方值得学习：
    通过分析得知机器人如果从(0,0)开始移动(题目要求)，按照题目要求，满足条件的只有只有向下或向右移动才行，所以递归中不用有向上或向左的部分；
    求行与列的位数和比较巧妙，充分结合了题目要求，没有硬算(但适用范围有限)；
    判断机器人是否访问过一个格子的方法使用了set()，而不是建立对应的布尔矩阵；
'''

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        print("a")
        def dfs(i, j, si, sj):
            print("b")

            if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
            visited.add((i,j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)
        print("c")
        visited = set()
        return dfs(0, 0, 0, 0)

m = 3
n = 4
k = 2
ans = Solution()
print(ans.movingCount(m,n,k))

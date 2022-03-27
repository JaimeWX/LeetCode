'''
依旧使用了对应题目要求的mxn布尔矩阵去判断 (递归可能不太行，尝试了其他人写的递归算法几乎相差无几)
执行用时：64 ms, 在所有 Python3 提交中击败了29.81%的用户
内存消耗：17.7 MB, 在所有 Python3 提交中击败了14.36%的用户
'''

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if k < 0 or m <= 0 or n <= 0:
            return 0
        grids = [[False] * n for i in range(m)]
        row = 0
        column = 0
        self.movingCountCore(row,column,m,n,grids,k)
        visitedNums = 0
        for i in grids:
            for j in i:
                if j == True:
                    visitedNums += 1
        del grids
        return visitedNums

    def movingCountCore(self,row,column,rows,columns,grids,k):
        validMoving = False
        if row >= 0 and row < rows and column >= 0 and column < columns and grids[row][column] == False and self.sumDigits(row,column) <= k:
            grids[row][column] = True
        # 上下左右
            validMoving = self.movingCountCore(row - 1, column, rows, columns, grids, k) or \
                          self.movingCountCore(row + 1, column, rows, columns, grids, k) or \
                          self.movingCountCore(row, column - 1, rows, columns, grids, k) or \
                          self.movingCountCore(row, column + 1, rows, columns, grids, k)
        return validMoving

    def sumDigits(self,row, column):
        result = []
        rowDigits = len(str(column))
        value = row * 10 ** rowDigits + column
        while value:
            result.append(value % 10)
            value = value // 10 # 整除整除！！！
        sumDigits = sum(result)
        return sumDigits

m = 38
n = 15
k = 9
ans = Solution()
print(ans.movingCount(m,n,k))

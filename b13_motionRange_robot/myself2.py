'''
根据ans优化myself: 这么写递归真的可以是int类型的！
    例如 m = 3 n = 4 k = 2
        movingCountCore(row + 1, column, rows, columns) == 2 表示向下的可达解
        movingCountCore(row, column + 1, rows, columns) == 3 表示向右的可达解
'''

class Solution:

    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()
        def movingCountCore(row,column,rows,columns):
            if row >= rows or column >= columns or (row,column) in visited or self.sumDigits(row,column) > k: return 0
            visited.add((row,column))
            return 1 + movingCountCore(row + 1, column, rows, columns) + movingCountCore(row, column + 1, rows, columns)
        return movingCountCore(0,0,m,n)

    def sumDigits(self,row, column):
        result = []
        rowDigits = len(str(column))
        value = row * 10 ** rowDigits + column
        while value:
            result.append(value % 10)
            value = value // 10 # 整除整除！！！
        sumDigits = sum(result)
        return sumDigits

m = 3
n = 4
k = 2
ans = Solution()
print(ans.movingCount(m,n,k))

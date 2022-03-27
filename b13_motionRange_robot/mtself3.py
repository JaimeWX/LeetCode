'''
我实在想不出来如果把if语句写成这样，怎么能让递归
ovingCountCore(row + 1, column, rows, columns) or movingCountCore(row, column + 1, rows,columns) 不是NoneType 而是 int
所以只能通过求set集合中的个数来判断可达解的数量
'''

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()
        def movingCountCore(row,column,rows,columns):
            if row < rows and column < columns and (row, column) not in visited and self.sumDigits(row, column) <= k:
                visited.add((row, column))
                movingCountCore(row + 1, column, rows, columns) or movingCountCore(row, column + 1, rows,columns)
        movingCountCore(0, 0, m, n)
        return len(visited)
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
'''
此题需要解决的几个关键问题
1. 给定序列的首字母可能在矩阵中多次出现，假设出现2次，当第一个位置的首字母无法解决，需要再次尝试第二个位置的首字母
2. 矩阵中的同一个元素不能重复访问，需要创建布尔矩阵记录某个元素是否访问
3. 递归的停止条件。只能用 index_word == len(word)
                不能用 index_word == len(word)-1 and board[row][column] == word[index_word] and     (visitList[row][column] == False)
    直观解释是不能用当前在矩阵中找到的元素等于序列的最后一个元素作为判断条件
'''
m
# index() 不能用于求二维数组某元素的索引(如果该二维数组中有重复元素)！！！

class Solution:
    def exist(self, board, word: str) -> bool:
        # 确定矩阵的行列数
        rows = len(board)
        columns = len(board[0])
        if len(word) > rows*columns:
            return False
        index_word = 0
        # 构建一个布尔矩阵记录矩阵中的某一个元素是否被访问
        visitList = [[False] * columns for i in range(rows)]
        # 查找word中的第一个字母是否在board中，如果在，找到第一个字母在矩阵中的位置
        # 第一个字母可能在矩阵中不止出现一次，意味着由多个位置，可能第一个位置的第一个字母找不到要求的序列，第二字母可以找到
        firstWord_position = []
        for j in board:
            for i in range(len(j)):
                if j[i] == word[0]:
                    i_position = []
                    row = board.index(j)
                    column = i
                    i_position.append(row)
                    i_position.append(column)
                    firstWord_position.append(i_position)
        while(len(firstWord_position) >= 1):
            row = firstWord_position[-1][0]
            column = firstWord_position[-1][1]
            if self.existPathCore(board, word, rows, columns, row, column, visitList, index_word):
                return True
            else:
                firstWord_position.pop(-1)
        return False

    def existPathCore(self,board,word,rows,columns,row,column,visitList,index_word):
        print(row,column)
        if row >= 0 and row < rows and column >= 0 and column < columns:
            print(board[row][column])
        if index_word == len(word)-1 :
            print(index_word)

            print("000")
            return True
        existPath = False
        if row >= 0 and row < rows and column >= 0 and column < columns and board[row][column] == word[index_word] and (visitList[row][column] == False):
            print("hhh")
            index_word += 1
            visitList[row][column] = True
            print(visitList)
            existPath = self.existPathCore(board, word, rows, columns, row - 1, column, visitList, index_word) or \
                        self.existPathCore(board, word, rows, columns, row + 1, column, visitList, index_word) or \
                        self.existPathCore(board, word, rows, columns, row, column - 1, visitList, index_word) or \
                        self.existPathCore(board, word, rows, columns, row, column + 1, visitList, index_word)
            if not existPath:
                print("xxxxxxxxxx")
                print(board[row][column])
                index_word -= 1
                print(index_word)
                visitList[row][column] = False
        return existPath



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
b1 = [["a","b"]]
w1 = "ba"
ans = Solution()
print(ans.exist(board,word))
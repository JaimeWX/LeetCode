# 解题思路：从右上角开始找，如果比T小，删行；比T大；删列
def findNumberIn2DArray(List,target):
    m = len(List) - 1
    n = len(List[0]) - 1
    first_row = 0
    if List:
        while(n>=0 and first_row<=m):
            print(List[first_row][n])
            #print("first_row=" + str(first_row))
            #print("n=" + str(n))
            if List[first_row][n] == target:
                return True
                break
            elif List[first_row][n] > target:
                n -= 1
            else:
                first_row += 1
        return False
    else:
        return False
List = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
       ]
target = 40

print(findNumberIn2DArray(List,target))

class Solution:
    def minArray(self, numbers) -> int:
        index1 = 0
        index2 = len(numbers)-1
        indexMid = index1
        # 按照旋转规则，输入数组中的第一个元素在绝大多数情况下是大于或等于最后一个元素的
        #   特殊情况：如果只旋转了原递增数组开头的前0个元素，也可构成旋转数组(实际上还是一个递增数组，这也是初始化indexMid = index1 的原因)
        while(numbers[index1] >= numbers[index2]):
            if index2 - index1 == 1:
                indexMid = index2
                break
            # 二分查找
            indexMid = int((index1+ index2)/2)
            #顺序查找解决 index1 == index2 == indexMid 的的情况
            if(numbers[index1] == numbers[index2] and numbers[indexMid] == numbers[index2]):
                print("hhh")
                smallestNumber = numbers[index1]
                for i in numbers:
                    if smallestNumber > i:
                        smallestNumber = i
                return smallestNumber
            #二分查找
            if numbers[indexMid] >= numbers[index1]:
                index1 = indexMid
            elif numbers[indexMid] <= numbers[index2]:
                index2 = indexMid
        return numbers[indexMid]

numbers = [3,3,1,3]
ans = Solution()
print(ans.minArray(numbers))
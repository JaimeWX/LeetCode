# 超出时间限制...
# 感觉完全是ML的思路hhh... 先找出假设空间，再找到所有与正例（a+b+c=0）一致的假设，最后用sorted()排除重复
from itertools import combinations
def threeSum(nums):
    outputList = []
    if len(nums) >= 3:
        threeList = list(combinations(nums,3))
        for i in threeList:
            if sum(i) == 0:
                if sorted(i) not in outputList:
                    outputList.append(sorted(i))
    return outputList

nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [0]
nums3 = [0,0,0]
nums4 = []
print(threeSum(nums3))

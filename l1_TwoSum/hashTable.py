# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
def twoSum(nums,target):
    hashTable = {}
    for i,num in enumerate(nums):
        if target - num in hashTable:
            return [hashTable[target - num], i]
        hashTable[nums[i]] = i
    return []

nums = [2,7,11,15]
target = 9
twoSum(nums,target)
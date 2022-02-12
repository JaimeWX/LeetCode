def twoSum2(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

array2 = [2, 2]
target = 4
print(twoSum2(array2,target))
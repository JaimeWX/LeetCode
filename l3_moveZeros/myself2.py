# 按顺序找到所有非0元素，然后顺序赋值给列表，剩下的用0填充
def moveZeros(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    while index < len(nums):
        nums[index] = 0
        index += 1
    return nums

nums1 = [0,0,1]
nums2 = [0,1,0,3,12]
print(moveZeros(nums1))
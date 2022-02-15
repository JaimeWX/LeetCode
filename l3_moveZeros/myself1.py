# 把所有0都删了，再添加到末尾
def moveZeros(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)
    return nums

nums = [0,0,1]
print(moveZeros(nums))


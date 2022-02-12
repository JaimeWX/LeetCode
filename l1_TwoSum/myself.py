#双重for循环
def twoSum(nums,target):
    List = []
    for i in nums:
        i_index = nums.index(i)
        for j in nums[i_index+1:]:
            if i+j == target:
                if i == j:
                    repeat = i
                    #找出列表中重复元素的索引
                    List = [r for r, x in enumerate(nums) if x == repeat]
                else:
                    List.append(nums.index(i))
                    List.append(nums.index(j))
    return List
array2 = [2,2]
target = 4
print(twoSum(array2,target))
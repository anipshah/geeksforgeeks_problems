def smallestPositive(nums):
    if nums == []:
        return 1
    nums.sort()
    if max(nums) <= 0:
        return 1
    for i in range(max(nums) + 1):
        if i not in nums:
            if i != 0:
                return i

    return max(nums) + 1
ar=[0,2,1,3,5]
print(smallestPositive(ar))
